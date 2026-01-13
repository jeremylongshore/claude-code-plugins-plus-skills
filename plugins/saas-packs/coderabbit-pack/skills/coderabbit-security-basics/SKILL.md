---
name: coderabbit-security-basics
license: MIT
allowed-tools: Read, Write, Grep
description: Apply coderabbit security best practices for secrets and access control.
  use when securing api keys, implementing least privilege access, or auditing coderabbit
  security configuration. trigger with phrases like "coderabbit security", "coderabbit
  s...
---
# CodeRabbit Security Basics

## Overview
Security best practices for CodeRabbit API keys, tokens, and access control.

## Prerequisites
- CodeRabbit SDK installed
- Understanding of environment variables
- Access to CodeRabbit dashboard

## Instructions

### Step 1: Configure Environment Variables
```bash
# .env (NEVER commit to git)
CODERABBIT_API_KEY=sk_live_***
CODERABBIT_SECRET=***

# .gitignore
.env
.env.local
.env.*.local
```

### Step 2: Implement Secret Rotation
```bash
# 1. Generate new key in CodeRabbit dashboard
# 2. Update environment variable
export CODERABBIT_API_KEY="new_key_here"

# 3. Verify new key works
curl -H "Authorization: Bearer ${CODERABBIT_API_KEY}" \
  https://api.coderabbit.com/health

# 4. Revoke old key in dashboard
```

### Step 3: Apply Least Privilege
| Environment | Recommended Scopes |
|-------------|-------------------|
| Development | `read:*` |
| Staging | `read:*, write:limited` |
| Production | `Only required scopes` |

## Output
- Secure API key storage
- Environment-specific access controls
- Audit logging enabled

## Error Handling
| Security Issue | Detection | Mitigation |
|----------------|-----------|------------|
| Exposed API key | Git scanning | Rotate immediately |
| Excessive scopes | Audit logs | Reduce permissions |
| Missing rotation | Key age check | Schedule rotation |

## Examples

### Service Account Pattern
```typescript
const clients = {
  reader: new CodeRabbitClient({
    apiKey: process.env.CODERABBIT_READ_KEY,
  }),
  writer: new CodeRabbitClient({
    apiKey: process.env.CODERABBIT_WRITE_KEY,
  }),
};
```

### Webhook Signature Verification
```typescript
import crypto from 'crypto';

function verifyWebhookSignature(
  payload: string, signature: string, secret: string
): boolean {
  const expected = crypto.createHmac('sha256', secret).update(payload).digest('hex');
  return crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(expected));
}
```

### Security Checklist
- [ ] API keys in environment variables
- [ ] `.env` files in `.gitignore`
- [ ] Different keys for dev/staging/prod
- [ ] Minimal scopes per environment
- [ ] Webhook signatures validated
- [ ] Audit logging enabled

### Audit Logging
```typescript
interface AuditEntry {
  timestamp: Date;
  action: string;
  userId: string;
  resource: string;
  result: 'success' | 'failure';
  metadata?: Record<string, any>;
}

async function auditLog(entry: Omit<AuditEntry, 'timestamp'>): Promise<void> {
  const log: AuditEntry = { ...entry, timestamp: new Date() };

  // Log to CodeRabbit analytics
  await coderabbitClient.track('audit', log);

  // Also log locally for compliance
  console.log('[AUDIT]', JSON.stringify(log));
}

// Usage
await auditLog({
  action: 'coderabbit.api.call',
  userId: currentUser.id,
  resource: '/v1/resource',
  result: 'success',
});
```

## Resources
- [CodeRabbit Security Guide](https://docs.coderabbit.com/security)
- [CodeRabbit API Scopes](https://docs.coderabbit.com/scopes)

## Next Steps
For production deployment, see `coderabbit-prod-checklist`.