# Circuit Breaker

## Circuit Breaker

```typescript
import CircuitBreaker from 'opossum';

const firecrawlBreaker = new CircuitBreaker(
  async (operation: () => Promise<any>) => operation(),
  {
    timeout: 30000,
    errorThresholdPercentage: 50,
    resetTimeout: 30000,
    volumeThreshold: 10,
  }
);

// Events
firecrawlBreaker.on('open', () => {
  console.warn('FireCrawl circuit OPEN - requests failing fast');
  alertOps('FireCrawl circuit breaker opened');
});

firecrawlBreaker.on('halfOpen', () => {
  console.info('FireCrawl circuit HALF-OPEN - testing recovery');
});

firecrawlBreaker.on('close', () => {
  console.info('FireCrawl circuit CLOSED - normal operation');
});

// Usage
async function safeFireCrawlCall<T>(fn: () => Promise<T>): Promise<T> {
  return firecrawlBreaker.fire(fn);
}
```