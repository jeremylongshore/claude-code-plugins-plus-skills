# Examples

### Quick Performance Wrapper
```typescript
const withPerformance = <T>(name: string, fn: () => Promise<T>) =>
  measuredVast.aiCall(name, () =>
    cachedVast.aiRequest(`cache:${name}`, fn)
  );
```