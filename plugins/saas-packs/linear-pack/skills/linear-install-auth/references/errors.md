# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| `Authentication failed` | Invalid or expired API key | Generate new key in Linear settings |
| `Invalid API key format` | Key doesn't start with `lin_api_` | Verify key format from Linear |
| `Rate limited` | Too many requests | Implement exponential backoff |
| `Module not found` | Installation failed | Run `npm install @linear/sdk` again |
| `Network error` | Firewall blocking | Ensure outbound HTTPS to api.linear.app |