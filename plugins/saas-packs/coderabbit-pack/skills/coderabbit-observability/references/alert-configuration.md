# Alert Configuration

## Alert Configuration

### Prometheus AlertManager Rules

```yaml
# coderabbit_alerts.yaml
groups:
  - name: coderabbit_alerts
    rules:
      - alert: CodeRabbitHighErrorRate
        expr: |
          rate(coderabbit_errors_total[5m]) /
          rate(coderabbit_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "CodeRabbit error rate > 5%"

      - alert: CodeRabbitHighLatency
        expr: |
          histogram_quantile(0.95,
            rate(coderabbit_request_duration_seconds_bucket[5m])
          ) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "CodeRabbit P95 latency > 2s"

      - alert: CodeRabbitDown
        expr: up{job="coderabbit"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "CodeRabbit integration is down"
```