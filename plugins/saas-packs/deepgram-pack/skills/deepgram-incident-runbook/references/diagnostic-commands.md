# Diagnostic Commands

## Diagnostic Commands

### Check Current Status
```bash
# API connectivity
curl -s -w "\nStatus: %{http_code}\nTime: %{time_total}s\n" \
  -X GET 'https://api.deepgram.com/v1/projects' \
  -H "Authorization: Token $DEEPGRAM_API_KEY"

# Test transcription
curl -X POST 'https://api.deepgram.com/v1/listen?model=nova-2' \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://static.deepgram.com/examples/nasa-podcast.wav"}'
```

### Check Application Metrics
```bash
# Error rate
curl -s 'http://localhost:9090/api/v1/query?query=rate(deepgram_errors_total[5m])'

# Request latency
curl -s 'http://localhost:9090/api/v1/query?query=histogram_quantile(0.95,rate(deepgram_latency_bucket[5m]))'

# Active connections
curl -s 'http://localhost:9090/api/v1/query?query=deepgram_active_connections'
```

### Check Kubernetes Resources
```bash
# Pod status
kubectl get pods -l app=deepgram-service

# Recent logs
kubectl logs -l app=deepgram-service --tail=100

# Resource usage
kubectl top pods -l app=deepgram-service
```