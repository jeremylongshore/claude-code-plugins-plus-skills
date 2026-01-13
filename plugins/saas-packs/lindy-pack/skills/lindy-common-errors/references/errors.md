# Error Handling Reference

| Error Code | HTTP Status | Retry? |
|------------|-------------|--------|
| LINDY_AUTH_INVALID_KEY | 401 | No |
| LINDY_RATE_LIMITED | 429 | Yes |
| LINDY_AGENT_NOT_FOUND | 404 | No |
| LINDY_AGENT_TIMEOUT | 504 | Yes |
| LINDY_TOOL_FAILED | 500 | Maybe |