# Alert Configuration

## Alert Configuration

### Prometheus AlertManager Rules

```yaml
# instantly_alerts.yaml
groups:
  - name: instantly_alerts
    rules:
      - alert: InstantlyHighErrorRate
        expr: |
          rate(instantly_errors_total[5m]) /
          rate(instantly_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Instantly error rate > 5%"

      - alert: InstantlyHighLatency
        expr: |
          histogram_quantile(0.95,
            rate(instantly_request_duration_seconds_bucket[5m])
          ) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Instantly P95 latency > 2s"

      - alert: InstantlyDown
        expr: up{job="instantly"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Instantly integration is down"
```