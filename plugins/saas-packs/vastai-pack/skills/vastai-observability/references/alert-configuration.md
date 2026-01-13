# Alert Configuration

## Alert Configuration

### Prometheus AlertManager Rules

```yaml
# vastai_alerts.yaml
groups:
  - name: vastai_alerts
    rules:
      - alert: Vast.aiHighErrorRate
        expr: |
          rate(vastai_errors_total[5m]) /
          rate(vastai_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Vast.ai error rate > 5%"

      - alert: Vast.aiHighLatency
        expr: |
          histogram_quantile(0.95,
            rate(vastai_request_duration_seconds_bucket[5m])
          ) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Vast.ai P95 latency > 2s"

      - alert: Vast.aiDown
        expr: up{job="vastai"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Vast.ai integration is down"
```