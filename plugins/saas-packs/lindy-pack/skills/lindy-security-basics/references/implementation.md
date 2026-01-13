# Implementation Guide

### Step 1: Secure API Key Storage
```typescript
// NEVER do this
const apiKey = 'lnd_abc123...'; // Hardcoded - BAD!

// DO this instead
const apiKey = process.env.LINDY_API_KEY;

// Or use secret management
import { SecretManager } from '@google-cloud/secret-manager';

async function getApiKey(): Promise<string> {
  const client = new SecretManager();
  const [secret] = await client.accessSecretVersion({
    name: 'projects/my-project/secrets/lindy-api-key/versions/latest',
  });
  return secret.payload?.data?.toString() || '';
}
```

### Step 2: Environment-Specific Keys
```bash
# .env.development
LINDY_API_KEY=lnd_dev_xxx
LINDY_ENVIRONMENT=development

# .env.production
LINDY_API_KEY=lnd_prod_xxx
LINDY_ENVIRONMENT=production
```

```typescript
// Validate environment
function validateEnvironment(): void {
  const env = process.env.LINDY_ENVIRONMENT;
  const key = process.env.LINDY_API_KEY;

  if (!key) {
    throw new Error('LINDY_API_KEY not set');
  }

  if (env === 'production' && key.startsWith('lnd_dev_')) {
    throw new Error('Development key used in production!');
  }
}
```

### Step 3: Configure Agent Permissions
```typescript
import { Lindy } from '@lindy-ai/sdk';

const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

async function createSecureAgent() {
  const agent = await lindy.agents.create({
    name: 'Secure Agent',
    instructions: 'Handle data securely.',
    permissions: {
      // Restrict to specific tools
      allowedTools: ['email', 'calendar'],
      // Prevent external network access
      networkAccess: 'internal-only',
      // Limit data access
      dataScopes: ['read:users', 'write:tickets'],
    },
  });

  return agent;
}
```

### Step 4: Audit Logging
```typescript
async function withAuditLog<T>(
  operation: string,
  fn: () => Promise<T>
): Promise<T> {
  const start = Date.now();
  const requestId = crypto.randomUUID();

  console.log(JSON.stringify({
    type: 'audit',
    operation,
    requestId,
    timestamp: new Date().toISOString(),
    status: 'started',
  }));

  try {
    const result = await fn();
    console.log(JSON.stringify({
      type: 'audit',
      operation,
      requestId,
      duration: Date.now() - start,
      status: 'completed',
    }));
    return result;
  } catch (error: any) {
    console.log(JSON.stringify({
      type: 'audit',
      operation,
      requestId,
      duration: Date.now() - start,
      status: 'failed',
      error: error.message,
    }));
    throw error;
  }
}
```