# Examples

### Quick Performance Wrapper
```typescript
const withPerformance = <T>(name: string, fn: () => Promise<T>) =>
  measuredClayCall(name, () =>
    cachedClayRequest(`cache:${name}`, fn)
  );
```