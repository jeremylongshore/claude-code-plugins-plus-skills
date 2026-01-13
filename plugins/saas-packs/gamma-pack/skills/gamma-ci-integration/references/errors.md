# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Secret not found | Missing GitHub secret | Add GAMMA_API_KEY secret |
| Test timeout | Slow API response | Increase testTimeout |
| Mock mismatch | Mock out of sync | Update mock responses |
| Rate limit in CI | Too many test runs | Use mock mode for PRs |