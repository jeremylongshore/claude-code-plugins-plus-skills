# Error Handling Reference

| Header | Description | Action |
|--------|-------------|--------|
| X-RateLimit-Limit | Max requests | Monitor usage |
| X-RateLimit-Remaining | Remaining requests | Throttle if low |
| X-RateLimit-Reset | Reset timestamp | Wait until reset |
| Retry-After | Seconds to wait | Honor this value |