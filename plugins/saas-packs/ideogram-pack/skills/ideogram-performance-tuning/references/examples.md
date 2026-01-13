# Examples

### Quick Performance Wrapper
```typescript
const withPerformance = <T>(name: string, fn: () => Promise<T>) =>
  measuredIdeogramCall(name, () =>
    cachedIdeogramRequest(`cache:${name}`, fn)
  );
```