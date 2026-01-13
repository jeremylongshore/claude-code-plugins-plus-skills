# Implementation: Rate Limiter Class

## Implementation: Rate Limiter Class

```typescript
// src/lib/apollo/rate-limiter.ts
interface RateLimiterConfig {
  maxRequests: number;
  windowMs: number;
  minSpacingMs: number;
}

class RateLimiter {
  private queue: Array<{
    resolve: (value: void) => void;
    reject: (error: Error) => void;
  }> = [];
  private requestTimestamps: number[] = [];
  private lastRequestTime = 0;
  private processing = false;

  constructor(private config: RateLimiterConfig) {}

  async acquire(): Promise<void> {
    return new Promise((resolve, reject) => {
      this.queue.push({ resolve, reject });
      this.processQueue();
    });
  }

  private async processQueue() {
    if (this.processing || this.queue.length === 0) return;
    this.processing = true;

    while (this.queue.length > 0) {
      // Clean old timestamps outside window
      const now = Date.now();
      this.requestTimestamps = this.requestTimestamps.filter(
        (ts) => now - ts < this.config.windowMs
      );

      // Check if we're at capacity
      if (this.requestTimestamps.length >= this.config.maxRequests) {
        const oldestTs = this.requestTimestamps[0];
        const waitTime = this.config.windowMs - (now - oldestTs) + 100;
        await this.wait(waitTime);
        continue;
      }

      // Enforce minimum spacing
      const timeSinceLastRequest = now - this.lastRequestTime;
      if (timeSinceLastRequest < this.config.minSpacingMs) {
        await this.wait(this.config.minSpacingMs - timeSinceLastRequest);
      }

      // Process next request
      const item = this.queue.shift()!;
      this.requestTimestamps.push(Date.now());
      this.lastRequestTime = Date.now();
      item.resolve();
    }

    this.processing = false;
  }

  private wait(ms: number): Promise<void> {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
}

// Create rate limiter for Apollo
export const apolloRateLimiter = new RateLimiter({
  maxRequests: 90, // Leave buffer below 100
  windowMs: 60000,
  minSpacingMs: 100, // 100ms between requests
});
```