# Alert Configuration

## Alert Configuration

### Prometheus AlertManager Rules

```yaml
# groq_alerts.yaml
groups:
  - name: groq_alerts
    rules:
      - alert: GroqHighErrorRate
        expr: |
          rate(groq_errors_total[5m]) /
          rate(groq_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Groq error rate > 5%"

      - alert: GroqHighLatency
        expr: |
          histogram_quantile(0.95,
            rate(groq_request_duration_seconds_bucket[5m])
          ) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Groq P95 latency > 2s"

      - alert: GroqDown
        expr: up{job="groq"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Groq integration is down"
```