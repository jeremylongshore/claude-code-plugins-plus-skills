# Examples

### Health Check Implementation
```typescript
async function healthCheck(): Promise<{ status: string; perplexity: any }> {
  const start = Date.now();
  try {
    await perplexityClient.ping();
    return { status: 'healthy', perplexity: { connected: true, latencyMs: Date.now() - start } };
  } catch (error) {
    return { status: 'degraded', perplexity: { connected: false, latencyMs: Date.now() - start } };
  }
}
```

### Immediate Rollback
```bash
kubectl rollout undo deployment/perplexity-integration
kubectl rollout status deployment/perplexity-integration
```