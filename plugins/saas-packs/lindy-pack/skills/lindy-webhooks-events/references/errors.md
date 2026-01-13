# Error Handling Reference

| Issue | Cause | Solution |
|-------|-------|----------|
| Invalid signature | Wrong secret | Check WEBHOOK_SECRET |
| Timeout | Handler slow | Respond quickly, process async |
| Duplicate events | Retry delivery | Implement idempotency |