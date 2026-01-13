# Examples

### Quick Performance Wrapper
```typescript
const withPerformance = <T>(name: string, fn: () => Promise<T>) =>
  measuredPerplexityCall(name, () =>
    cachedPerplexityRequest(`cache:${name}`, fn)
  );
```