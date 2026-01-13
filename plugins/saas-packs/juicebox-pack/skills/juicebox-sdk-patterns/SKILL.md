---
name: juicebox-sdk-patterns
description: |
  Apply production-ready Juicebox SDK patterns.
  Use when implementing robust error handling, retry logic,
  or enterprise-grade Juicebox integrations.
  Trigger with phrases like "juicebox best practices", "juicebox patterns",
  "production juicebox", "juicebox SDK architecture".
allowed-tools: Read, Write, Edit, Bash, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Juicebox SDK Patterns

## Overview
Production-ready patterns for robust Juicebox integration including error handling, retries, and caching.

## Prerequisites
- Juicebox SDK installed
- Understanding of async/await patterns
- Familiarity with dependency injection

## Instructions

### Step 1: Create Client Wrapper
```typescript
// lib/juicebox-client.ts
import { JuiceboxClient, JuiceboxError } from '@juicebox/sdk';

export class JuiceboxService {
  private client: JuiceboxClient;
  private cache: Map<string, { data: any; expires: number }>;

  constructor(apiKey: string) {
    this.client = new JuiceboxClient({
      apiKey,
      timeout: 30000,
      retries: 3
    });
    this.cache = new Map();
  }

  async searchPeople(query: string, options?: SearchOptions) {
    const cacheKey = `search:${query}:${JSON.stringify(options)}`;
    const cached = this.getFromCache(cacheKey);
    if (cached) return cached;

    try {
      const results = await this.client.search.people({
        query,
        ...options
      });
      this.setCache(cacheKey, results, 300000); // 5 min cache
      return results;
    } catch (error) {
      if (error instanceof JuiceboxError) {
        throw this.handleJuiceboxError(error);
      }
      throw error;
    }
  }

  private handleJuiceboxError(error: JuiceboxError) {
    switch (error.code) {
      case 'RATE_LIMITED':
        return new Error(`Rate limited. Retry after ${error.retryAfter}s`);
      case 'INVALID_QUERY':
        return new Error(`Invalid query: ${error.message}`);
      default:
        return error;
    }
  }
}
```

### Step 2: Implement Retry Logic
```typescript
// lib/retry.ts
export async function withRetry<T>(
  fn: () => Promise<T>,
  options: { maxRetries: number; backoff: number }
): Promise<T> {
  let lastError: Error;

  for (let i = 0; i < options.maxRetries; i++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error as Error;
      await sleep(options.backoff * Math.pow(2, i));
    }
  }

  throw lastError!;
}
```

### Step 3: Add Observability
```typescript
// lib/instrumented-client.ts
export class InstrumentedJuiceboxService extends JuiceboxService {
  async searchPeople(query: string, options?: SearchOptions) {
    const start = Date.now();
    const span = tracer.startSpan('juicebox.search');

    try {
      const results = await super.searchPeople(query, options);
      span.setStatus({ code: SpanStatusCode.OK });
      metrics.histogram('juicebox.search.duration', Date.now() - start);
      return results;
    } catch (error) {
      span.setStatus({ code: SpanStatusCode.ERROR });
      metrics.increment('juicebox.search.errors');
      throw error;
    } finally {
      span.end();
    }
  }
}
```

## Output
- Production-ready client wrapper
- Retry logic with exponential backoff
- Caching layer for performance
- Observability instrumentation

## Error Handling
| Pattern | Use Case | Benefit |
|---------|----------|---------|
| Circuit Breaker | Prevent cascade failures | System resilience |
| Retry with Backoff | Transient errors | Higher success rate |
| Cache-Aside | Repeated queries | Lower latency |
| Bulkhead | Resource isolation | Fault isolation |

## Examples

### Singleton Pattern
```typescript
// Ensure single client instance
let instance: JuiceboxService | null = null;

export function getJuiceboxService(): JuiceboxService {
  if (!instance) {
    instance = new JuiceboxService(process.env.JUICEBOX_API_KEY!);
  }
  return instance;
}
```

## Resources
- [SDK Best Practices](https://juicebox.ai/docs/best-practices)
- [Error Handling Guide](https://juicebox.ai/docs/errors)

## Next Steps
Apply these patterns then explore `juicebox-core-workflow-a` for search workflows.
