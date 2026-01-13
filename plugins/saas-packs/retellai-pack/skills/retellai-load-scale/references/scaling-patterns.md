# Scaling Patterns

## Scaling Patterns

### Horizontal Scaling
```yaml
# kubernetes HPA
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: retellai-integration-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: retellai-integration
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
          name: retellai_queue_depth
        target:
          type: AverageValue
          averageValue: 100
```

### Connection Pooling
```typescript
import { Pool } from 'generic-pool';

const retellaiPool = Pool.create({
  create: async () => {
    return new RetellAIClient({
      apiKey: process.env.RETELLAI_API_KEY!,
    });
  },
  destroy: async (client) => {
    await client.close();
  },
  max: 20,
  min: 5,
  idleTimeoutMillis: 30000,
});

async function withRetell AIClient<T>(
  fn: (client: RetellAIClient) => Promise<T>
): Promise<T> {
  const client = await retellaiPool.acquire();
  try {
    return await fn(client);
  } finally {
    retellaiPool.release(client);
  }
}
```