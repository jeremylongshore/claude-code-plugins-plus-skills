# Key Components

## Key Components

### Step 1: Client Wrapper
```typescript
// src/coderabbit/client.ts
export class CodeRabbitService {
  private client: CodeRabbitClient;
  private cache: Cache;
  private monitor: Monitor;

  constructor(config: CodeRabbitConfig) {
    this.client = new CodeRabbitClient(config);
    this.cache = new Cache(config.cacheOptions);
    this.monitor = new Monitor('coderabbit');
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
// src/coderabbit/errors.ts
export class CodeRabbitServiceError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly retryable: boolean,
    public readonly originalError?: Error
  ) {
    super(message);
    this.name = 'CodeRabbitServiceError';
  }
}

export function wrapCodeRabbitError(error: unknown): CodeRabbitServiceError {
  // Transform SDK errors to application errors
}
```

### Step 3: Health Check
```typescript
// src/coderabbit/health.ts
export async function checkCodeRabbitHealth(): Promise<HealthStatus> {
  try {
    const start = Date.now();
    await coderabbitClient.ping();
    return {
      status: 'healthy',
      latencyMs: Date.now() - start,
    };
  } catch (error) {
    return { status: 'unhealthy', error: error.message };
  }
}
```