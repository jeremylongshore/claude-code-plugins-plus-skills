# Error Handling Reference

| Issue | Cause | Solution |
|-------|-------|----------|
| Invalid signature | Wrong secret | Verify webhook secret |
| Duplicate events | Network retry | Implement idempotency |
| Processing timeout | Slow handler | Use async queue |