# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| 429 Too Many Requests | Rate limit exceeded | Implement backoff, cache more |
| quota_exceeded | Monthly quota hit | Upgrade plan or reduce usage |
| concurrent_limit | Too many parallel requests | Queue requests |