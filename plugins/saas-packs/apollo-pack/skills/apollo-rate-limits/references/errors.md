# Error Handling Reference

| Scenario | Strategy |
|----------|----------|
| 429 response | Use Retry-After header |
| Burst limit hit | Add minimum spacing |
| Sustained limit | Queue with concurrency |
| Network timeout | Exponential backoff |