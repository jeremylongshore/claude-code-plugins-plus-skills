# Error Handling Reference

| Error Code | Meaning | Action |
|------------|---------|--------|
| 400 | Bad Request | Check request format and data |
| 401 | Unauthorized | Verify API credentials |
| 403 | Forbidden | Check API key permissions |
| 404 | Not Found | Verify endpoint URL |
| 429 | Rate Limited | Implement backoff |
| 500 | Server Error | Retry with backoff |