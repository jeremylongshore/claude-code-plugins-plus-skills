# Key Components

## Key Components

### Step 1: Client Wrapper
```typescript
// src/ideogram/client.ts
export class IdeogramService {
  private client: IdeogramClient;
  private cache: Cache;
  private monitor: Monitor;

  constructor(config: IdeogramConfig) {
    this.client = new IdeogramClient(config);
    this.cache = new Cache(config.cacheOptions);
    this.monitor = new Monitor('ideogram');
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
// src/ideogram/errors.ts
export class IdeogramServiceError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly retryable: boolean,
    public readonly originalError?: Error
  ) {
    super(message);
    this.name = 'IdeogramServiceError';
  }
}

export function wrapIdeogramError(error: unknown): IdeogramServiceError {
  // Transform SDK errors to application errors
}
```

### Step 3: Health Check
```typescript
// src/ideogram/health.ts
export async function checkIdeogramHealth(): Promise<HealthStatus> {
  try {
    const start = Date.now();
    await ideogramClient.ping();
    return {
      status: 'healthy',
      latencyMs: Date.now() - start,
    };
  } catch (error) {
    return { status: 'unhealthy', error: error.message };
  }
}
```