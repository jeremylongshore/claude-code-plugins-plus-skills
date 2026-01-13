# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| `429 Too Many Requests` | Rate limit exceeded | Use backoff and queue |
| `Complexity exceeded` | Query too expensive | Simplify query structure |
| `Timeout` | Long-running query | Paginate or split queries |