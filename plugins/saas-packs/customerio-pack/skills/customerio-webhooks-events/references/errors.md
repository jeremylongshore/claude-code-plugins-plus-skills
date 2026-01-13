# Error Handling Reference

| Issue | Solution |
|-------|----------|
| Invalid signature | Verify webhook secret matches |
| Duplicate events | Use event_id for deduplication |
| Queue overflow | Increase worker concurrency |