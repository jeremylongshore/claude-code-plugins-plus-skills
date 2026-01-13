# Key Components

## Key Components

### Step 1: Client Wrapper
```typescript
// src/windsurf/client.ts
export class WindsurfService {
  private client: WindsurfClient;
  private cache: Cache;
  private monitor: Monitor;

  constructor(config: WindsurfConfig) {
    this.client = new WindsurfClient(config);
    this.cache = new Cache(config.cacheOptions);
    this.monitor = new Monitor('windsurf');
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
// src/windsurf/errors.ts
export class WindsurfServiceError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly retryable: boolean,
    public readonly originalError?: Error
  ) {
    super(message);
    this.name = 'WindsurfServiceError';
  }
}

export function wrapWindsurfError(error: unknown): WindsurfServiceError {
  // Transform SDK errors to application errors
}
```

### Step 3: Health Check
```typescript
// src/windsurf/health.ts
export async function checkWindsurfHealth(): Promise<HealthStatus> {
  try {
    const start = Date.now();
    await windsurfClient.ping();
    return {
      status: 'healthy',
      latencyMs: Date.now() - start,
    };
  } catch (error) {
    return { status: 'unhealthy', error: error.message };
  }
}
```