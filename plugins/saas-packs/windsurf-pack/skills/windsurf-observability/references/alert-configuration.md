# Alert Configuration

## Alert Configuration

### Prometheus AlertManager Rules

```yaml
# windsurf_alerts.yaml
groups:
  - name: windsurf_alerts
    rules:
      - alert: WindsurfHighErrorRate
        expr: |
          rate(windsurf_errors_total[5m]) /
          rate(windsurf_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Windsurf error rate > 5%"

      - alert: WindsurfHighLatency
        expr: |
          histogram_quantile(0.95,
            rate(windsurf_request_duration_seconds_bucket[5m])
          ) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Windsurf P95 latency > 2s"

      - alert: WindsurfDown
        expr: up{job="windsurf"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Windsurf integration is down"
```