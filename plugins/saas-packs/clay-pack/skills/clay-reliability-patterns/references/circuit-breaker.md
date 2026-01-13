# Circuit Breaker

## Circuit Breaker

```typescript
import CircuitBreaker from 'opossum';

const clayBreaker = new CircuitBreaker(
  async (operation: () => Promise<any>) => operation(),
  {
    timeout: 30000,
    errorThresholdPercentage: 50,
    resetTimeout: 30000,
    volumeThreshold: 10,
  }
);

// Events
clayBreaker.on('open', () => {
  console.warn('Clay circuit OPEN - requests failing fast');
  alertOps('Clay circuit breaker opened');
});

clayBreaker.on('halfOpen', () => {
  console.info('Clay circuit HALF-OPEN - testing recovery');
});

clayBreaker.on('close', () => {
  console.info('Clay circuit CLOSED - normal operation');
});

// Usage
async function safeClayCall<T>(fn: () => Promise<T>): Promise<T> {
  return clayBreaker.fire(fn);
}
```