# Examples

### Quick k6 Test
```bash
k6 run --vus 10 --duration 30s replit-load-test.js
```

### Check Current Capacity
```typescript
const metrics = await getSystemMetrics();
const capacity = estimateReplitCapacity(metrics);
console.log('Headroom:', capacity.headroom + '%');
console.log('Recommendation:', capacity.scaleRecommendation);
```

### Scale HPA Manually
```bash
kubectl scale deployment replit-integration --replicas=5
kubectl get hpa replit-integration-hpa
```