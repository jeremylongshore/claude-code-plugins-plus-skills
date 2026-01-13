# Pattern 4: Request Batching

## Pattern 4: Request Batching

```typescript
// src/lib/apollo/batch.ts
class ApolloBatcher {
  private queue: Array<{ domain: string; resolve: Function; reject: Function }> = [];
  private timeout: NodeJS.Timeout | null = null;
  private readonly batchSize = 10;
  private readonly batchDelay = 100;

  async enrichCompany(domain: string): Promise<Organization> {
    return new Promise((resolve, reject) => {
      this.queue.push({ domain, resolve, reject });
      this.scheduleBatch();
    });
  }

  private scheduleBatch() {
    if (this.timeout) return;

    this.timeout = setTimeout(async () => {
      this.timeout = null;
      const batch = this.queue.splice(0, this.batchSize);

      try {
        // Apollo doesn't have batch endpoint, process sequentially with rate limiting
        for (const item of batch) {
          try {
            const result = await apollo.enrichOrganization(item.domain);
            item.resolve(result);
          } catch (error) {
            item.reject(error);
          }
          await new Promise((r) => setTimeout(r, 50)); // Rate limit spacing
        }
      } catch (error) {
        batch.forEach((item) => item.reject(error));
      }

      if (this.queue.length > 0) {
        this.scheduleBatch();
      }
    }, this.batchDelay);
  }
}

export const apolloBatcher = new ApolloBatcher();
```