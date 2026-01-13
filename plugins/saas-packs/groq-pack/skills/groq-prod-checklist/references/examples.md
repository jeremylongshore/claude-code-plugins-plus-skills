# Examples

### Health Check Implementation
```typescript
async function healthCheck(): Promise<{ status: string; groq: any }> {
  const start = Date.now();
  try {
    await groqClient.ping();
    return { status: 'healthy', groq: { connected: true, latencyMs: Date.now() - start } };
  } catch (error) {
    return { status: 'degraded', groq: { connected: false, latencyMs: Date.now() - start } };
  }
}
```

### Immediate Rollback
```bash
kubectl rollout undo deployment/groq-integration
kubectl rollout status deployment/groq-integration
```