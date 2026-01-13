# Key Components

## Key Components

### Step 1: Client Wrapper
```typescript
// src/firecrawl/client.ts
export class FireCrawlService {
  private client: FireCrawlClient;
  private cache: Cache;
  private monitor: Monitor;

  constructor(config: FireCrawlConfig) {
    this.client = new FireCrawlClient(config);
    this.cache = new Cache(config.cacheOptions);
    this.monitor = new Monitor('firecrawl');
  }

  async get(id: string): Promise<Resource> {
    return this.cache.getOrFetch(id, () =>
      this.monitor.track('get', () => this.client.get(id))
    );
  }
}
```

### Step 2: Error Boundary
```typescript
// src/firecrawl/errors.ts
export class FireCrawlServiceError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly retryable: boolean,
    public readonly originalError?: Error
  ) {
    super(message);
    this.name = 'FireCrawlServiceError';
  }
}

export function wrapFireCrawlError(error: unknown): FireCrawlServiceError {
  // Transform SDK errors to application errors
}
```

### Step 3: Health Check
```typescript
// src/firecrawl/health.ts
export async function checkFireCrawlHealth(): Promise<HealthStatus> {
  try {
    const start = Date.now();
    await firecrawlClient.ping();
    return {
      status: 'healthy',
      latencyMs: Date.now() - start,
    };
  } catch (error) {
    return { status: 'unhealthy', error: error.message };
  }
}
```