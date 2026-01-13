# Examples

### Health Check Implementation
```typescript
async function healthCheck(): Promise<{ status: string; ideogram: any }> {
  const start = Date.now();
  try {
    await ideogramClient.ping();
    return { status: 'healthy', ideogram: { connected: true, latencyMs: Date.now() - start } };
  } catch (error) {
    return { status: 'degraded', ideogram: { connected: false, latencyMs: Date.now() - start } };
  }
}
```

### Immediate Rollback
```bash
kubectl rollout undo deployment/ideogram-integration
kubectl rollout status deployment/ideogram-integration
```