# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| `Circular JSON` | Logging full Linear objects | Use selective logging |
| `Memory leak` | Unbounded trace storage | Set maxTraces limit |
| `Missing env` | Validation failed | Check environment setup |