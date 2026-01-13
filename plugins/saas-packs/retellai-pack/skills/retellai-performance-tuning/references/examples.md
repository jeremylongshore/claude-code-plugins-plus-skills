# Examples

### Quick Performance Wrapper
```typescript
const withPerformance = <T>(name: string, fn: () => Promise<T>) =>
  measuredRetell AICall(name, () =>
    cachedRetell AIRequest(`cache:${name}`, fn)
  );
```