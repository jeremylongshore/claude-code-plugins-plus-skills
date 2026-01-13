# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| `Invalid signature` | Webhook secret mismatch | Verify secret matches Linear settings |
| `Token expired` | Refresh token expired | Re-authorize user |
| `Invalid scope` | Missing permission | Request additional scopes |