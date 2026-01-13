# Alert Configuration

## Alert Configuration

### Prometheus AlertManager Rules

```yaml
# firecrawl_alerts.yaml
groups:
  - name: firecrawl_alerts
    rules:
      - alert: FireCrawlHighErrorRate
        expr: |
          rate(firecrawl_errors_total[5m]) /
          rate(firecrawl_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "FireCrawl error rate > 5%"

      - alert: FireCrawlHighLatency
        expr: |
          histogram_quantile(0.95,
            rate(firecrawl_request_duration_seconds_bucket[5m])
          ) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "FireCrawl P95 latency > 2s"

      - alert: FireCrawlDown
        expr: up{job="firecrawl"} == 0
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "FireCrawl integration is down"
```