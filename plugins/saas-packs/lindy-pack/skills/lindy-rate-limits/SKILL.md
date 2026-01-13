---
name: lindy-rate-limits
license: MIT
allowed-tools: Read, Write, Edit
description: Manage and optimize Lindy AI rate limits. Use when hitting rate limits,
  optimizing API usage, or implementing rate limit handling. Trigger with phrases
  like "lindy rate limit", "lindy quota", "lindy throttling", "lindy API limits".
---
# Lindy Rate Limits

## Overview
Comprehensive guide to understanding and managing Lindy API rate limits.

## Prerequisites
- Lindy SDK installed
- Understanding of your plan's limits
- Access to usage dashboard

## Rate Limit Tiers

### Free Tier
| Resource | Limit | Window |
|----------|-------|--------|
| API Requests | 100/min | Rolling |
| Agent Runs | 50/day | Daily |
| Concurrent Runs | 2 | Instant |

### Pro Tier
| Resource | Limit | Window |
|----------|-------|--------|
| API Requests | 1000/min | Rolling |
| Agent Runs | 1000/day | Daily |
| Concurrent Runs | 10 | Instant |

### Enterprise
| Resource | Limit | Window |
|----------|-------|--------|
| API Requests | Custom | Rolling |
| Agent Runs | Unlimited | - |
| Concurrent Runs | 100+ | Instant |

## Instructions

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

## Output
- Usage monitoring implementation
- Client-side rate limiter
- Retry logic for rate limit errors
- Optimized API usage patterns

## Error Handling
| Scenario | Strategy | Code |
|----------|----------|------|
| Near limit | Slow down | Reduce request rate |
| Hit limit | Wait | Respect Retry-After |
| Burst | Queue | Implement request queue |

## Examples

### Queue-Based Rate Limiting
```typescript
class RequestQueue {
  private queue: Array<() => Promise<void>> = [];
  private processing = false;
  private requestsThisMinute = 0;
  private lastMinuteStart = Date.now();

  async enqueue<T>(fn: () => Promise<T>): Promise<T> {
    return new Promise((resolve, reject) => {
      this.queue.push(async () => {
        try {
          resolve(await fn());
        } catch (e) {
          reject(e);
        }
      });
      this.processQueue();
    });
  }

  private async processQueue(): Promise<void> {
    if (this.processing) return;
    this.processing = true;

    while (this.queue.length > 0) {
      if (Date.now() - this.lastMinuteStart > 60000) {
        this.requestsThisMinute = 0;
        this.lastMinuteStart = Date.now();
      }

      if (this.requestsThisMinute >= 100) {
        await new Promise(r => setTimeout(r, 1000));
        continue;
      }

      const request = this.queue.shift()!;
      this.requestsThisMinute++;
      await request();
    }

    this.processing = false;
  }
}
```

## Resources
- [Lindy Rate Limits](https://docs.lindy.ai/rate-limits)
- [Usage Dashboard](https://app.lindy.ai/usage)
- [Upgrade Plans](https://lindy.ai/pricing)

## Next Steps
Proceed to `lindy-security-basics` for security configuration.
