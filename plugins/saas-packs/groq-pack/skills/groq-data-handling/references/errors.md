# Error Handling Reference

| Issue | Cause | Solution |
|-------|-------|----------|
| PII in logs | Missing redaction | Wrap logging with redact |
| Deletion failed | Data locked | Check dependencies |
| Export incomplete | Timeout | Increase batch size |
| Audit gap | Missing entries | Review log pipeline |