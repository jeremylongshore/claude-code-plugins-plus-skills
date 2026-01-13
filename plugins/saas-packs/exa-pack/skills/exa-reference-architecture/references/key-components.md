# Key Components

## Key Components

### Step 1: Client Wrapper
```typescript
// src/exa/client.ts
export class ExaService {
  private client: ExaClient;
  private cache: Cache;
  private monitor: Monitor;

  constructor(config: ExaConfig) {
    this.client = new ExaClient(config);
    this.cache = new Cache(config.cacheOptions);
    this.monitor = new Monitor('exa');
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
// src/exa/errors.ts
export class ExaServiceError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly retryable: boolean,
    public readonly originalError?: Error
  ) {
    super(message);
    this.name = 'ExaServiceError';
  }
}

export function wrapExaError(error: unknown): ExaServiceError {
  // Transform SDK errors to application errors
}
```

### Step 3: Health Check
```typescript
// src/exa/health.ts
export async function checkExaHealth(): Promise<HealthStatus> {
  try {
    const start = Date.now();
    await exaClient.ping();
    return {
      status: 'healthy',
      latencyMs: Date.now() - start,
    };
  } catch (error) {
    return { status: 'unhealthy', error: error.message };
  }
}
```