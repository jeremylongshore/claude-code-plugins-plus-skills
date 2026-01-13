# Examples

### Health Check Implementation
```typescript
async function healthCheck(): Promise<{ status: string; firecrawl: any }> {
  const start = Date.now();
  try {
    await firecrawlClient.ping();
    return { status: 'healthy', firecrawl: { connected: true, latencyMs: Date.now() - start } };
  } catch (error) {
    return { status: 'degraded', firecrawl: { connected: false, latencyMs: Date.now() - start } };
  }
}
```

### Immediate Rollback
```bash
kubectl rollout undo deployment/firecrawl-integration
kubectl rollout status deployment/firecrawl-integration
```