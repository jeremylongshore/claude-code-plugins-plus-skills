# Implementation: Exponential Backoff

## Implementation: Exponential Backoff

```typescript
// src/lib/apollo/backoff.ts
interface BackoffConfig {
  initialDelayMs: number;
  maxDelayMs: number;
  maxRetries: number;
  multiplier: number;
  jitter: boolean;
}

const defaultConfig: BackoffConfig = {
  initialDelayMs: 1000,
  maxDelayMs: 60000,
  maxRetries: 5,
  multiplier: 2,
  jitter: true,
};

export async function withBackoff<T>(
  fn: () => Promise<T>,
  config: Partial<BackoffConfig> = {}
): Promise<T> {
  const cfg = { ...defaultConfig, ...config };
  let lastError: Error;
  let delay = cfg.initialDelayMs;

  for (let attempt = 0; attempt <= cfg.maxRetries; attempt++) {
    try {
      await apolloRateLimiter.acquire();
      return await fn();
    } catch (error: any) {
      lastError = error;

      // Check if retryable
      const status = error.response?.status;
      if (status === 401 || status === 403 || status === 422) {
        throw error; // Don't retry auth/validation errors
      }

      if (attempt === cfg.maxRetries) {
        break;
      }

      // Get delay from Retry-After header or calculate
      const retryAfter = error.response?.headers?.['retry-after'];
      if (retryAfter) {
        delay = parseInt(retryAfter) * 1000;
      }

      // Add jitter to prevent thundering herd
      const jitter = cfg.jitter ? Math.random() * 1000 : 0;
      const actualDelay = Math.min(delay + jitter, cfg.maxDelayMs);

      console.log(`Retry ${attempt + 1}/${cfg.maxRetries} after ${actualDelay}ms`);
      await new Promise((r) => setTimeout(r, actualDelay));

      delay *= cfg.multiplier;
    }
  }

  throw lastError!;
}
```