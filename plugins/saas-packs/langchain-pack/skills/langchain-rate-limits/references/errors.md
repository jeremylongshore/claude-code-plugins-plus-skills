# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| RateLimitError | Exceeded quota | Implement backoff, reduce concurrency |
| Timeout | Request too slow | Increase timeout, check network |
| 429 Too Many Requests | API throttled | Wait and retry with backoff |
| Quota Exceeded | Monthly limit hit | Upgrade plan or switch provider |