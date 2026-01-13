# Examples

### Health Check Implementation
```typescript
async function healthCheck(): Promise<{ status: string; vastai: any }> {
  const start = Date.now();
  try {
    await vastaiClient.ping();
    return { status: 'healthy', vastai: { connected: true, latencyMs: Date.now() - start } };
  } catch (error) {
    return { status: 'degraded', vastai: { connected: false, latencyMs: Date.now() - start } };
  }
}
```

### Immediate Rollback
```bash
kubectl rollout undo deployment/vastai-integration
kubectl rollout status deployment/vastai-integration
```