# Production Configuration Template

## Production Configuration Template

```typescript
// config/production.ts
import { LinearClient } from "@linear/sdk";

export const config = {
  linear: {
    // Use secret manager, not environment variables directly
    apiKey: await getSecret("linear-api-key-prod"),
    webhookSecret: await getSecret("linear-webhook-secret-prod"),
  },
  rateLimit: {
    maxRetries: 5,
    baseDelayMs: 1000,
    maxDelayMs: 30000,
  },
  cache: {
    ttlSeconds: 300, // 5 minutes
    maxEntries: 1000,
  },
  timeouts: {
    requestMs: 30000,
    webhookProcessingMs: 5000,
  },
};

export function createProductionClient(): LinearClient {
  return new LinearClient({
    apiKey: config.linear.apiKey,
    // Add production-specific configuration
  });
}
```