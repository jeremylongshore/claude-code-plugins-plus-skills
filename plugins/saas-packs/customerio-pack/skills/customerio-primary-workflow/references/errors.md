# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Event not triggering | Wrong event name | Match exact event name in dashboard |
| User not receiving | Missing email attribute | Ensure email is set on identify |
| Duplicate sends | Multiple event fires | Deduplicate or use idempotency |