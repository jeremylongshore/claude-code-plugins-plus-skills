# Error Handling Reference

| Scenario | Strategy | Code |
|----------|----------|------|
| Near limit | Slow down | Reduce request rate |
| Hit limit | Wait | Respect Retry-After |
| Burst | Queue | Implement request queue |