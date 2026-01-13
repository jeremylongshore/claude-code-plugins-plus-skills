# Examples

### Quick Performance Wrapper
```typescript
const withPerformance = <T>(name: string, fn: () => Promise<T>) =>
  measuredGroqCall(name, () =>
    cachedGroqRequest(`cache:${name}`, fn)
  );
```