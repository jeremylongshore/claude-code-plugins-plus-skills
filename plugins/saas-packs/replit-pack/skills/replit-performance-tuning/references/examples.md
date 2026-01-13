# Examples

### Quick Performance Wrapper
```typescript
const withPerformance = <T>(name: string, fn: () => Promise<T>) =>
  measuredReplitCall(name, () =>
    cachedReplitRequest(`cache:${name}`, fn)
  );
```