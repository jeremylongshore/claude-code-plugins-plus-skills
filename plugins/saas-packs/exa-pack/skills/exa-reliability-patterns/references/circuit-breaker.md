# Circuit Breaker

## Circuit Breaker

```typescript
import CircuitBreaker from 'opossum';

const exaBreaker = new CircuitBreaker(
  async (operation: () => Promise<any>) => operation(),
  {
    timeout: 30000,
    errorThresholdPercentage: 50,
    resetTimeout: 30000,
    volumeThreshold: 10,
  }
);

// Events
exaBreaker.on('open', () => {
  console.warn('Exa circuit OPEN - requests failing fast');
  alertOps('Exa circuit breaker opened');
});

exaBreaker.on('halfOpen', () => {
  console.info('Exa circuit HALF-OPEN - testing recovery');
});

exaBreaker.on('close', () => {
  console.info('Exa circuit CLOSED - normal operation');
});

// Usage
async function safeExaCall<T>(fn: () => Promise<T>): Promise<T> {
  return exaBreaker.fire(fn);
}
```