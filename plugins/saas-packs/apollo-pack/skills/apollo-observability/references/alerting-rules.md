# Alerting Rules

## Alerting Rules

```yaml
# prometheus/apollo-alerts.yml
groups:
  - name: apollo-alerts
    rules:
      # High error rate
      - alert: ApolloHighErrorRate
        expr: |
          sum(rate(apollo_errors_total[5m])) /
          sum(rate(apollo_requests_total[5m])) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High Apollo API error rate"
          description: "Apollo error rate is {{ $value | humanizePercentage }}"

      # Rate limit warnings
      - alert: ApolloRateLimitApproaching
        expr: apollo_rate_limit_remaining < 20
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "Apollo rate limit approaching"
          description: "Only {{ $value }} requests remaining"

      - alert: ApolloRateLimitHit
        expr: increase(apollo_rate_limit_hits_total[5m]) > 0
        labels:
          severity: critical
        annotations:
          summary: "Apollo rate limit hit"
          description: "Rate limit was hit {{ $value }} times in last 5 minutes"

      # Latency alerts
      - alert: ApolloHighLatency
        expr: |
          histogram_quantile(0.95, rate(apollo_request_duration_seconds_bucket[5m])) > 5
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "High Apollo API latency"
          description: "P95 latency is {{ $value | humanizeDuration }}"

      # Credit usage
      - alert: ApolloHighCreditUsage
        expr: |
          increase(apollo_credits_used_total[24h]) > 8000
        labels:
          severity: warning
        annotations:
          summary: "High Apollo credit consumption"
          description: "{{ $value }} credits used in last 24 hours"
```