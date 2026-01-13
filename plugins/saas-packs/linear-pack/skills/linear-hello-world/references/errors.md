# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| `Team not found` | Invalid team ID or no access | Use `client.teams()` to list accessible teams |
| `Validation error` | Missing required fields | Ensure title and teamId are provided |
| `Permission denied` | Insufficient permissions | Check API key scope in Linear settings |
| `Rate limited` | Too many requests | Add delays between requests |