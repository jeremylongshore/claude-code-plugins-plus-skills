# Implementation Guide

### Step 1: Secure API Key Storage
```typescript
// NEVER do this
const gamma = new GammaClient({
  apiKey: 'gamma_live_abc123...', // Hardcoded - BAD!
});

// DO this instead
const gamma = new GammaClient({
  apiKey: process.env.GAMMA_API_KEY,
});
```

**Environment Setup:**
```bash
# .env (add to .gitignore!)
GAMMA_API_KEY=gamma_live_abc123...

# Load in application
import 'dotenv/config';
```

### Step 2: Key Rotation Strategy
```typescript
// Support multiple keys for rotation
const gamma = new GammaClient({
  apiKey: process.env.GAMMA_API_KEY_PRIMARY
    || process.env.GAMMA_API_KEY_SECONDARY,
});

// Rotation script
async function rotateApiKey() {
  // 1. Generate new key in Gamma dashboard
  // 2. Update GAMMA_API_KEY_SECONDARY
  // 3. Deploy and verify
  // 4. Swap PRIMARY and SECONDARY
  // 5. Revoke old key
}
```

### Step 3: Request Signing (if supported)
```typescript
import crypto from 'crypto';

function signRequest(payload: object, secret: string): string {
  const timestamp = Date.now().toString();
  const message = timestamp + JSON.stringify(payload);

  return crypto
    .createHmac('sha256', secret)
    .update(message)
    .digest('hex');
}

// Usage with webhook verification
function verifyWebhook(body: string, signature: string, secret: string): boolean {
  const expected = crypto
    .createHmac('sha256', secret)
    .update(body)
    .digest('hex');

  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expected)
  );
}
```

### Step 4: Access Control Patterns
```typescript
// Scoped API keys (if supported)
const readOnlyGamma = new GammaClient({
  apiKey: process.env.GAMMA_API_KEY_READONLY,
  scopes: ['presentations:read', 'exports:read'],
});

const fullAccessGamma = new GammaClient({
  apiKey: process.env.GAMMA_API_KEY_FULL,
});

// Permission check before operations
async function createPresentation(user: User, data: object) {
  if (!user.permissions.includes('gamma:create')) {
    throw new Error('Insufficient permissions');
  }
  return fullAccessGamma.presentations.create(data);
}
```

### Step 5: Audit Logging
```typescript
import { GammaClient } from '@gamma/sdk';

function createAuditedClient(userId: string) {
  return new GammaClient({
    apiKey: process.env.GAMMA_API_KEY,
    interceptors: {
      request: (config) => {
        console.log(JSON.stringify({
          timestamp: new Date().toISOString(),
          userId,
          action: `${config.method} ${config.path}`,
          type: 'gamma_api_request',
        }));
        return config;
      },
    },
  });
}
```