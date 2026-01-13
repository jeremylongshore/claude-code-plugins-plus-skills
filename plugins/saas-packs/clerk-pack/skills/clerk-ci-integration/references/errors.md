# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Secret not found | Missing GitHub secret | Add secret in repo settings |
| Test user not found | User not created | Run setup script first |
| Timeout on sign-in | Slow response | Increase timeout, check network |
| Build fails | Missing env vars | Check all NEXT_PUBLIC vars set |