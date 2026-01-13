# Key Components

## Key Components

### Step 1: Client Wrapper
```typescript
// src/fireflies/client.ts
export class Fireflies.aiService {
  private client: Fireflies.aiClient;
  private cache: Cache;
  private monitor: Monitor;

  constructor(config: Fireflies.aiConfig) {
    this.client = new Fireflies.aiClient(config);
    this.cache = new Cache(config.cacheOptions);
    this.monitor = new Monitor('fireflies');
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
// src/fireflies/errors.ts
export class Fireflies.aiServiceError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly retryable: boolean,
    public readonly originalError?: Error
  ) {
    super(message);
    this.name = 'Fireflies.aiServiceError';
  }
}

export function wrapFireflies.aiError(error: unknown): Fireflies.aiServiceError {
  // Transform SDK errors to application errors
}
```

### Step 3: Health Check
```typescript
// src/fireflies/health.ts
export async function checkFireflies.aiHealth(): Promise<HealthStatus> {
  try {
    const start = Date.now();
    await firefliesClient.ping();
    return {
      status: 'healthy',
      latencyMs: Date.now() - start,
    };
  } catch (error) {
    return { status: 'unhealthy', error: error.message };
  }
}
```