# Examples

### Health Check Implementation
```typescript
async function healthCheck(): Promise<{ status: string; windsurf: any }> {
  const start = Date.now();
  try {
    await windsurfClient.ping();
    return { status: 'healthy', windsurf: { connected: true, latencyMs: Date.now() - start } };
  } catch (error) {
    return { status: 'degraded', windsurf: { connected: false, latencyMs: Date.now() - start } };
  }
}
```

### Immediate Rollback
```bash
kubectl rollout undo deployment/windsurf-integration
kubectl rollout status deployment/windsurf-integration
```