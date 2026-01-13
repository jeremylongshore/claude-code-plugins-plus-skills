# Alert Configuration

## Alert Configuration

### Prometheus AlertManager Rules

```yaml
# exa_alerts.yaml
groups:
  - name: exa_alerts
    rules:
      - alert: ExaHighErrorRate
        expr: |
          rate(exa_errors_total[5m]) /
          rate(exa_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Exa error rate > 5%"

      - alert: ExaHighLatency
        expr: |
          histogram_quantile(0.95,
            rate(exa_request_duration_seconds_bucket[5m])
          ) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Exa P95 latency > 2s"

      - alert: ExaDown
        expr: up{job="exa"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Exa integration is down"
```