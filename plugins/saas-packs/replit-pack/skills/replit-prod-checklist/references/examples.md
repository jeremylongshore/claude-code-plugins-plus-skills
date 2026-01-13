# Examples

### Health Check Implementation
```typescript
async function healthCheck(): Promise<{ status: string; replit: any }> {
  const start = Date.now();
  try {
    await replitClient.ping();
    return { status: 'healthy', replit: { connected: true, latencyMs: Date.now() - start } };
  } catch (error) {
    return { status: 'degraded', replit: { connected: false, latencyMs: Date.now() - start } };
  }
}
```

### Immediate Rollback
```bash
kubectl rollout undo deployment/replit-integration
kubectl rollout status deployment/replit-integration
```