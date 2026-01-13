# Examples

### Health Check Implementation
```typescript
async function healthCheck(): Promise<{ status: string; posthog: any }> {
  const start = Date.now();
  try {
    await posthogClient.ping();
    return { status: 'healthy', posthog: { connected: true, latencyMs: Date.now() - start } };
  } catch (error) {
    return { status: 'degraded', posthog: { connected: false, latencyMs: Date.now() - start } };
  }
}
```

### Immediate Rollback
```bash
kubectl rollout undo deployment/posthog-integration
kubectl rollout status deployment/posthog-integration
```