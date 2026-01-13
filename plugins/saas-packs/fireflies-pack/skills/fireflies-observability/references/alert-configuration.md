# Alert Configuration

## Alert Configuration

### Prometheus AlertManager Rules

```yaml
# fireflies_alerts.yaml
groups:
  - name: fireflies_alerts
    rules:
      - alert: Fireflies.aiHighErrorRate
        expr: |
          rate(fireflies_errors_total[5m]) /
          rate(fireflies_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Fireflies.ai error rate > 5%"

      - alert: Fireflies.aiHighLatency
        expr: |
          histogram_quantile(0.95,
            rate(fireflies_request_duration_seconds_bucket[5m])
          ) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Fireflies.ai P95 latency > 2s"

      - alert: Fireflies.aiDown
        expr: up{job="fireflies"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Fireflies.ai integration is down"
```