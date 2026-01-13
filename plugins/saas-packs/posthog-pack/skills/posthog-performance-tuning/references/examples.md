# Examples

### Quick Performance Wrapper
```typescript
const withPerformance = <T>(name: string, fn: () => Promise<T>) =>
  measuredPostHogCall(name, () =>
    cachedPostHogRequest(`cache:${name}`, fn)
  );
```