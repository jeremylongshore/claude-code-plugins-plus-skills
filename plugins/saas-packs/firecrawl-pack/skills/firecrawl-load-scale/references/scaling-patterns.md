# Scaling Patterns

## Scaling Patterns

### Horizontal Scaling
```yaml
# kubernetes HPA
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: firecrawl-integration-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: firecrawl-integration
  minReplicas: 2
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Pods
      pods:
        metric:
          name: firecrawl_queue_depth
        target:
          type: AverageValue
          averageValue: 100
```

### Connection Pooling
```typescript
import { Pool } from 'generic-pool';

const firecrawlPool = Pool.create({
  create: async () => {
    return new FireCrawlClient({
      apiKey: process.env.FIRECRAWL_API_KEY!,
    });
  },
  destroy: async (client) => {
    await client.close();
  },
  max: 20,
  min: 5,
  idleTimeoutMillis: 30000,
});

async function withFireCrawlClient<T>(
  fn: (client: FireCrawlClient) => Promise<T>
): Promise<T> {
  const client = await firecrawlPool.acquire();
  try {
    return await fn(client);
  } finally {
    firecrawlPool.release(client);
  }
}
```