# Error Handling Reference

| Scenario | Action |
|----------|--------|
| 429 received | Respect Retry-After header |
| Burst traffic | Use queue with concurrency limit |
| Sustained high volume | Implement sliding window |