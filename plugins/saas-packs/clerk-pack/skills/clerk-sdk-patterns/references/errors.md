# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| auth() returns null | Not in server context | Use in Server Components or API routes |
| useUser() not updating | Component not re-rendering | Check ClerkProvider placement |
| getToken() fails | Template not configured | Configure JWT template in dashboard |
| orgId is null | No organization selected | Prompt user to select organization |