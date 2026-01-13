# Key Components

## Key Components

### Step 1: Client Wrapper
```typescript
// src/groq/client.ts
export class GroqService {
  private client: GroqClient;
  private cache: Cache;
  private monitor: Monitor;

  constructor(config: GroqConfig) {
    this.client = new GroqClient(config);
    this.cache = new Cache(config.cacheOptions);
    this.monitor = new Monitor('groq');
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
// src/groq/errors.ts
export class GroqServiceError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly retryable: boolean,
    public readonly originalError?: Error
  ) {
    super(message);
    this.name = 'GroqServiceError';
  }
}

export function wrapGroqError(error: unknown): GroqServiceError {
  // Transform SDK errors to application errors
}
```

### Step 3: Health Check
```typescript
// src/groq/health.ts
export async function checkGroqHealth(): Promise<HealthStatus> {
  try {
    const start = Date.now();
    await groqClient.ping();
    return {
      status: 'healthy',
      latencyMs: Date.now() - start,
    };
  } catch (error) {
    return { status: 'unhealthy', error: error.message };
  }
}
```