# Circuit Breaker

## Circuit Breaker

```typescript
import CircuitBreaker from 'opossum';

const replitBreaker = new CircuitBreaker(
  async (operation: () => Promise<any>) => operation(),
  {
    timeout: 30000,
    errorThresholdPercentage: 50,
    resetTimeout: 30000,
    volumeThreshold: 10,
  }
);

// Events
replitBreaker.on('open', () => {
  console.warn('Replit circuit OPEN - requests failing fast');
  alertOps('Replit circuit breaker opened');
});

replitBreaker.on('halfOpen', () => {
  console.info('Replit circuit HALF-OPEN - testing recovery');
});

replitBreaker.on('close', () => {
  console.info('Replit circuit CLOSED - normal operation');
});

// Usage
async function safeReplitCall<T>(fn: () => Promise<T>): Promise<T> {
  return replitBreaker.fire(fn);
}
```