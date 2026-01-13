# Examples

### Quick Performance Wrapper
```typescript
const withPerformance = <T>(name: string, fn: () => Promise<T>) =>
  measuredWindsurfCall(name, () =>
    cachedWindsurfRequest(`cache:${name}`, fn)
  );
```