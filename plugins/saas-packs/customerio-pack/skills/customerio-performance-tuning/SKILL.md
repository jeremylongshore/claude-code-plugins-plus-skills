---
name: customerio-performance-tuning
description: |
  Optimize Customer.io API performance.
  Use when improving response times, reducing latency,
  or optimizing high-volume integrations.
  Trigger with phrases like "customer.io performance", "optimize customer.io",
  "customer.io latency", "customer.io speed".
allowed-tools: Read, Write, Edit, Bash
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Customer.io Performance Tuning

## Overview
Optimize Customer.io API performance for high-volume and low-latency integrations.

## Prerequisites
- Customer.io integration working
- Monitoring infrastructure
- Understanding of your traffic patterns

## Instructions

### Step 1: Connection Pooling
```typescript
// lib/customerio-pooled.ts
import { TrackClient, RegionUS } from '@customerio/track';
import { Agent } from 'http';
import { Agent as HttpsAgent } from 'https';

// Create connection pool with keep-alive
const httpsAgent = new HttpsAgent({
  keepAlive: true,
  keepAliveMsecs: 30000,
  maxSockets: 100,
  maxFreeSockets: 20,
  timeout: 30000
});

// Create client with connection pooling
export function createPooledClient(): TrackClient {
  return new TrackClient(
    process.env.CUSTOMERIO_SITE_ID!,
    process.env.CUSTOMERIO_API_KEY!,
    {
      region: RegionUS,
      // Pass custom agent for connection pooling
      httpAgent: httpsAgent
    }
  );
}

// Singleton for connection reuse
let clientInstance: TrackClient | null = null;

export function getClient(): TrackClient {
  if (!clientInstance) {
    clientInstance = createPooledClient();
  }
  return clientInstance;
}
```

### Step 2: Batch Processing
```typescript
// lib/batch-processor.ts
import { TrackClient } from '@customerio/track';

interface BatchItem {
  type: 'identify' | 'track';
  userId: string;
  data: Record<string, any>;
}

export class BatchProcessor {
  private batch: BatchItem[] = [];
  private batchSize: number;
  private flushInterval: number;
  private timer: NodeJS.Timer | null = null;

  constructor(
    private client: TrackClient,
    options: { batchSize?: number; flushIntervalMs?: number } = {}
  ) {
    this.batchSize = options.batchSize || 100;
    this.flushInterval = options.flushIntervalMs || 1000;
    this.startFlushTimer();
  }

  add(item: BatchItem): void {
    this.batch.push(item);

    if (this.batch.length >= this.batchSize) {
      this.flush();
    }
  }

  async flush(): Promise<void> {
    if (this.batch.length === 0) return;

    const items = this.batch.splice(0, this.batchSize);

    // Process in parallel with concurrency limit
    const concurrency = 10;
    for (let i = 0; i < items.length; i += concurrency) {
      const chunk = items.slice(i, i + concurrency);
      await Promise.all(chunk.map(item => this.processItem(item)));
    }
  }

  private async processItem(item: BatchItem): Promise<void> {
    try {
      if (item.type === 'identify') {
        await this.client.identify(item.userId, item.data);
      } else {
        await this.client.track(item.userId, {
          name: item.data.event,
          data: item.data.properties
        });
      }
    } catch (error) {
      console.error(`Failed to process ${item.type} for ${item.userId}:`, error);
    }
  }

  private startFlushTimer(): void {
    this.timer = setInterval(() => this.flush(), this.flushInterval);
  }

  async shutdown(): Promise<void> {
    if (this.timer) {
      clearInterval(this.timer);
    }
    await this.flush();
  }
}
```

### Step 3: Async Fire-and-Forget
```typescript
// lib/async-tracker.ts
import { TrackClient } from '@customerio/track';

class AsyncTracker {
  private queue: Array<() => Promise<void>> = [];
  private processing = false;
  private concurrency = 5;

  constructor(private client: TrackClient) {}

  // Non-blocking identify
  identifyAsync(userId: string, attributes: Record<string, any>): void {
    this.enqueue(() => this.client.identify(userId, attributes));
  }

  // Non-blocking track
  trackAsync(userId: string, event: string, data?: Record<string, any>): void {
    this.enqueue(() => this.client.track(userId, { name: event, data }));
  }

  private enqueue(operation: () => Promise<void>): void {
    this.queue.push(operation);
    this.processQueue();
  }

  private async processQueue(): Promise<void> {
    if (this.processing) return;
    this.processing = true;

    while (this.queue.length > 0) {
      const batch = this.queue.splice(0, this.concurrency);
      await Promise.allSettled(batch.map(op => op()));
    }

    this.processing = false;
  }
}

export const asyncTracker = new AsyncTracker(getClient());
```

