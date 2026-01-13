# Error Handling Reference

| Scenario | Strategy |
|----------|----------|
| 429 with Retry-After | Wait exact duration |
| 429 without Retry-After | Exponential backoff |
| Approaching limit | Proactive throttling |
| Daily quota exhausted | Queue for next day |