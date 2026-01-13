# Examples

### Quick k6 Test
```bash
k6 run --vus 10 --duration 30s windsurf-load-test.js
```

### Check Current Capacity
```typescript
const metrics = await getSystemMetrics();
const capacity = estimateWindsurfCapacity(metrics);
console.log('Headroom:', capacity.headroom + '%');
console.log('Recommendation:', capacity.scaleRecommendation);
```

### Scale HPA Manually
```bash
kubectl scale deployment windsurf-integration --replicas=5
kubectl get hpa windsurf-integration-hpa
```