# Error Handling Reference

| Issue | Monitoring Action |
|-------|-------------------|
| High auth latency | Alert on p95 > 200ms |
| Failed webhooks | Alert on failure rate > 1% |
| Session anomalies | Track unusual session patterns |
| API errors | Capture with Sentry context |