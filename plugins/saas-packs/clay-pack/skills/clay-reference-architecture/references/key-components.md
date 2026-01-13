# Key Components

## Key Components

### Step 1: Client Wrapper
```typescript
// src/clay/client.ts
export class ClayService {
  private client: ClayClient;
  private cache: Cache;
  private monitor: Monitor;

  constructor(config: ClayConfig) {
    this.client = new ClayClient(config);
    this.cache = new Cache(config.cacheOptions);
    this.monitor = new Monitor('clay');
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
// src/clay/errors.ts
export class ClayServiceError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly retryable: boolean,
    public readonly originalError?: Error
  ) {
    super(message);
    this.name = 'ClayServiceError';
  }
}

export function wrapClayError(error: unknown): ClayServiceError {
  // Transform SDK errors to application errors
}
```

### Step 3: Health Check
```typescript
// src/clay/health.ts
export async function checkClayHealth(): Promise<HealthStatus> {
  try {
    const start = Date.now();
    await clayClient.ping();
    return {
      status: 'healthy',
      latencyMs: Date.now() - start,
    };
  } catch (error) {
    return { status: 'unhealthy', error: error.message };
  }
}
```