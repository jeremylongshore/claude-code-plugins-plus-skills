# Key Components

## Key Components

### Step 1: Client Wrapper
```typescript
// src/instantly/client.ts
export class InstantlyService {
  private client: InstantlyClient;
  private cache: Cache;
  private monitor: Monitor;

  constructor(config: InstantlyConfig) {
    this.client = new InstantlyClient(config);
    this.cache = new Cache(config.cacheOptions);
    this.monitor = new Monitor('instantly');
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
// src/instantly/errors.ts
export class InstantlyServiceError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly retryable: boolean,
    public readonly originalError?: Error
  ) {
    super(message);
    this.name = 'InstantlyServiceError';
  }
}

export function wrapInstantlyError(error: unknown): InstantlyServiceError {
  // Transform SDK errors to application errors
}
```

### Step 3: Health Check
```typescript
// src/instantly/health.ts
export async function checkInstantlyHealth(): Promise<HealthStatus> {
  try {
    const start = Date.now();
    await instantlyClient.ping();
    return {
      status: 'healthy',
      latencyMs: Date.now() - start,
    };
  } catch (error) {
    return { status: 'unhealthy', error: error.message };
  }
}
```