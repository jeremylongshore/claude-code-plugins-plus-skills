# Examples

### Health Check Implementation
```typescript
async function healthCheck(): Promise<{ status: string; coderabbit: any }> {
  const start = Date.now();
  try {
    await coderabbitClient.ping();
    return { status: 'healthy', coderabbit: { connected: true, latencyMs: Date.now() - start } };
  } catch (error) {
    return { status: 'degraded', coderabbit: { connected: false, latencyMs: Date.now() - start } };
  }
}
```

### Immediate Rollback
```bash
kubectl rollout undo deployment/coderabbit-integration
kubectl rollout status deployment/coderabbit-integration
```