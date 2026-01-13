# Error Handling Reference

| Issue | Cause | Solution |
|-------|-------|----------|
| Secret not found | Not configured | Add via `gh secret set` |
| Tests timeout | Agent slow | Increase jest timeout |
| Rate limited | Too many tests | Add delays or use test key |