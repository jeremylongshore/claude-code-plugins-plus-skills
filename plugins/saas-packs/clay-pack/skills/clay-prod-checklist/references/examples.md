# Examples

### Health Check Implementation
```typescript
async function healthCheck(): Promise<{ status: string; clay: any }> {
  const start = Date.now();
  try {
    await clayClient.ping();
    return { status: 'healthy', clay: { connected: true, latencyMs: Date.now() - start } };
  } catch (error) {
    return { status: 'degraded', clay: { connected: false, latencyMs: Date.now() - start } };
  }
}
```

### Immediate Rollback
```bash
kubectl rollout undo deployment/clay-integration
kubectl rollout status deployment/clay-integration
```