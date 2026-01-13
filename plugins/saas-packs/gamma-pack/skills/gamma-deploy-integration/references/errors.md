# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Secret not found | Missing secret | Create secret in platform |
| Timeout | Function too slow | Increase timeout limit |
| Cold start | Lambda initialization | Use provisioned concurrency |
| Permission denied | IAM misconfigured | Update IAM policies |