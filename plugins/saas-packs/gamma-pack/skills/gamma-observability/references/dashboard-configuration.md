# Dashboard Configuration

## Dashboard Configuration

### Grafana Dashboard
```json
{
  "title": "Gamma Integration",
  "panels": [
    {
      "title": "Request Rate",
      "type": "graph",
      "targets": [
        { "expr": "rate(gamma_requests_total[5m])" }
      ]
    },
    {
      "title": "Latency P95",
      "type": "graph",
      "targets": [
        { "expr": "histogram_quantile(0.95, rate(gamma_request_duration_seconds_bucket[5m]))" }
      ]
    },
    {
      "title": "Error Rate",
      "type": "stat",
      "targets": [
        { "expr": "rate(gamma_requests_total{status=~'5..'}[5m]) / rate(gamma_requests_total[5m])" }
      ]
    },
    {
      "title": "Rate Limit Remaining",
      "type": "gauge",
      "targets": [
        { "expr": "gamma_rate_limit_remaining" }
      ]
    }
  ]
}
```

### Alert Rules
```yaml
# prometheus/alerts.yml
groups:
  - name: gamma
    rules:
      - alert: GammaHighErrorRate
        expr: rate(gamma_requests_total{status=~"5.."}[5m]) / rate(gamma_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: High Gamma API error rate

      - alert: GammaRateLimitLow
        expr: gamma_rate_limit_remaining < 10
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: Gamma rate limit nearly exhausted

      - alert: GammaHighLatency
        expr: histogram_quantile(0.95, rate(gamma_request_duration_seconds_bucket[5m])) > 5
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: Gamma API latency is high
```