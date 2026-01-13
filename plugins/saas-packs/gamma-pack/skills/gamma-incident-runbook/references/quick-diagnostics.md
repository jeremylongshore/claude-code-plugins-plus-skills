# Quick Diagnostics

## Quick Diagnostics

### Step 1: Check Gamma Status
```bash
# Check Gamma status page
curl -s https://status.gamma.app/api/v2/status.json | jq '.status'

# Check our integration health
curl -s https://your-app.com/health/gamma | jq '.'

# Quick connectivity test
curl -w "\nTime: %{time_total}s\n" \
  -H "Authorization: Bearer $GAMMA_API_KEY" \
  https://api.gamma.app/v1/ping
```

### Step 2: Review Key Metrics
```bash
# Check error rate (Prometheus)
curl -s 'http://prometheus:9090/api/v1/query?query=rate(gamma_requests_total{status=~"5.."}[5m])' | jq '.data.result'

# Check latency P95
curl -s 'http://prometheus:9090/api/v1/query?query=histogram_quantile(0.95,rate(gamma_request_duration_seconds_bucket[5m]))' | jq '.data.result'

# Check rate limit
curl -s 'http://prometheus:9090/api/v1/query?query=gamma_rate_limit_remaining' | jq '.data.result'
```

### Step 3: Review Recent Logs
```bash
# Last 100 error logs
grep -i "gamma.*error" /var/log/app/gamma-*.log | tail -100

# Rate limit hits
grep "429" /var/log/app/gamma-*.log | wc -l

# Timeout errors
grep -i "timeout" /var/log/app/gamma-*.log | tail -50
```