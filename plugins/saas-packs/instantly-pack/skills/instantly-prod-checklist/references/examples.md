# Examples

### Health Check Implementation
```typescript
async function healthCheck(): Promise<{ status: string; instantly: any }> {
  const start = Date.now();
  try {
    await instantlyClient.ping();
    return { status: 'healthy', instantly: { connected: true, latencyMs: Date.now() - start } };
  } catch (error) {
    return { status: 'degraded', instantly: { connected: false, latencyMs: Date.now() - start } };
  }
}
```

### Immediate Rollback
```bash
kubectl rollout undo deployment/instantly-integration
kubectl rollout status deployment/instantly-integration
```