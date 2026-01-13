# Examples

### Health Check Implementation
```typescript
async function healthCheck(): Promise<{ status: string; fireflies: any }> {
  const start = Date.now();
  try {
    await firefliesClient.ping();
    return { status: 'healthy', fireflies: { connected: true, latencyMs: Date.now() - start } };
  } catch (error) {
    return { status: 'degraded', fireflies: { connected: false, latencyMs: Date.now() - start } };
  }
}
```

### Immediate Rollback
```bash
kubectl rollout undo deployment/fireflies-integration
kubectl rollout status deployment/fireflies-integration
```