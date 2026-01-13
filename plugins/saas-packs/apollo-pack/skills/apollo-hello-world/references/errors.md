# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| 401 Unauthorized | Invalid API key | Check APOLLO_API_KEY environment variable |
| 422 Unprocessable | Invalid request body | Verify request payload format |
| 429 Rate Limited | Too many requests | Wait and retry with exponential backoff |
| Empty Results | No matching contacts | Broaden search criteria |