# Examples

### Health Check Implementation
```typescript
async function healthCheck(): Promise<{ status: string; exa: any }> {
  const start = Date.now();
  try {
    await exaClient.ping();
    return { status: 'healthy', exa: { connected: true, latencyMs: Date.now() - start } };
  } catch (error) {
    return { status: 'degraded', exa: { connected: false, latencyMs: Date.now() - start } };
  }
}
```

### Immediate Rollback
```bash
kubectl rollout undo deployment/exa-integration
kubectl rollout status deployment/exa-integration
```