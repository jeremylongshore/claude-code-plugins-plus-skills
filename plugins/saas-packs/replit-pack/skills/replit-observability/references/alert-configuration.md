# Alert Configuration

## Alert Configuration

### Prometheus AlertManager Rules

```yaml
# replit_alerts.yaml
groups:
  - name: replit_alerts
    rules:
      - alert: ReplitHighErrorRate
        expr: |
          rate(replit_errors_total[5m]) /
          rate(replit_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Replit error rate > 5%"

      - alert: ReplitHighLatency
        expr: |
          histogram_quantile(0.95,
            rate(replit_request_duration_seconds_bucket[5m])
          ) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Replit P95 latency > 2s"

      - alert: ReplitDown
        expr: up{job="replit"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Replit integration is down"
```