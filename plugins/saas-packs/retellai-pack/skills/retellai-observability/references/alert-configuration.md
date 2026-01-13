# Alert Configuration

## Alert Configuration

### Prometheus AlertManager Rules

```yaml
# retellai_alerts.yaml
groups:
  - name: retellai_alerts
    rules:
      - alert: Retell AIHighErrorRate
        expr: |
          rate(retellai_errors_total[5m]) /
          rate(retellai_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Retell AI error rate > 5%"

      - alert: Retell AIHighLatency
        expr: |
          histogram_quantile(0.95,
            rate(retellai_request_duration_seconds_bucket[5m])
          ) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Retell AI P95 latency > 2s"

      - alert: Retell AIDown
        expr: up{job="retellai"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Retell AI integration is down"
```