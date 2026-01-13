---
name: deepgram-data-handling
description: |
  Implement audio data handling best practices for Deepgram integrations.
  Use when managing audio file storage, implementing data retention policies,
  or ensuring GDPR/HIPAA compliance for transcription data.
  Trigger with phrases like "deepgram data", "audio storage", "transcription data",
  "deepgram GDPR", "deepgram HIPAA", "deepgram privacy".
allowed-tools: Read, Write, Edit, Bash
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Deepgram Data Handling

## Overview
Best practices for handling audio data and transcriptions with Deepgram, including storage, retention, and compliance.

## Prerequisites
- Understanding of data protection regulations
- Cloud storage configured
- Encryption capabilities
- Data retention policies defined

## Data Lifecycle

```
Upload → Process → Store → Retain → Archive → Delete
  ↓         ↓        ↓        ↓         ↓        ↓
Encrypt  Transcribe  Save   Review   Compress  Secure
                                               Delete
```

## Compliance Considerations

| Regulation | Key Requirements |
|------------|------------------|
| GDPR | Data minimization, right to deletion, consent |
| HIPAA | PHI protection, access controls, audit logs |
| SOC 2 | Security controls, availability, confidentiality |
| PCI DSS | Data encryption, access logging |

## Instructions

### Step 1: Implement Secure Upload
Handle audio uploads with encryption and validation.

### Step 2: Configure Data Processing
Process transcriptions with privacy controls.

### Step 3: Set Up Storage
Store data with appropriate encryption and access controls.

### Step 4: Implement Retention
Automate data retention and deletion policies.

## Examples

### Secure Upload Handler
```typescript
// services/secure-upload.ts
import crypto from 'crypto';
import { S3Client, PutObjectCommand } from '@aws-sdk/client-s3';
import { KMSClient, GenerateDataKeyCommand } from '@aws-sdk/client-kms';

interface UploadOptions {
  userId: string;
  purpose: string;
  retentionDays: number;
  encrypted: boolean;
}

export class SecureAudioUpload {
  private s3: S3Client;
  private kms: KMSClient;
  private bucket: string;
  private kmsKeyId: string;

  constructor() {
    this.s3 = new S3Client({});
    this.kms = new KMSClient({});
    this.bucket = process.env.AUDIO_BUCKET!;
    this.kmsKeyId = process.env.KMS_KEY_ID!;
  }

  async upload(
    audioBuffer: Buffer,
    options: UploadOptions
  ): Promise<{ audioId: string; url: string }> {
    const audioId = crypto.randomUUID();

    // Validate audio
    if (!this.isValidAudio(audioBuffer)) {
      throw new Error('Invalid audio format');
    }

    // Generate encryption key
    let encryptedData = audioBuffer;
    let dataKey: string | undefined;

    if (options.encrypted) {
      const { encrypted, key } = await this.encryptData(audioBuffer);
      encryptedData = encrypted;
      dataKey = key;
    }

    // Calculate content hash
    const hash = crypto.createHash('sha256').update(audioBuffer).digest('hex');

    // Upload to S3
    const key = `audio/${options.userId}/${audioId}`;
    const expirationDate = new Date();
    expirationDate.setDate(expirationDate.getDate() + options.retentionDays);

    await this.s3.send(new PutObjectCommand({
      Bucket: this.bucket,
      Key: key,
      Body: encryptedData,
      ContentType: 'audio/wav',
      Metadata: {
        'user-id': options.userId,
        'purpose': options.purpose,
        'content-hash': hash,
        'encrypted': String(options.encrypted),
        'data-key': dataKey || '',
        'expiration-date': expirationDate.toISOString(),
      },
      ServerSideEncryption: 'aws:kms',
      SSEKMSKeyId: this.kmsKeyId,
    }));

    return {
      audioId,
      url: `s3://${this.bucket}/${key}`,
    };
  }

  private isValidAudio(buffer: Buffer): boolean {
    // Check for common audio file headers
    const headers = {
      wav: Buffer.from([0x52, 0x49, 0x46, 0x46]), // RIFF
      mp3: Buffer.from([0xFF, 0xFB]),
      flac: Buffer.from([0x66, 0x4C, 0x61, 0x43]), // fLaC
    };

    return Object.values(headers).some(header =>
      buffer.slice(0, header.length).equals(header)
    );
  }

  private async encryptData(data: Buffer): Promise<{
    encrypted: Buffer;
    key: string;
  }> {
    // Generate data key using KMS
    const { Plaintext, CiphertextBlob } = await this.kms.send(
      new GenerateDataKeyCommand({
        KeyId: this.kmsKeyId,
        KeySpec: 'AES_256',
      })
    );

    // Encrypt data with AES-256-GCM
    const iv = crypto.randomBytes(12);
    const cipher = crypto.createCipheriv('aes-256-gcm', Plaintext!, iv);

    const encrypted = Buffer.concat([
      iv,
      cipher.update(data),
      cipher.final(),
      cipher.getAuthTag(),
    ]);

    return {
      encrypted,
      key: CiphertextBlob!.toString('base64'),
    };
  }
}
```

### PII Redaction
```typescript
// services/pii-redaction.ts
interface RedactionRule {
  name: string;
  pattern: RegExp;
  replacement: string;
}

