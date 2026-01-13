# Error Handling Reference

### Retry Configuration
```yaml
# Zapier Error Handling
On Error:
  Retry: 3 times
  Delay: 5 minutes between retries
  Fallback: Send error to Slack #ops-alerts
```

### Common Errors
| Error | Cause | Solution |
|-------|-------|----------|
| Webhook timeout | Large payload | Add processing delay |
| Auth expired | Token invalid | Refresh OAuth tokens |
| Rate limited | Too many requests | Add delays between actions |
| Parse failed | Note format changed | Update parsing logic |