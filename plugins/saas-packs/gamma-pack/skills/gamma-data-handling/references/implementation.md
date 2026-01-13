# Implementation Guide

### Step 1: Data Consent Management
```typescript
// models/consent.ts
interface UserConsent {
  userId: string;
  gammaDataProcessing: boolean;
  aiAnalysis: boolean;
  analytics: boolean;
  consentDate: Date;
  consentVersion: string;
}

async function checkConsent(userId: string, purpose: string): Promise<boolean> {
  const consent = await db.consents.findUnique({
    where: { userId },
  });

  if (!consent) {
    throw new ConsentRequiredError('User consent not obtained');
  }

  switch (purpose) {
    case 'presentation_creation':
      return consent.gammaDataProcessing;
    case 'ai_generation':
      return consent.gammaDataProcessing && consent.aiAnalysis;
    case 'analytics':
      return consent.analytics;
    default:
      return false;
  }
}

// Usage before Gamma operations
async function createPresentation(userId: string, data: object) {
  if (!await checkConsent(userId, 'presentation_creation')) {
    throw new Error('Consent required for presentation creation');
  }

  return gamma.presentations.create(data);
}
```

### Step 2: PII Handling
```typescript
// lib/pii-handler.ts
interface PIIField {
  field: string;
  type: 'email' | 'name' | 'phone' | 'address' | 'custom';
  action: 'mask' | 'hash' | 'encrypt' | 'remove';
}

const piiFields: PIIField[] = [
  { field: 'email', type: 'email', action: 'mask' },
  { field: 'name', type: 'name', action: 'hash' },
  { field: 'phone', type: 'phone', action: 'mask' },
];

function sanitizeForLogging(data: object): object {
  const sanitized = { ...data };

  for (const pii of piiFields) {
    if (sanitized[pii.field]) {
      switch (pii.action) {
        case 'mask':
          sanitized[pii.field] = maskValue(sanitized[pii.field]);
          break;
        case 'hash':
          sanitized[pii.field] = hashValue(sanitized[pii.field]);
          break;
        case 'remove':
          delete sanitized[pii.field];
          break;
      }
    }
  }

  return sanitized;
}

function maskValue(value: string): string {
  if (value.includes('@')) {
    // Email masking
    const [local, domain] = value.split('@');
    return `${local[0]}***@${domain}`;
  }
  // Generic masking
  return value.substring(0, 2) + '***' + value.substring(value.length - 2);
}
```

### Step 3: Data Retention Policies
```typescript
// services/data-retention.ts
interface RetentionPolicy {
  dataType: string;
  retentionDays: number;
  action: 'delete' | 'archive' | 'anonymize';
}

const policies: RetentionPolicy[] = [
  { dataType: 'presentation_exports', retentionDays: 1, action: 'delete' },
  { dataType: 'user_prompts', retentionDays: 30, action: 'anonymize' },
  { dataType: 'api_logs', retentionDays: 90, action: 'archive' },
  { dataType: 'presentations', retentionDays: 365, action: 'delete' },
];

async function enforceRetentionPolicies() {
  for (const policy of policies) {
    const cutoffDate = new Date();
    cutoffDate.setDate(cutoffDate.getDate() - policy.retentionDays);

    switch (policy.action) {
      case 'delete':
        await deleteExpiredData(policy.dataType, cutoffDate);
        break;
      case 'archive':
        await archiveExpiredData(policy.dataType, cutoffDate);
        break;
      case 'anonymize':
        await anonymizeExpiredData(policy.dataType, cutoffDate);
        break;
    }

    console.log(`Retention enforced for ${policy.dataType}`);
  }
}

// Run daily
scheduleJob('0 2 * * *', enforceRetentionPolicies);
```

### Step 4: GDPR Data Subject Requests
```typescript
// services/gdpr.ts
interface DataSubjectRequest {
  userId: string;
  type: 'access' | 'erasure' | 'portability' | 'rectification';
  requestDate: Date;
  status: 'pending' | 'processing' | 'completed';
}

async function handleAccessRequest(userId: string) {
  // Gather all user data
  const userData = {
    account: await db.users.findUnique({ where: { id: userId } }),
    presentations: await db.presentations.findMany({ where: { userId } }),
    exports: await db.exports.findMany({ where: { userId } }),
    consents: await db.consents.findMany({ where: { userId } }),
    activityLogs: await db.activityLogs.findMany({
      where: { userId },
      take: 1000,
    }),
  };

  // Include Gamma-stored data
  const gammaPresentations = await gamma.presentations.list({
    filter: { externalUserId: userId },
  });

  return {
    ...userData,
    gammaData: gammaPresentations,
    exportedAt: new Date().toISOString(),
  };
}

async function handleErasureRequest(userId: string) {
  // Delete from our database
  await db.presentations.deleteMany({ where: { userId } });
  await db.exports.deleteMany({ where: { userId } });
  await db.activityLogs.deleteMany({ where: { userId } });

  // Request deletion from Gamma
  const gammaPresentations = await gamma.presentations.list({
    filter: { externalUserId: userId },
  });

  for (const p of gammaPresentations) {
    await gamma.presentations.delete(p.id);
  }

  // Anonymize remaining data
  await db.users.update({
    where: { id: userId },
    data: {
      email: `deleted_${Date.now()}@anonymized.local`,
      name: 'Deleted User',
      deletedAt: new Date(),
    },
  });

  return { success: true, deletedCount: gammaPresentations.length + 1 };
}
```

### Step 5: Audit Trail
```typescript
// lib/audit.ts
interface AuditEntry {
  timestamp: Date;
  userId: string;
  action: string;
  resource: string;
  resourceId: string;
  details: object;
  ipAddress: string;
}

async function logAuditEvent(entry: Omit<AuditEntry, 'timestamp'>) {
  await db.auditLog.create({
    data: {
      ...entry,
      timestamp: new Date(),
    },
  });
}

// Usage
await logAuditEvent({
  userId: user.id,
  action: 'PRESENTATION_CREATED',
  resource: 'presentation',
  resourceId: presentation.id,
  details: { title: presentation.title },
  ipAddress: req.ip,
});
```