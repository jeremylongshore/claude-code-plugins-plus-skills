# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Session not found | Expired or revoked | Redirect to sign-in |
| Token expired | JWT lifetime exceeded | Call getToken() for fresh token |
| Middleware loop | Incorrect matcher | Check matcher regex excludes static files |
| Headers already sent | Response already started | Check middleware order |