const redactionRules: RedactionRule[] = [
  {
    name: 'ssn',
    pattern: /\b\d{3}[-\s]?\d{2}[-\s]?\d{4}\b/g,
    replacement: '[SSN REDACTED]',
  },
  {
    name: 'credit_card',
    pattern: /\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b/g,
    replacement: '[CARD REDACTED]',
  },
  {
    name: 'phone',
    pattern: /\b(\+1[-\s]?)?\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4}\b/g,
    replacement: '[PHONE REDACTED]',
  },
  {
    name: 'email',
    pattern: /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/g,
    replacement: '[EMAIL REDACTED]',
  },
  {
    name: 'date_of_birth',
    pattern: /\b(0?[1-9]|1[0-2])[\/\-](0?[1-9]|[12]\d|3[01])[\/\-](19|20)\d{2}\b/g,
    replacement: '[DOB REDACTED]',
  },
];

export function redactPII(transcript: string): {
  redacted: string;
  redactions: Array<{ type: string; count: number }>;
} {
  let redacted = transcript;
  const redactions: Array<{ type: string; count: number }> = [];

  for (const rule of redactionRules) {
    const matches = redacted.match(rule.pattern);
    if (matches && matches.length > 0) {
      redactions.push({ type: rule.name, count: matches.length });
      redacted = redacted.replace(rule.pattern, rule.replacement);
    }
  }

  return { redacted, redactions };
}

// Deepgram has built-in redaction feature
export async function transcribeWithRedaction(
  client: DeepgramClient,
  audioUrl: string
): Promise<{ transcript: string; redactedTranscript: string }> {
  const { result, error } = await client.listen.prerecorded.transcribeUrl(
    { url: audioUrl },
    {
      model: 'nova-2',
      redact: ['pci', 'ssn', 'numbers'], // Deepgram's built-in redaction
      smart_format: true,
    }
  );

  if (error) throw error;

  const transcript = result.results.channels[0].alternatives[0].transcript;
  const { redacted } = redactPII(transcript);

  return { transcript, redactedTranscript: redacted };
}
```

### Data Retention Policy
```typescript
// services/retention.ts
import { S3Client, ListObjectsV2Command, DeleteObjectsCommand } from '@aws-sdk/client-s3';
import { db } from './database';
import { logger } from './logger';

interface RetentionPolicy {
  name: string;
  retentionDays: number;
  dataTypes: string[];
  complianceReasons: string[];
}

const policies: RetentionPolicy[] = [
  {
    name: 'standard',
    retentionDays: 30,
    dataTypes: ['audio', 'transcript'],
    complianceReasons: ['business'],
  },
  {
    name: 'legal_hold',
    retentionDays: 365 * 7, // 7 years
    dataTypes: ['audio', 'transcript', 'metadata'],
    complianceReasons: ['legal', 'regulatory'],
  },
  {
    name: 'hipaa',
    retentionDays: 365 * 6, // 6 years
    dataTypes: ['audio', 'transcript', 'access_logs'],
    complianceReasons: ['hipaa'],
  },
];

export class RetentionManager {
  private s3: S3Client;
  private bucket: string;

  constructor() {
    this.s3 = new S3Client({});
    this.bucket = process.env.AUDIO_BUCKET!;
  }

  async enforceRetention(): Promise<{
    checked: number;
    deleted: number;
    retained: number;
  }> {
    const stats = { checked: 0, deleted: 0, retained: 0 };
    const now = new Date();

    // Get all audio files
    const { Contents } = await this.s3.send(new ListObjectsV2Command({
      Bucket: this.bucket,
      Prefix: 'audio/',
    }));

    if (!Contents) return stats;

    const toDelete: string[] = [];

    for (const object of Contents) {
      stats.checked++;

      if (!object.Key) continue;

      // Get metadata to determine policy
      const metadata = await this.getMetadata(object.Key);
      const policy = this.getApplicablePolicy(metadata);
      const expirationDate = new Date(metadata.uploadDate);
      expirationDate.setDate(expirationDate.getDate() + policy.retentionDays);

      if (now > expirationDate && !metadata.legalHold) {
        toDelete.push(object.Key);
        stats.deleted++;
      } else {
        stats.retained++;
      }
    }

    // Batch delete
    if (toDelete.length > 0) {
      await this.deleteObjects(toDelete);
    }

    logger.info('Retention enforcement completed', stats);
    return stats;
  }

  private getApplicablePolicy(metadata: Record<string, string>): RetentionPolicy {
    // Determine which policy applies
    if (metadata.legalHold === 'true') {
      return policies.find(p => p.name === 'legal_hold')!;
    }
    if (metadata.hipaa === 'true') {
      return policies.find(p => p.name === 'hipaa')!;
    }
    return policies.find(p => p.name === 'standard')!;
  }

