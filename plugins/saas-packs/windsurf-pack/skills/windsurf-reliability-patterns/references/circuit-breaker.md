# Circuit Breaker

## Circuit Breaker

```typescript
import CircuitBreaker from 'opossum';

const windsurfBreaker = new CircuitBreaker(
  async (operation: () => Promise<any>) => operation(),
  {
    timeout: 30000,
    errorThresholdPercentage: 50,
    resetTimeout: 30000,
    volumeThreshold: 10,
  }
);

// Events
windsurfBreaker.on('open', () => {
  console.warn('Windsurf circuit OPEN - requests failing fast');
  alertOps('Windsurf circuit breaker opened');
});

windsurfBreaker.on('halfOpen', () => {
  console.info('Windsurf circuit HALF-OPEN - testing recovery');
});

windsurfBreaker.on('close', () => {
  console.info('Windsurf circuit CLOSED - normal operation');
});

// Usage
async function safeWindsurfCall<T>(fn: () => Promise<T>): Promise<T> {
  return windsurfBreaker.fire(fn);
}
```