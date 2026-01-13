# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Fixture Not Found | Missing audio file | Run fixture download script |
| Env Not Loaded | dotenv not configured | Install and configure dotenv |
| Watch Mode Fails | Missing tsx | Install tsx: `npm i -D tsx` |
| API Rate Limited | Too many dev requests | Use cached responses in tests |