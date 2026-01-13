# Error Handling Reference

| Scenario | Strategy | Implementation |
|----------|----------|----------------|
| Occasional 429 | Exponential backoff | `withBackoff()` wrapper |
| Consistent 429 | Request queue | `RateLimitedQueue` class |
| Near limit | Preemptive throttle | Check remaining before call |
| Burst traffic | Token bucket | Implement token bucket algorithm |