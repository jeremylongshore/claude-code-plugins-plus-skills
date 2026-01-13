# Examples

### Health Check Implementation
```typescript
async function healthCheck(): Promise<{ status: string; retellai: any }> {
  const start = Date.now();
  try {
    await retellaiClient.ping();
    return { status: 'healthy', retellai: { connected: true, latencyMs: Date.now() - start } };
  } catch (error) {
    return { status: 'degraded', retellai: { connected: false, latencyMs: Date.now() - start } };
  }
}
```

### Immediate Rollback
```bash
kubectl rollout undo deployment/retellai-integration
kubectl rollout status deployment/retellai-integration
```