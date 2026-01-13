# Examples

### TypeScript Rate Limiter
```typescript
// lib/rate-limiter.ts
interface RateLimiterConfig {
  maxConcurrent: number;
  maxPerMinute: number;
  retryAttempts: number;
  baseDelay: number;
}

export class DeepgramRateLimiter {
  private queue: Array<{
    fn: () => Promise<unknown>;
    resolve: (value: unknown) => void;
    reject: (error: Error) => void;
  }> = [];
  private activeRequests = 0;
  private requestsThisMinute = 0;
  private minuteStart = Date.now();
  private config: RateLimiterConfig;

  constructor(config: Partial<RateLimiterConfig> = {}) {
    this.config = {
      maxConcurrent: config.maxConcurrent ?? 50,
      maxPerMinute: config.maxPerMinute ?? 500,
      retryAttempts: config.retryAttempts ?? 3,
      baseDelay: config.baseDelay ?? 1000,
    };
  }

  async execute<T>(fn: () => Promise<T>): Promise<T> {
    return new Promise((resolve, reject) => {
      this.queue.push({
        fn,
        resolve: resolve as (value: unknown) => void,
        reject,
      });
      this.processQueue();
    });
  }

  private async processQueue() {
    // Reset minute counter if needed
    const now = Date.now();
    if (now - this.minuteStart >= 60000) {
      this.requestsThisMinute = 0;
      this.minuteStart = now;
    }

    // Check limits
    if (this.activeRequests >= this.config.maxConcurrent) return;
    if (this.requestsThisMinute >= this.config.maxPerMinute) return;
    if (this.queue.length === 0) return;

    const { fn, resolve, reject } = this.queue.shift()!;
    this.activeRequests++;
    this.requestsThisMinute++;

    try {
      const result = await this.executeWithRetry(fn);
      resolve(result);
    } catch (error) {
      reject(error instanceof Error ? error : new Error(String(error)));
    } finally {
      this.activeRequests--;
      this.processQueue();
    }
  }

  private async executeWithRetry<T>(
    fn: () => Promise<T>,
    attempt = 0
  ): Promise<T> {
    try {
      return await fn();
    } catch (error) {
      const isRateLimited = error instanceof Error &&
        (error.message.includes('429') || error.message.includes('rate limit'));

      if (isRateLimited && attempt < this.config.retryAttempts) {
        const delay = this.config.baseDelay * Math.pow(2, attempt);
        const jitter = Math.random() * 1000;
        await new Promise(r => setTimeout(r, delay + jitter));
        return this.executeWithRetry(fn, attempt + 1);
      }

      throw error;
    }
  }

  getStats() {
    return {
      activeRequests: this.activeRequests,
      queuedRequests: this.queue.length,
      requestsThisMinute: this.requestsThisMinute,
    };
  }
}
```

### Exponential Backoff with Jitter
```typescript
// lib/backoff.ts
interface BackoffConfig {
  baseDelay: number;
  maxDelay: number;
  factor: number;
  jitter: boolean;
}

export class ExponentialBackoff {
  private attempt = 0;
  private config: BackoffConfig;

  constructor(config: Partial<BackoffConfig> = {}) {
    this.config = {
      baseDelay: config.baseDelay ?? 1000,
      maxDelay: config.maxDelay ?? 60000,
      factor: config.factor ?? 2,
      jitter: config.jitter ?? true,
    };
  }

  getDelay(): number {
    const exponential = this.config.baseDelay *
      Math.pow(this.config.factor, this.attempt);
    const capped = Math.min(exponential, this.config.maxDelay);

    if (this.config.jitter) {
      // Full jitter: random value between 0 and calculated delay
      return Math.random() * capped;
    }

    return capped;
  }

  increment(): void {
    this.attempt++;
  }

  reset(): void {
    this.attempt = 0;
  }

  async wait(): Promise<void> {
    const delay = this.getDelay();
    await new Promise(resolve => setTimeout(resolve, delay));
    this.increment();
  }
}

// Usage
const backoff = new ExponentialBackoff();

async function transcribeWithBackoff(url: string) {
  const maxAttempts = 5;

  for (let i = 0; i < maxAttempts; i++) {
    try {
      return await transcribe(url);
    } catch (error) {
      if (i === maxAttempts - 1) throw error;

      if (error instanceof Error && error.message.includes('429')) {
        console.log(`Rate limited, waiting ${backoff.getDelay()}ms...`);
        await backoff.wait();
      } else {
        throw error;
      }
    }
  }
}
```

