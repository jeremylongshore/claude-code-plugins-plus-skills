# Key Components

## Key Components

### Step 1: Client Wrapper
```typescript
// src/vastai/client.ts
export class Vast.aiService {
  private client: Vast.aiClient;
  private cache: Cache;
  private monitor: Monitor;

  constructor(config: Vast.aiConfig) {
    this.client = new Vast.aiClient(config);
    this.cache = new Cache(config.cacheOptions);
    this.monitor = new Monitor('vastai');
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
// src/vastai/errors.ts
export class Vast.aiServiceError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly retryable: boolean,
    public readonly originalError?: Error
  ) {
    super(message);
    this.name = 'Vast.aiServiceError';
  }
}

export function wrapVast.aiError(error: unknown): Vast.aiServiceError {
  // Transform SDK errors to application errors
}
```

### Step 3: Health Check
```typescript
// src/vastai/health.ts
export async function checkVast.aiHealth(): Promise<HealthStatus> {
  try {
    const start = Date.now();
    await vastaiClient.ping();
    return {
      status: 'healthy',
      latencyMs: Date.now() - start,
    };
  } catch (error) {
    return { status: 'unhealthy', error: error.message };
  }
}
```