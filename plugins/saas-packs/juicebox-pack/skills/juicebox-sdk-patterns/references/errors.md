# Error Handling Reference

| Pattern | Use Case | Benefit |
|---------|----------|---------|
| Circuit Breaker | Prevent cascade failures | System resilience |
| Retry with Backoff | Transient errors | Higher success rate |
| Cache-Aside | Repeated queries | Lower latency |
| Bulkhead | Resource isolation | Fault isolation |