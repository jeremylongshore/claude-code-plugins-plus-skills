# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Invalid signature | Wrong secret | Verify CLERK_WEBHOOK_SECRET |
| Missing headers | Request not from Clerk | Check sender is Clerk |
| Duplicate processing | Event sent twice | Implement idempotency |
| Timeout | Handler too slow | Use background jobs |