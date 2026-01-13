---
name: deepgram-security-basics
license: MIT
allowed-tools: Read, Grep, Bash
description: Apply deepgram security best practices for api key management and data
  protection. use when securing deepgram integrations, implementing key rotation,
  or auditing security configurations. trigger with phrases like "deepgram security",
  "deepgram ap...
---
# Deepgram Security Basics

## Overview
Implement security best practices for Deepgram API integration including key management, data protection, and access control.

## Prerequisites
- Deepgram Console access
- Understanding of environment variables
- Knowledge of secret management

## Security Checklist

- [ ] API keys stored in environment variables or secret manager
- [ ] Different keys for development/staging/production
- [ ] Key rotation schedule established
- [ ] Audit logging enabled
- [ ] Network access restricted
- [ ] Data handling compliant with regulations

## Instructions

### Step 1: Secure API Key Storage
Never hardcode API keys in source code.

### Step 2: Implement Key Rotation
Create a process for regular key rotation.

### Step 3: Set Up Access Control
Configure project-level permissions.

### Step 4: Enable Audit Logging
Track API usage and access patterns.

## Examples

### Environment Variable Configuration
```bash
# .env.example (commit this)
DEEPGRAM_API_KEY=your-api-key-here

# .env (NEVER commit this)
DEEPGRAM_API_KEY=actual-secret-key

# .gitignore
.env
.env.local
.env.*.local
```

### Secret Manager Integration (AWS)
```typescript
// lib/secrets.ts
import { SecretsManager } from '@aws-sdk/client-secrets-manager';

const client = new SecretsManager({ region: 'us-east-1' });

let cachedKey: string | null = null;
let cacheExpiry = 0;

export async function getDeepgramKey(): Promise<string> {
  // Use cached key if not expired
  if (cachedKey && Date.now() < cacheExpiry) {
    return cachedKey;
  }

  const response = await client.getSecretValue({
    SecretId: 'deepgram/api-key',
  });

  if (!response.SecretString) {
    throw new Error('Deepgram API key not found in Secrets Manager');
  }

  const secret = JSON.parse(response.SecretString);
  cachedKey = secret.DEEPGRAM_API_KEY;
  cacheExpiry = Date.now() + 300000; // 5 minute cache

  return cachedKey!;
}
```

### Secret Manager Integration (GCP)
```typescript
// lib/secrets-gcp.ts
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';

const client = new SecretManagerServiceClient();

export async function getDeepgramKey(): Promise<string> {
  const projectId = process.env.GCP_PROJECT_ID;
  const secretName = `projects/${projectId}/secrets/deepgram-api-key/versions/latest`;

  const [version] = await client.accessSecretVersion({ name: secretName });
  const payload = version.payload?.data?.toString();

  if (!payload) {
    throw new Error('Deepgram API key not found');
  }

  return payload;
}
```

### Key Rotation Script
```typescript
// scripts/rotate-key.ts
import { createClient } from '@deepgram/sdk';

interface KeyRotationResult {
  oldKeyId: string;
  newKeyId: string;
  rotatedAt: Date;
}

export async function rotateDeepgramKey(
  adminKey: string,
  projectId: string
): Promise<KeyRotationResult> {
  const client = createClient(adminKey);

  // 1. Create new key
  const { result: newKey, error: createError } = await client.manage.createProjectKey(
    projectId,
    {
      comment: `Rotated key - ${new Date().toISOString()}`,
      scopes: ['usage:write', 'listen:*'],
      expiration_date: new Date(Date.now() + 90 * 24 * 60 * 60 * 1000), // 90 days
    }
  );

  if (createError) throw new Error(`Failed to create key: ${createError.message}`);

  // 2. Test new key
  const testClient = createClient(newKey.key);
  const { error: testError } = await testClient.manage.getProjects();

  if (testError) {
    // Rollback: delete new key
    await client.manage.deleteProjectKey(projectId, newKey.key_id);
    throw new Error('New key validation failed');
  }

  // 3. Get old key ID (from current key metadata)
  const { result: keys } = await client.manage.getProjectKeys(projectId);
  const oldKey = keys?.api_keys.find(k =>
    k.comment?.includes('Current production key')
  );

  // 4. Update secret manager with new key
  // (Implementation depends on your secret manager)

  // 5. Delete old key after grace period
  if (oldKey) {
    console.log(`Old key ${oldKey.key_id} scheduled for deletion`);
    // Schedule deletion for later to allow propagation
  }

  return {
    oldKeyId: oldKey?.key_id || 'unknown',
    newKeyId: newKey.key_id,
    rotatedAt: new Date(),
  };
}
```

### Scoped API Keys
```typescript
// Create keys with minimal required permissions
const scopedKeys = {
  // Transcription-only key
  transcription: {
    scopes: ['listen:*'],
    comment: 'Read-only transcription key',
  },

  // Admin key (for key management only)
  admin: {
    scopes: ['manage:*'],
    comment: 'Administrative access only',
  },

  // Usage tracking key
  usage: {
    scopes: ['usage:read'],
    comment: 'Usage monitoring only',
  },
};

async function createScopedKey(
  adminKey: string,
  projectId: string,
  keyType: keyof typeof scopedKeys
) {
  const client = createClient(adminKey);
  const config = scopedKeys[keyType];

  const { result, error } = await client.manage.createProjectKey(
    projectId,
    config
  );

  if (error) throw error;
  return result;
}
```

