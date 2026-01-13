# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| `Invalid signature` | Wrong secret or tampering | Verify webhook secret |
| `Timeout` | Processing too slow | Use async queue |
| `Duplicate events` | Webhook retry | Implement idempotency |
| `Missing data` | Partial event | Handle gracefully |