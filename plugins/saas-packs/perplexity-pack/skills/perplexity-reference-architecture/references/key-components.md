# Key Components

## Key Components

### Step 1: Client Wrapper
```typescript
// src/perplexity/client.ts
export class PerplexityService {
  private client: PerplexityClient;
  private cache: Cache;
  private monitor: Monitor;

  constructor(config: PerplexityConfig) {
    this.client = new PerplexityClient(config);
    this.cache = new Cache(config.cacheOptions);
    this.monitor = new Monitor('perplexity');
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
// src/perplexity/errors.ts
export class PerplexityServiceError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly retryable: boolean,
    public readonly originalError?: Error
  ) {
    super(message);
    this.name = 'PerplexityServiceError';
  }
}

export function wrapPerplexityError(error: unknown): PerplexityServiceError {
  // Transform SDK errors to application errors
}
```

### Step 3: Health Check
```typescript
// src/perplexity/health.ts
export async function checkPerplexityHealth(): Promise<HealthStatus> {
  try {
    const start = Date.now();
    await perplexityClient.ping();
    return {
      status: 'healthy',
      latencyMs: Date.now() - start,
    };
  } catch (error) {
    return { status: 'unhealthy', error: error.message };
  }
}
```