# Examples

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