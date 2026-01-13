# Circuit Breaker

## Circuit Breaker

```typescript
import CircuitBreaker from 'opossum';

const perplexityBreaker = new CircuitBreaker(
  async (operation: () => Promise<any>) => operation(),
  {
    timeout: 30000,
    errorThresholdPercentage: 50,
    resetTimeout: 30000,
    volumeThreshold: 10,
  }
);

// Events
perplexityBreaker.on('open', () => {
  console.warn('Perplexity circuit OPEN - requests failing fast');
  alertOps('Perplexity circuit breaker opened');
});

perplexityBreaker.on('halfOpen', () => {
  console.info('Perplexity circuit HALF-OPEN - testing recovery');
});

perplexityBreaker.on('close', () => {
  console.info('Perplexity circuit CLOSED - normal operation');
});

// Usage
async function safePerplexityCall<T>(fn: () => Promise<T>): Promise<T> {
  return perplexityBreaker.fire(fn);
}
```