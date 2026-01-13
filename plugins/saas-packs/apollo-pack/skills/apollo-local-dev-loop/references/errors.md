# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Missing API Key | .env not loaded | Run `source .env` or use dotenv |
| Mock Not Working | MSW not configured | Ensure setupServer is called |
| Rate Limited in Dev | Too many test calls | Use mock server for tests |
| Stale Credentials | Key rotated | Update .env with new key |