### Step 4: Caching for Deduplication
```typescript
// lib/dedup-cache.ts
import { LRUCache } from 'lru-cache';

interface CacheEntry {
  userId: string;
  attributes: Record<string, any>;
  timestamp: number;
}

const identifyCache = new LRUCache<string, CacheEntry>({
  max: 10000,
  ttl: 60000 // 1 minute
});

export function shouldIdentify(
  userId: string,
  attributes: Record<string, any>
): boolean {
  const cacheKey = `${userId}:${JSON.stringify(attributes)}`;
  const cached = identifyCache.get(cacheKey);

  if (cached) {
    // Skip if identical identify within TTL
    return false;
  }

  identifyCache.set(cacheKey, {
    userId,
    attributes,
    timestamp: Date.now()
  });

  return true;
}

// Track event deduplication
const eventCache = new LRUCache<string, number>({
  max: 50000,
  ttl: 5000 // 5 seconds
});

export function shouldTrack(
  userId: string,
  eventName: string,
  eventId?: string
): boolean {
  const cacheKey = eventId || `${userId}:${eventName}:${Date.now()}`;

  if (eventCache.has(cacheKey)) {
    return false;
  }

  eventCache.set(cacheKey, Date.now());
  return true;
}
```

### Step 5: Regional Optimization
```typescript
// lib/regional-client.ts
import { TrackClient, RegionUS, RegionEU } from '@customerio/track';

interface RegionalConfig {
  us: { siteId: string; apiKey: string };
  eu: { siteId: string; apiKey: string };
}

class RegionalCustomerIO {
  private clients: Map<string, TrackClient> = new Map();

  constructor(config: RegionalConfig) {
    this.clients.set('us', new TrackClient(
      config.us.siteId,
      config.us.apiKey,
      { region: RegionUS }
    ));

    this.clients.set('eu', new TrackClient(
      config.eu.siteId,
      config.eu.apiKey,
      { region: RegionEU }
    ));
  }

  private getClientForUser(userId: string, userRegion?: string): TrackClient {
    // Route to nearest region
    const region = userRegion || this.inferRegion(userId);
    return this.clients.get(region) || this.clients.get('us')!;
  }

  private inferRegion(userId: string): string {
    // Implement region inference logic
    // Could be based on user preferences, IP geolocation, etc.
    return 'us';
  }

  async identify(
    userId: string,
    attributes: Record<string, any>,
    region?: string
  ): Promise<void> {
    const client = this.getClientForUser(userId, region);
    await client.identify(userId, attributes);
  }
}
```

### Step 6: Performance Monitoring
```typescript
// lib/performance-monitor.ts
import { metrics } from './metrics';

function wrapWithTiming<T>(
  name: string,
  operation: () => Promise<T>
): Promise<T> {
  const start = Date.now();

  return operation()
    .then(result => {
      metrics.histogram(`customerio.${name}.latency`, Date.now() - start);
      metrics.increment(`customerio.${name}.success`);
      return result;
    })
    .catch(error => {
      metrics.histogram(`customerio.${name}.latency`, Date.now() - start);
      metrics.increment(`customerio.${name}.error`);
      throw error;
    });
}

// Usage
await wrapWithTiming('identify', () =>
  client.identify(userId, attributes)
);
```

## Performance Benchmarks

| Operation | Target Latency | Notes |
|-----------|---------------|-------|
| Identify | < 100ms | With connection pooling |
| Track Event | < 100ms | With connection pooling |
| Batch (100 items) | < 500ms | Parallel processing |
| Webhook Processing | < 50ms | Excluding downstream ops |

## Optimization Checklist

- [ ] Connection pooling enabled
- [ ] Batch processing for bulk operations
- [ ] Async fire-and-forget for non-critical events
- [ ] Deduplication cache implemented
- [ ] Regional routing configured
- [ ] Performance monitoring in place

## Error Handling
| Issue | Solution |
|-------|----------|
| High latency | Enable connection pooling |
| Timeout errors | Reduce payload size, increase timeout |
| Memory pressure | Limit cache and queue sizes |

## Resources
- [API Performance Tips](https://customer.io/docs/api/track/#section/Rate-limits)
- [Best Practices](https://customer.io/docs/best-practices/)

## Next Steps
After performance tuning, proceed to `customerio-cost-tuning` for cost optimization.
