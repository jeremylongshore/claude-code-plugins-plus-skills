# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Invalid API Key | Incorrect or mismatched keys | Verify keys in Clerk dashboard match environment |
| ClerkProvider Missing | SDK used outside provider | Wrap app root with ClerkProvider |
| Middleware Not Running | Matcher misconfigured | Check matcher regex in middleware.ts |
| Module Not Found | Installation failed | Run `npm install @clerk/nextjs` again |