# Examples

### Quick Performance Wrapper
```typescript
const withPerformance = <T>(name: string, fn: () => Promise<T>) =>
  measuredFireCrawlCall(name, () =>
    cachedFireCrawlRequest(`cache:${name}`, fn)
  );
```