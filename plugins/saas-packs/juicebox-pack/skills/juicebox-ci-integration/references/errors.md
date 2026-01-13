# Error Handling Reference

| CI Issue | Cause | Solution |
|----------|-------|----------|
| Secret not found | Not configured | Run `gh secret set` |
| Rate limited | Too many test runs | Use sandbox mode |
| Flaky tests | Network issues | Add retry logic |