  private async deleteObjects(keys: string[]): Promise<void> {
    const batches = this.chunk(keys, 1000);

    for (const batch of batches) {
      await this.s3.send(new DeleteObjectsCommand({
        Bucket: this.bucket,
        Delete: {
          Objects: batch.map(Key => ({ Key })),
        },
      }));

      // Also delete from database
      await db.transcripts.deleteMany({
        audioKey: { $in: batch },
      });
    }
  }

  private chunk<T>(arr: T[], size: number): T[][] {
    return Array.from({ length: Math.ceil(arr.length / size) }, (_, i) =>
      arr.slice(i * size, i * size + size)
    );
  }

  private async getMetadata(key: string): Promise<Record<string, string>> {
    // Implementation to get object metadata
    return {};
  }
}
```

### GDPR Right to Deletion
```typescript
// services/gdpr.ts
import { db } from './database';
import { S3Client, DeleteObjectCommand, ListObjectsV2Command } from '@aws-sdk/client-s3';
import { logger } from './logger';

interface DeletionRequest {
  userId: string;
  requestedAt: Date;
  dataTypes: string[];
  verificationToken: string;
}

export class GDPRCompliance {
  private s3: S3Client;

  constructor() {
    this.s3 = new S3Client({});
  }

  async processRightToErasure(userId: string): Promise<{
    success: boolean;
    deletedItems: {
      transcripts: number;
      audioFiles: number;
      metadata: number;
    };
  }> {
    const deletedItems = {
      transcripts: 0,
      audioFiles: 0,
      metadata: 0,
    };

    try {
      // 1. Delete transcripts from database
      const transcriptResult = await db.transcripts.deleteMany({
        userId,
      });
      deletedItems.transcripts = transcriptResult.deletedCount;

      // 2. Delete audio files from S3
      const audioFiles = await this.listUserAudioFiles(userId);
      for (const file of audioFiles) {
        await this.s3.send(new DeleteObjectCommand({
          Bucket: process.env.AUDIO_BUCKET!,
          Key: file,
        }));
        deletedItems.audioFiles++;
      }

      // 3. Delete user metadata
      const metadataResult = await db.userMetadata.deleteMany({
        userId,
      });
      deletedItems.metadata = metadataResult.deletedCount;

      // 4. Log deletion for audit
      await this.logDeletion(userId, deletedItems);

      logger.info('GDPR erasure completed', { userId, deletedItems });

      return { success: true, deletedItems };
    } catch (error) {
      logger.error('GDPR erasure failed', {
        userId,
        error: error instanceof Error ? error.message : 'Unknown',
      });
      throw error;
    }
  }

  async exportUserData(userId: string): Promise<Buffer> {
    // Collect all user data
    const userData = {
      transcripts: await db.transcripts.find({ userId }).toArray(),
      metadata: await db.userMetadata.findOne({ userId }),
      usageHistory: await db.usage.find({ userId }).toArray(),
      exportedAt: new Date().toISOString(),
    };

    // Return as JSON
    return Buffer.from(JSON.stringify(userData, null, 2));
  }

  private async listUserAudioFiles(userId: string): Promise<string[]> {
    const { Contents } = await this.s3.send(new ListObjectsV2Command({
      Bucket: process.env.AUDIO_BUCKET!,
      Prefix: `audio/${userId}/`,
    }));

    return Contents?.map(c => c.Key!).filter(Boolean) || [];
  }

  private async logDeletion(
    userId: string,
    deletedItems: Record<string, number>
  ): Promise<void> {
    await db.auditLog.insertOne({
      action: 'GDPR_ERASURE',
      userId,
      deletedItems,
      timestamp: new Date(),
    });
  }
}
```

### Audit Logging
```typescript
// services/audit-log.ts
interface AuditEvent {
  timestamp: Date;
  action: string;
  userId: string;
  resourceType: 'audio' | 'transcript' | 'user';
  resourceId: string;
  details: Record<string, unknown>;
  ipAddress?: string;
  userAgent?: string;
}

export class AuditLogger {
  async log(event: Omit<AuditEvent, 'timestamp'>): Promise<void> {
    const fullEvent: AuditEvent = {
      ...event,
      timestamp: new Date(),
    };

    // Store in tamper-evident log
    await db.auditLog.insertOne({
      ...fullEvent,
      hash: this.computeHash(fullEvent),
    });

    // Also send to external SIEM if configured
    if (process.env.SIEM_ENDPOINT) {
      await this.sendToSIEM(fullEvent);
    }
  }

  private computeHash(event: AuditEvent): string {
    return crypto
      .createHash('sha256')
      .update(JSON.stringify(event))
      .digest('hex');
  }

  private async sendToSIEM(event: AuditEvent): Promise<void> {
    await fetch(process.env.SIEM_ENDPOINT!, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(event),
    });
  }
}
```

## Resources
- [Deepgram Security](https://deepgram.com/security)
- [GDPR Compliance Guide](https://developers.deepgram.com/docs/gdpr)
- [HIPAA Compliance](https://deepgram.com/hipaa)

## Next Steps
Proceed to `deepgram-enterprise-rbac` for access control configuration.