### Request Sanitization
```typescript
// lib/sanitize.ts
export function sanitizeAudioUrl(url: string): string {
  const parsed = new URL(url);

  // Only allow HTTPS
  if (parsed.protocol !== 'https:') {
    throw new Error('Only HTTPS URLs are allowed');
  }

  // Block internal/local URLs
  const blockedHosts = ['localhost', '127.0.0.1', '0.0.0.0', '::1'];
  if (blockedHosts.includes(parsed.hostname)) {
    throw new Error('Local URLs are not allowed');
  }

  // Block private IP ranges
  const privateRanges = [
    /^10\./,
    /^172\.(1[6-9]|2[0-9]|3[0-1])\./,
    /^192\.168\./,
  ];

  if (privateRanges.some(range => range.test(parsed.hostname))) {
    throw new Error('Private IP addresses are not allowed');
  }

  return url;
}

export function sanitizeTranscriptResponse(response: unknown): unknown {
  // Remove any unexpected fields that might contain sensitive data
  if (typeof response !== 'object' || response === null) {
    return response;
  }

  const allowedFields = [
    'results',
    'metadata',
    'channels',
    'alternatives',
    'transcript',
    'confidence',
    'words',
    'start',
    'end',
  ];

  const sanitized: Record<string, unknown> = {};

  for (const [key, value] of Object.entries(response)) {
    if (allowedFields.includes(key)) {
      sanitized[key] = value;
    }
  }

  return sanitized;
}
```

### Audit Logging
```typescript
// lib/audit.ts
interface AuditEvent {
  timestamp: Date;
  action: string;
  projectId?: string;
  requestId?: string;
  userId?: string;
  ipAddress?: string;
  success: boolean;
  metadata?: Record<string, unknown>;
}

export class AuditLogger {
  private events: AuditEvent[] = [];

  log(event: Omit<AuditEvent, 'timestamp'>) {
    const fullEvent: AuditEvent = {
      ...event,
      timestamp: new Date(),
    };

    this.events.push(fullEvent);

    // In production, send to your logging service
    console.log(JSON.stringify({
      ...fullEvent,
      timestamp: fullEvent.timestamp.toISOString(),
    }));
  }

  async transcribe(
    transcribeFn: () => Promise<unknown>,
    context: { userId?: string; ipAddress?: string }
  ) {
    const startTime = Date.now();

    try {
      const result = await transcribeFn();

      this.log({
        action: 'TRANSCRIBE',
        success: true,
        userId: context.userId,
        ipAddress: context.ipAddress,
        metadata: {
          durationMs: Date.now() - startTime,
        },
      });

      return result;
    } catch (error) {
      this.log({
        action: 'TRANSCRIBE',
        success: false,
        userId: context.userId,
        ipAddress: context.ipAddress,
        metadata: {
          error: error instanceof Error ? error.message : 'Unknown error',
          durationMs: Date.now() - startTime,
        },
      });

      throw error;
    }
  }
}
```

### Data Protection
```typescript
// lib/data-protection.ts
import crypto from 'crypto';

// Encrypt transcripts at rest
export function encryptTranscript(transcript: string, key: Buffer): string {
  const iv = crypto.randomBytes(16);
  const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);

  let encrypted = cipher.update(transcript, 'utf8', 'hex');
  encrypted += cipher.final('hex');

  const authTag = cipher.getAuthTag();

  return JSON.stringify({
    iv: iv.toString('hex'),
    data: encrypted,
    tag: authTag.toString('hex'),
  });
}

export function decryptTranscript(encrypted: string, key: Buffer): string {
  const { iv, data, tag } = JSON.parse(encrypted);

  const decipher = crypto.createDecipheriv(
    'aes-256-gcm',
    key,
    Buffer.from(iv, 'hex')
  );

  decipher.setAuthTag(Buffer.from(tag, 'hex'));

  let decrypted = decipher.update(data, 'hex', 'utf8');
  decrypted += decipher.final('utf8');

  return decrypted;
}

// Redact sensitive information from transcripts
export function redactSensitiveData(transcript: string): string {
  const patterns = [
    // Credit card numbers
    { pattern: /\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b/g, replacement: '[REDACTED-CC]' },
    // SSN
    { pattern: /\b\d{3}[\s-]?\d{2}[\s-]?\d{4}\b/g, replacement: '[REDACTED-SSN]' },
    // Phone numbers
    { pattern: /\b\d{3}[\s-]?\d{3}[\s-]?\d{4}\b/g, replacement: '[REDACTED-PHONE]' },
    // Email addresses
    { pattern: /\b[\w.-]+@[\w.-]+\.\w+\b/g, replacement: '[REDACTED-EMAIL]' },
  ];

  let redacted = transcript;
  for (const { pattern, replacement } of patterns) {
    redacted = redacted.replace(pattern, replacement);
  }

  return redacted;
}
```

## Resources
- [Deepgram Security Overview](https://deepgram.com/security)
- [API Key Management](https://developers.deepgram.com/docs/api-key-management)
- [HIPAA Compliance](https://deepgram.com/hipaa)
- [SOC 2 Compliance](https://deepgram.com/soc2)

## Next Steps
Proceed to `deepgram-prod-checklist` for production deployment checklist.
