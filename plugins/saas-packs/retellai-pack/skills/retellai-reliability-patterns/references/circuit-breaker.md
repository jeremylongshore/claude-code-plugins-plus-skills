# Circuit Breaker

## Circuit Breaker

```typescript
import CircuitBreaker from 'opossum';

const retellaiBreaker = new CircuitBreaker(
  async (operation: () => Promise<any>) => operation(),
  {
    timeout: 30000,
    errorThresholdPercentage: 50,
    resetTimeout: 30000,
    volumeThreshold: 10,
  }
);

// Events
retellaiBreaker.on('open', () => {
  console.warn('Retell AI circuit OPEN - requests failing fast');
  alertOps('Retell AI circuit breaker opened');
});

retellaiBreaker.on('halfOpen', () => {
  console.info('Retell AI circuit HALF-OPEN - testing recovery');
});

retellaiBreaker.on('close', () => {
  console.info('Retell AI circuit CLOSED - normal operation');
});

// Usage
async function safeRetell AICall<T>(fn: () => Promise<T>): Promise<T> {
  return retellaiBreaker.fire(fn);
}
```