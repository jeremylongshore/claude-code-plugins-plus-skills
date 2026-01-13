# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Wrong environment keys | Misconfiguration | Validate at startup |
| Webhook signature fails | Wrong secret | Check env-specific secret |
| User not found | Env mismatch | Check environment isolation |