### Circuit Breaker Pattern
```typescript
// lib/circuit-breaker.ts
enum CircuitState {
  CLOSED = 'CLOSED',
  OPEN = 'OPEN',
  HALF_OPEN = 'HALF_OPEN',
}

interface CircuitBreakerConfig {
  failureThreshold: number;
  resetTimeout: number;
  halfOpenRequests: number;
}

export class CircuitBreaker {
  private state = CircuitState.CLOSED;
  private failures = 0;
  private lastFailure = 0;
  private halfOpenSuccesses = 0;
  private config: CircuitBreakerConfig;

  constructor(config: Partial<CircuitBreakerConfig> = {}) {
    this.config = {
      failureThreshold: config.failureThreshold ?? 5,
      resetTimeout: config.resetTimeout ?? 30000,
      halfOpenRequests: config.halfOpenRequests ?? 3,
    };
  }

  async execute<T>(fn: () => Promise<T>): Promise<T> {
    if (this.state === CircuitState.OPEN) {
      if (Date.now() - this.lastFailure > this.config.resetTimeout) {
        this.state = CircuitState.HALF_OPEN;
        this.halfOpenSuccesses = 0;
      } else {
        throw new Error('Circuit breaker is OPEN');
      }
    }

    try {
      const result = await fn();

      if (this.state === CircuitState.HALF_OPEN) {
        this.halfOpenSuccesses++;
        if (this.halfOpenSuccesses >= this.config.halfOpenRequests) {
          this.state = CircuitState.CLOSED;
          this.failures = 0;
        }
      }

      return result;
    } catch (error) {
      this.recordFailure();
      throw error;
    }
  }

  private recordFailure() {
    this.failures++;
    this.lastFailure = Date.now();

    if (this.failures >= this.config.failureThreshold) {
      this.state = CircuitState.OPEN;
      console.log('Circuit breaker OPENED');
    }
  }

  getState(): CircuitState {
    return this.state;
  }
}
```

### Usage Monitor
```typescript
// lib/usage-monitor.ts
interface UsageStats {
  requestCount: number;
  audioSeconds: number;
  errorCount: number;
  rateLimitHits: number;
  startTime: Date;
}

export class DeepgramUsageMonitor {
  private stats: UsageStats = {
    requestCount: 0,
    audioSeconds: 0,
    errorCount: 0,
    rateLimitHits: 0,
    startTime: new Date(),
  };

  recordRequest(audioSeconds: number = 0) {
    this.stats.requestCount++;
    this.stats.audioSeconds += audioSeconds;
  }

  recordError(isRateLimit: boolean = false) {
    this.stats.errorCount++;
    if (isRateLimit) {
      this.stats.rateLimitHits++;
    }
  }

  getStats(): UsageStats & { audioDuration: string; uptimeHours: number } {
    const uptimeMs = Date.now() - this.stats.startTime.getTime();

    return {
      ...this.stats,
      audioDuration: this.formatDuration(this.stats.audioSeconds),
      uptimeHours: uptimeMs / 3600000,
    };
  }

  private formatDuration(seconds: number): string {
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    return `${hours}h ${minutes}m`;
  }

  shouldAlert(): boolean {
    // Alert if rate limit hit rate exceeds 10%
    const hitRate = this.stats.rateLimitHits / this.stats.requestCount;
    return hitRate > 0.1 && this.stats.requestCount > 10;
  }
}
```

### Python Rate Limiter
```python
# lib/rate_limiter.py
import asyncio
import time
from collections import deque
from typing import Callable, TypeVar

T = TypeVar('T')

class RateLimiter:
    def __init__(
        self,
        max_concurrent: int = 50,
        max_per_minute: int = 500
    ):
        self.max_concurrent = max_concurrent
        self.max_per_minute = max_per_minute
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.request_times: deque = deque()

    async def execute(self, fn: Callable[[], T]) -> T:
        await self._wait_for_rate_limit()

        async with self.semaphore:
            self.request_times.append(time.time())
            return await fn()

    async def _wait_for_rate_limit(self):
        now = time.time()

        # Remove requests older than 1 minute
        while self.request_times and now - self.request_times[0] > 60:
            self.request_times.popleft()

        # Wait if at limit
        if len(self.request_times) >= self.max_per_minute:
            wait_time = 60 - (now - self.request_times[0])
            if wait_time > 0:
                await asyncio.sleep(wait_time)
```