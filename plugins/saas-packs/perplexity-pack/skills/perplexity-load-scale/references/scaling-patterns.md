# Scaling Patterns

## Scaling Patterns

### Horizontal Scaling
```yaml
# kubernetes HPA
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: perplexity-integration-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: perplexity-integration
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
          name: perplexity_queue_depth
        target:
          type: AverageValue
          averageValue: 100
```

### Connection Pooling
```typescript
import { Pool } from 'generic-pool';

const perplexityPool = Pool.create({
  create: async () => {
    return new PerplexityClient({
      apiKey: process.env.PERPLEXITY_API_KEY!,
    });
  },
  destroy: async (client) => {
    await client.close();
  },
  max: 20,
  min: 5,
  idleTimeoutMillis: 30000,
});

async function withPerplexityClient<T>(
  fn: (client: PerplexityClient) => Promise<T>
): Promise<T> {
  const client = await perplexityPool.acquire();
  try {
    return await fn(client);
  } finally {
    perplexityPool.release(client);
  }
}
```