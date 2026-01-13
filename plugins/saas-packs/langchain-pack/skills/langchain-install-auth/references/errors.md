# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Invalid API Key | Incorrect or expired key | Verify key in provider dashboard |
| Rate Limited | Exceeded quota | Check quota limits, implement backoff |
| Network Error | Firewall blocking | Ensure outbound HTTPS allowed |
| Module Not Found | Installation failed | Run `pip install` again, check Python version |
| Provider Error | Service unavailable | Check provider status page |