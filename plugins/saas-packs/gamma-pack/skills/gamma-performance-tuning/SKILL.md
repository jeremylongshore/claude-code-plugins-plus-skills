---
name: gamma-performance-tuning
license: MIT
allowed-tools: Read, Write, Edit
description: Optimize Gamma API performance and reduce latency. Use when experiencing
  slow response times, optimizing throughput, or improving user experience with Gamma
  integrations. Trigger with phrases like "gamma performance", "gamma slow", "gamma
  latency"...
---
# Gamma Performance Tuning

## Overview
Optimize Gamma API integration performance for faster response times and better throughput.

## Prerequisites
- Working Gamma integration
- Performance monitoring tools
- Understanding of caching concepts

## Instructions

### Step 1: Client Configuration Optimization
```typescript
import { GammaClient } from '@gamma/sdk';

const gamma = new GammaClient({
  apiKey: process.env.GAMMA_API_KEY,

  // Connection optimization
  timeout: 30000,
  keepAlive: true,
  maxSockets: 10,

  // Retry configuration
  retries: 3,
  retryDelay: 1000,
  retryCondition: (err) => err.status >= 500 || err.status === 429,

  // Compression
  compression: true,
});
```

### Step 2: Response Caching
```typescript
import NodeCache from 'node-cache';

const cache = new NodeCache({
  stdTTL: 300, // 5 minutes default
  checkperiod: 60,
});

async function getCachedPresentation(id: string) {
  const cacheKey = `presentation:${id}`;

  // Check cache first
  const cached = cache.get(cacheKey);
  if (cached) {
    return cached;
  }

  // Fetch from API
  const presentation = await gamma.presentations.get(id);

  // Cache the result
  cache.set(cacheKey, presentation);

  return presentation;
}

// Cache invalidation on updates
gamma.on('presentation.updated', (event) => {
  cache.del(`presentation:${event.data.id}`);
});
```

### Step 3: Parallel Request Optimization
```typescript
// Instead of sequential requests
async function getSequential(ids: string[]) {
  const results = [];
  for (const id of ids) {
    results.push(await gamma.presentations.get(id)); // Slow!
  }
  return results;
}

// Use parallel requests with concurrency control
import pLimit from 'p-limit';

const limit = pLimit(5); // Max 5 concurrent requests

async function getParallel(ids: string[]) {
  return Promise.all(
    ids.map(id => limit(() => gamma.presentations.get(id)))
  );
}

// Batch API if available
async function getBatch(ids: string[]) {
  return gamma.presentations.getBatch(ids); // Single request for multiple items
}
```

### Step 4: Lazy Loading and Pagination
```typescript
// Pagination for large lists
async function* getAllPresentations() {
  let cursor: string | undefined;

  do {
    const page = await gamma.presentations.list({
      limit: 100,
      cursor,
    });

    for (const presentation of page.items) {
      yield presentation;
    }

    cursor = page.nextCursor;
  } while (cursor);
}

// Usage
for await (const presentation of getAllPresentations()) {
  // Process one at a time, memory efficient
}
```

### Step 5: Request Optimization
```typescript
// Only request needed fields
const presentation = await gamma.presentations.get(id, {
  fields: ['id', 'title', 'url', 'updatedAt'], // Skip large fields
});

// Avoid redundant API calls
const createOptions = {
  title: 'My Presentation',
  prompt: 'AI content',
  returnImmediately: true, // Don't wait for generation
};

const { id, statusUrl } = await gamma.presentations.create(createOptions);

// Poll status separately if needed
const status = await gamma.presentations.status(id);
```

### Step 6: Connection Pooling
```typescript
import http from 'http';
import https from 'https';

// Reuse connections
const httpAgent = new http.Agent({
  keepAlive: true,
  maxSockets: 25,
  maxFreeSockets: 10,
  timeout: 60000,
});

const httpsAgent = new https.Agent({
  keepAlive: true,
  maxSockets: 25,
  maxFreeSockets: 10,
  timeout: 60000,
});

const gamma = new GammaClient({
  apiKey: process.env.GAMMA_API_KEY,
  httpAgent,
  httpsAgent,
});
```

## Performance Metrics

### Monitoring Setup
```typescript
import { performance } from 'perf_hooks';

async function timedRequest<T>(name: string, fn: () => Promise<T>): Promise<T> {
  const start = performance.now();

  try {
    const result = await fn();
    const duration = performance.now() - start;

    console.log(`[PERF] ${name}: ${duration.toFixed(2)}ms`);
    metrics.recordLatency(name, duration);

    return result;
  } catch (err) {
    const duration = performance.now() - start;
    console.log(`[PERF] ${name} FAILED: ${duration.toFixed(2)}ms`);
    throw err;
  }
}

// Usage
const presentation = await timedRequest('gamma.get', () =>
  gamma.presentations.get(id)
);
```

## Performance Targets

| Operation | Target | Action if Exceeded |
|-----------|--------|-------------------|
| Simple GET | < 200ms | Check network, use caching |
| List (100 items) | < 500ms | Reduce page size |
| Create presentation | < 5s | Use async pattern |
| Export PDF | < 30s | Use webhook notification |

## Resources
- [Gamma Performance Guide](https://gamma.app/docs/performance)
- [Node.js Performance](https://nodejs.org/en/docs/guides/dont-block-the-event-loop)

## Next Steps
Proceed to `gamma-cost-tuning` for cost optimization.
