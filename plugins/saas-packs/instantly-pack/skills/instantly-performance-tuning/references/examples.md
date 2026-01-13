# Examples

### Quick Performance Wrapper
```typescript
const withPerformance = <T>(name: string, fn: () => Promise<T>) =>
  measuredInstantlyCall(name, () =>
    cachedInstantlyRequest(`cache:${name}`, fn)
  );
```