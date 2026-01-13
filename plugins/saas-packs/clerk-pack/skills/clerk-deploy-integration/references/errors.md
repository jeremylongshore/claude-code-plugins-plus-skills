# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| 500 on sign-in | Missing secret key | Add CLERK_SECRET_KEY to platform |
| Webhook fails | Wrong endpoint URL | Update URL in Clerk Dashboard |
| CORS error | Domain not allowed | Add domain to Clerk allowed origins |
| Redirect loop | Wrong sign-in URL | Check CLERK_SIGN_IN_URL config |