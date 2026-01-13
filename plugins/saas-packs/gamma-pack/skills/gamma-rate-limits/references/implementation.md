# Implementation Guide

### Step 1: Check Rate Limit Headers
```typescript
const response = await gamma.presentations.list();

// Rate limit headers
const headers = response.headers;
console.log('Limit:', headers['x-ratelimit-limit']);
console.log('Remaining:', headers['x-ratelimit-remaining']);
console.log('Reset:', new Date(headers['x-ratelimit-reset'] * 1000));
```

### Step 2: Implement Exponential Backoff
```typescript
async function withBackoff<T>(
  fn: () => Promise<T>,
  options = { maxRetries: 5, baseDelay: 1000 }
): Promise<T> {
  for (let attempt = 0; attempt < options.maxRetries; attempt++) {
    try {
      return await fn();
    } catch (err) {
      if (err.status !== 429 || attempt === options.maxRetries - 1) {
        throw err;
      }

      const delay = err.retryAfter
        ? err.retryAfter * 1000
        : options.baseDelay * Math.pow(2, attempt);

      console.log(`Rate limited. Retrying in ${delay}ms...`);
      await new Promise(r => setTimeout(r, delay));
    }
  }
  throw new Error('Max retries exceeded');
}

// Usage
const result = await withBackoff(() =>
  gamma.presentations.create({ title: 'My Deck', prompt: 'AI overview' })
);
```

### Step 3: Request Queue
```typescript
class RateLimitedQueue {
  private queue: Array<() => Promise<any>> = [];
  private processing = false;
  private requestsPerMinute: number;
  private interval: number;

  constructor(requestsPerMinute = 60) {
    this.requestsPerMinute = requestsPerMinute;
    this.interval = 60000 / requestsPerMinute;
  }

  async add<T>(fn: () => Promise<T>): Promise<T> {
    return new Promise((resolve, reject) => {
      this.queue.push(async () => {
        try {
          resolve(await fn());
        } catch (err) {
          reject(err);
        }
      });
      this.process();
    });
  }

  private async process() {
    if (this.processing) return;
    this.processing = true;

    while (this.queue.length > 0) {
      const fn = this.queue.shift()!;
      await fn();
      await new Promise(r => setTimeout(r, this.interval));
    }

    this.processing = false;
  }
}

// Usage
const queue = new RateLimitedQueue(30); // 30 req/min

const results = await Promise.all([
  queue.add(() => gamma.presentations.create({ ... })),
  queue.add(() => gamma.presentations.create({ ... })),
  queue.add(() => gamma.presentations.create({ ... })),
]);
```

### Step 4: Monitor Usage
```typescript
async function getRateLimitStatus() {
  const status = await gamma.rateLimit.status();

  return {
    limit: status.limit,
    remaining: status.remaining,
    percentUsed: ((status.limit - status.remaining) / status.limit * 100).toFixed(1),
    resetAt: new Date(status.reset * 1000),
    resetIn: Math.ceil((status.reset * 1000 - Date.now()) / 1000),
  };
}

// Usage
const status = await getRateLimitStatus();
console.log(`Used ${status.percentUsed}% of rate limit`);
console.log(`Resets in ${status.resetIn} seconds`);
```