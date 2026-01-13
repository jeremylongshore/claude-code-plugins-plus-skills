# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Wrong environment | Env vars not loaded | Use dotenv or env-specific files |
| Dev events in prod | Environment check failed | Verify NODE_ENV is set correctly |
| Mock not working | Import order issue | Mock before importing client |