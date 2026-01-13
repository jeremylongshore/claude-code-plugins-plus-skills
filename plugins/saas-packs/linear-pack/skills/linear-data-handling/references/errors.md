# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| `Sync timeout` | Too many records | Use smaller batches |
| `Conflict detected` | Concurrent edits | Apply conflict resolution |
| `Stale data` | Missed webhooks | Trigger full sync |
| `Export failed` | API rate limit | Add delays between requests |