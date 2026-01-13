# Examples

### Quick Performance Wrapper
```typescript
const withPerformance = <T>(name: string, fn: () => Promise<T>) =>
  measuredCodeRabbitCall(name, () =>
    cachedCodeRabbitRequest(`cache:${name}`, fn)
  );
```