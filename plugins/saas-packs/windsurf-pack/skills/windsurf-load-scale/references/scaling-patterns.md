# Scaling Patterns

## Scaling Patterns

### Horizontal Scaling
```yaml
# kubernetes HPA
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: windsurf-integration-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: windsurf-integration
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
          name: windsurf_queue_depth
        target:
          type: AverageValue
          averageValue: 100
```

### Connection Pooling
```typescript
import { Pool } from 'generic-pool';

const windsurfPool = Pool.create({
  create: async () => {
    return new WindsurfClient({
      apiKey: process.env.WINDSURF_API_KEY!,
    });
  },
  destroy: async (client) => {
    await client.close();
  },
  max: 20,
  min: 5,
  idleTimeoutMillis: 30000,
});

async function withWindsurfClient<T>(
  fn: (client: WindsurfClient) => Promise<T>
): Promise<T> {
  const client = await windsurfPool.acquire();
  try {
    return await fn(client);
  } finally {
    windsurfPool.release(client);
  }
}
```