# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Secret Not Found | Missing GitHub secret | Add OPENAI_API_KEY to repository secrets |
| Rate Limit in CI | Too many API calls | Use mocks for unit tests, limit integration tests |
| Timeout | Slow tests | Add timeout markers, parallelize tests |
| Import Error | Missing dev dependencies | Ensure `.[dev]` extras installed |