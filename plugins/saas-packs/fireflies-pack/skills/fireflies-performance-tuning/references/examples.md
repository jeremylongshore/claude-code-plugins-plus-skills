# Examples

### Quick Performance Wrapper
```typescript
const withPerformance = <T>(name: string, fn: () => Promise<T>) =>
  measuredFireflies.aiCall(name, () =>
    cachedFireflies.aiRequest(`cache:${name}`, fn)
  );
```