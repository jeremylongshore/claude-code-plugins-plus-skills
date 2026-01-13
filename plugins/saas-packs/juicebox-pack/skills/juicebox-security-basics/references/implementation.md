# Implementation Guide

### Step 1: Secure API Key Storage

**NEVER do this:**
```typescript
// BAD - hardcoded API key
const client = new JuiceboxClient({
  apiKey: 'jb_prod_xxxxxxxxxxxxxxxxx'
});
```

**DO this instead:**
```typescript
// GOOD - environment variable
const client = new JuiceboxClient({
  apiKey: process.env.JUICEBOX_API_KEY
});
```

**For production, use secret managers:**
```typescript
// AWS Secrets Manager
import { SecretsManager } from '@aws-sdk/client-secrets-manager';

async function getApiKey(): Promise<string> {
  const client = new SecretsManager({ region: 'us-east-1' });
  const secret = await client.getSecretValue({
    SecretId: 'juicebox/api-key'
  });
  return JSON.parse(secret.SecretString!).apiKey;
}

// Google Secret Manager
import { SecretManagerServiceClient } from '@google-cloud/secret-manager';

async function getApiKey(): Promise<string> {
  const client = new SecretManagerServiceClient();
  const [version] = await client.accessSecretVersion({
    name: 'projects/my-project/secrets/juicebox-api-key/versions/latest'
  });
  return version.payload!.data!.toString();
}
```

### Step 2: Implement Access Controls
```typescript
// middleware/juicebox-auth.ts
export function requireJuiceboxAccess(requiredScope: string) {
  return async (req: Request, res: Response, next: NextFunction) => {
    const user = req.user;

    if (!user) {
      return res.status(401).json({ error: 'Authentication required' });
    }

    const hasScope = user.permissions.includes(`juicebox:${requiredScope}`);
    if (!hasScope) {
      return res.status(403).json({ error: 'Insufficient permissions' });
    }

    next();
  };
}

// Usage
app.get('/api/search',
  requireJuiceboxAccess('search:read'),
  async (req, res) => {
    // ... search logic
  }
);
```

### Step 3: Audit Logging
```typescript
// lib/audit-logger.ts
export class JuiceboxAuditLogger {
  async logAccess(event: AuditEvent): Promise<void> {
    const entry = {
      timestamp: new Date().toISOString(),
      userId: event.userId,
      action: event.action,
      resource: event.resource,
      ip: event.ip,
      userAgent: event.userAgent,
      success: event.success,
      metadata: event.metadata
    };

    await db.auditLogs.insert(entry);

    // Alert on suspicious activity
    if (this.isSuspicious(event)) {
      await this.sendAlert(entry);
    }
  }

  private isSuspicious(event: AuditEvent): boolean {
    return (
      event.action === 'bulk_export' ||
      event.metadata?.resultCount > 1000 ||
      this.isOffHours()
    );
  }
}
```

### Step 4: Data Privacy Compliance
```typescript
// lib/data-privacy.ts
export class DataPrivacyHandler {
  // Redact PII before logging
  redactPII(profile: Profile): RedactedProfile {
    return {
      ...profile,
      email: this.maskEmail(profile.email),
      phone: profile.phone ? '***-***-' + profile.phone.slice(-4) : undefined
    };
  }

  // Track data access for compliance
  async recordDataAccess(
    userId: string,
    profileIds: string[],
    purpose: string
  ): Promise<void> {
    await db.dataAccessLog.insert({
      userId,
      profileIds,
      purpose,
      timestamp: new Date(),
      retentionExpiry: addDays(new Date(), 90)
    });
  }

  // Handle data deletion requests
  async handleDeletionRequest(requestId: string): Promise<void> {
    // Remove from local cache/storage
    // Log compliance action
    // Notify relevant systems
  }
}
```