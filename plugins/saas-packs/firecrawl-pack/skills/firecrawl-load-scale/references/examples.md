# Examples

### Quick k6 Test
```bash
k6 run --vus 10 --duration 30s firecrawl-load-test.js
```

### Check Current Capacity
```typescript
const metrics = await getSystemMetrics();
const capacity = estimateFireCrawlCapacity(metrics);
console.log('Headroom:', capacity.headroom + '%');
console.log('Recommendation:', capacity.scaleRecommendation);
```

### Scale HPA Manually
```bash
kubectl scale deployment firecrawl-integration --replicas=5
kubectl get hpa firecrawl-integration-hpa
```