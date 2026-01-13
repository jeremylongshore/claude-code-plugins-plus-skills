# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Invalid API Key | Incorrect or expired key | Verify key in Customer.io Settings > API Credentials |
| Invalid Site ID | Wrong site identifier | Check Site ID in Customer.io Settings |
| 401 Unauthorized | Authentication failed | Ensure both Site ID and API Key are correct |
| Network Error | Firewall blocking | Ensure outbound HTTPS to track.customer.io allowed |
| Module Not Found | Installation failed | Run `npm install` or `pip install` again |