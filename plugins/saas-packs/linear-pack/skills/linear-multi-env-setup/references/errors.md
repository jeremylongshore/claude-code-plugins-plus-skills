# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| `Wrong environment` | API key mismatch | Verify secrets for correct env |
| `Secret not found` | Missing secret | Add secret to secret manager |
| `Team not found` | Wrong workspace | Check defaultTeamKey setting |
| `Permission denied` | Insufficient scope | Regenerate API key |