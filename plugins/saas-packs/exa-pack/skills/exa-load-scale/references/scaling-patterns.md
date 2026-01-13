# Scaling Patterns

## Scaling Patterns

### Horizontal Scaling
```yaml
# kubernetes HPA
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: exa-integration-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: exa-integration
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
          name: exa_queue_depth
        target:
          type: AverageValue
          averageValue: 100
```

### Connection Pooling
```typescript
import { Pool } from 'generic-pool';

const exaPool = Pool.create({
  create: async () => {
    return new ExaClient({
      apiKey: process.env.EXA_API_KEY!,
    });
  },
  destroy: async (client) => {
    await client.close();
  },
  max: 20,
  min: 5,
  idleTimeoutMillis: 30000,
});

async function withExaClient<T>(
  fn: (client: ExaClient) => Promise<T>
): Promise<T> {
  const client = await exaPool.acquire();
  try {
    return await fn(client);
  } finally {
    exaPool.release(client);
  }
}
```