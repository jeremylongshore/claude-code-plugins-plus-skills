# Alert Configuration

## Alert Configuration

### Prometheus AlertManager Rules

```yaml
# posthog_alerts.yaml
groups:
  - name: posthog_alerts
    rules:
      - alert: PostHogHighErrorRate
        expr: |
          rate(posthog_errors_total[5m]) /
          rate(posthog_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "PostHog error rate > 5%"

      - alert: PostHogHighLatency
        expr: |
          histogram_quantile(0.95,
            rate(posthog_request_duration_seconds_bucket[5m])
          ) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "PostHog P95 latency > 2s"

      - alert: PostHogDown
        expr: up{job="posthog"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "PostHog integration is down"
```