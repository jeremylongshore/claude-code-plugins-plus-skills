# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Type Mismatch | Incorrect response shape | Add runtime validation |
| Client Undefined | Singleton not initialized | Call init() before use |
| Memory Leak | Multiple client instances | Use singleton pattern |
| Timeout | Large audio file | Increase timeout settings |