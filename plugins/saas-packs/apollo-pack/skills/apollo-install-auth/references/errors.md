# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| 401 Unauthorized | Invalid API key | Verify key in Apollo dashboard |
| 403 Forbidden | Insufficient permissions | Check API plan and permissions |
| 429 Rate Limited | Exceeded quota | Implement backoff, check usage |
| Network Error | Firewall blocking | Ensure outbound HTTPS to api.apollo.io |