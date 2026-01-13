# Implementation

## Implementation

### Service Layer Example
```typescript
// services/presentation-service.ts
import { GammaClient } from '@gamma/sdk';
import { Cache } from './cache';
import { Queue } from './queue';

export class PresentationService {
  private gamma: GammaClient;
  private cache: Cache;
  private queue: Queue;

  constructor() {
    this.gamma = new GammaClient({
      apiKey: process.env.GAMMA_API_KEY,
    });
    this.cache = new Cache({ ttl: 300 });
    this.queue = new Queue('presentations');
  }

  async create(userId: string, options: CreateOptions) {
    // Add to queue for async processing
    const job = await this.queue.add({
      type: 'create',
      userId,
      options,
    });

    return { jobId: job.id, status: 'queued' };
  }

  async get(id: string) {
    return this.cache.getOrFetch(
      `presentation:${id}`,
      () => this.gamma.presentations.get(id)
    );
  }

  async list(userId: string, options: ListOptions) {
    return this.gamma.presentations.list({
      filter: { userId },
      ...options,
    });
  }
}
```

### Event Handler Example
```typescript
// workers/gamma-worker.ts
import { Worker } from 'bullmq';
import { GammaClient } from '@gamma/sdk';

const gamma = new GammaClient({ apiKey: process.env.GAMMA_API_KEY });

const worker = new Worker('presentations', async (job) => {
  switch (job.data.type) {
    case 'create':
      const presentation = await gamma.presentations.create(job.data.options);
      await notifyUser(job.data.userId, 'created', presentation);
      return presentation;

    case 'export':
      const exportResult = await gamma.exports.create(
        job.data.presentationId,
        job.data.format
      );
      await notifyUser(job.data.userId, 'exported', exportResult);
      return exportResult;

    default:
      throw new Error(`Unknown job type: ${job.data.type}`);
  }
});
```