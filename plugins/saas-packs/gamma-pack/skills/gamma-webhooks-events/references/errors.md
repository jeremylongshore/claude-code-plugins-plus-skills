# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Invalid signature | Secret mismatch | Verify webhook secret |
| Timeout | Slow processing | Use async queue |
| Duplicate events | Retry delivery | Implement idempotency |
| Missing events | Endpoint down | Use reliable hosting |