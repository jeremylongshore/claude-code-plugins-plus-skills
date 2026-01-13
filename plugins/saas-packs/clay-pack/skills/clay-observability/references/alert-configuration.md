# Alert Configuration

## Alert Configuration

### Prometheus AlertManager Rules

```yaml
# clay_alerts.yaml
groups:
  - name: clay_alerts
    rules:
      - alert: ClayHighErrorRate
        expr: |
          rate(clay_errors_total[5m]) /
          rate(clay_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Clay error rate > 5%"

      - alert: ClayHighLatency
        expr: |
          histogram_quantile(0.95,
            rate(clay_request_duration_seconds_bucket[5m])
          ) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Clay P95 latency > 2s"

      - alert: ClayDown
        expr: up{job="clay"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Clay integration is down"
```