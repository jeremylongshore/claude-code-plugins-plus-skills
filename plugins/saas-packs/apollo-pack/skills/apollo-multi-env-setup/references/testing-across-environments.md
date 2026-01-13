# Testing Across Environments

## Testing Across Environments

```typescript
// tests/integration/env-tests.ts
describe('Environment Configuration', () => {
  const originalEnv = process.env.NODE_ENV;

  afterEach(() => {
    process.env.NODE_ENV = originalEnv;
  });

  it('loads development config correctly', () => {
    process.env.NODE_ENV = 'development';
    const config = getConfig();
    expect(config.rateLimit).toBe(10);
    expect(config.features.sequences).toBe(false);
  });

  it('loads staging config correctly', () => {
    process.env.NODE_ENV = 'staging';
    const config = getConfig();
    expect(config.rateLimit).toBe(50);
    expect(config.features.sequences).toBe(true);
  });

  it('loads production config correctly', () => {
    process.env.NODE_ENV = 'production';
    const config = getConfig();
    expect(config.rateLimit).toBe(90);
    expect(config.logging.redactPII).toBe(true);
  });

  it('throws on missing API key', () => {
    process.env.NODE_ENV = 'production';
    delete process.env.APOLLO_API_KEY;
    expect(() => validateEnvironment()).toThrow();
  });
});
```