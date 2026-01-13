# Error Handling Reference

| Risk | Mitigation |
|------|------------|
| API Key Exposure | Use secrets manager, never hardcode |
| Prompt Injection | Validate input, separate user/system prompts |
| Code Execution | Whitelist commands, sandbox execution |
| Data Leakage | Validate outputs, mask sensitive data |
| Denial of Service | Rate limit, set timeouts |