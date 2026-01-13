# Implementation Guide

### Step 1: Check Current Usage
```typescript
import { Lindy } from '@lindy-ai/sdk';

const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

async function checkUsage() {
  const usage = await lindy.usage.current();

  console.log('Current Usage:');
  console.log(`  API Requests: ${usage.apiRequests.used}/${usage.apiRequests.limit}`);
  console.log(`  Agent Runs: ${usage.agentRuns.used}/${usage.agentRuns.limit}`);
  console.log(`  Concurrent: ${usage.concurrent.active}/${usage.concurrent.limit}`);

  return usage;
}
```

### Step 2: Implement Rate Limiter
```typescript
class RateLimiter {
  private tokens: number;
  private lastRefill: number;
  private readonly maxTokens: number;
  private readonly refillRate: number; // tokens per second

  constructor(maxTokens: number, refillRate: number) {
    this.maxTokens = maxTokens;
    this.tokens = maxTokens;
    this.refillRate = refillRate;
    this.lastRefill = Date.now();
  }

  async acquire(): Promise<void> {
    this.refill();

    if (this.tokens < 1) {
      const waitTime = (1 - this.tokens) / this.refillRate * 1000;
      await new Promise(r => setTimeout(r, waitTime));
      this.refill();
    }

    this.tokens -= 1;
  }

  private refill(): void {
    const now = Date.now();
    const elapsed = (now - this.lastRefill) / 1000;
    this.tokens = Math.min(this.maxTokens, this.tokens + elapsed * this.refillRate);
    this.lastRefill = now;
  }
}

// Usage: 100 requests per minute
const limiter = new RateLimiter(100, 100 / 60);

async function rateLimitedRequest<T>(fn: () => Promise<T>): Promise<T> {
  await limiter.acquire();
  return fn();
}
```

### Step 3: Handle Rate Limit Errors
```typescript
async function withRetryOnRateLimit<T>(
  fn: () => Promise<T>,
  maxRetries = 5
): Promise<T> {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error: any) {
      if (error.code === 'LINDY_RATE_LIMITED') {
        const retryAfter = error.retryAfter || Math.pow(2, attempt);
        console.log(`Rate limited. Retrying in ${retryAfter}s...`);
        await new Promise(r => setTimeout(r, retryAfter * 1000));
        continue;
      }
      throw error;
    }
  }
  throw new Error('Max retries exceeded');
}
```