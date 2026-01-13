# Error Handling Reference

| Pattern | Failure Mode | Recovery |
|---------|--------------|----------|
| Basic | API error | Retry with backoff |
| Event-driven | Worker crash | Queue retry |
| Multi-agent | Step failure | Skip or fallback |
| HA | Primary down | Automatic failover |