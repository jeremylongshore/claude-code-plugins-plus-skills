# Alert Configuration

## Alert Configuration

### Prometheus AlertManager Rules

```yaml
# perplexity_alerts.yaml
groups:
  - name: perplexity_alerts
    rules:
      - alert: PerplexityHighErrorRate
        expr: |
          rate(perplexity_errors_total[5m]) /
          rate(perplexity_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Perplexity error rate > 5%"

      - alert: PerplexityHighLatency
        expr: |
          histogram_quantile(0.95,
            rate(perplexity_request_duration_seconds_bucket[5m])
          ) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Perplexity P95 latency > 2s"

      - alert: PerplexityDown
        expr: up{job="perplexity"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Perplexity integration is down"
```