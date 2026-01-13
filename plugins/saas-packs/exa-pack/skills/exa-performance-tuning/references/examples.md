# Examples

### Quick Performance Wrapper
```typescript
const withPerformance = <T>(name: string, fn: () => Promise<T>) =>
  measuredExaCall(name, () =>
    cachedExaRequest(`cache:${name}`, fn)
  );
```