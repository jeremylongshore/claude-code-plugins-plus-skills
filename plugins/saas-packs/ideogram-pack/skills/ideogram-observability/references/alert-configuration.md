# Alert Configuration

## Alert Configuration

### Prometheus AlertManager Rules

```yaml
# ideogram_alerts.yaml
groups:
  - name: ideogram_alerts
    rules:
      - alert: IdeogramHighErrorRate
        expr: |
          rate(ideogram_errors_total[5m]) /
          rate(ideogram_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Ideogram error rate > 5%"

      - alert: IdeogramHighLatency
        expr: |
          histogram_quantile(0.95,
            rate(ideogram_request_duration_seconds_bucket[5m])
          ) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Ideogram P95 latency > 2s"

      - alert: IdeogramDown
        expr: up{job="ideogram"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Ideogram integration is down"
```