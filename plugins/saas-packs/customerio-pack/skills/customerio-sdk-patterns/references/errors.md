# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Type mismatch | Invalid attribute type | Use TypeScript interfaces |
| Queue overflow | Too many events | Increase flush frequency or batch size |
| Retry exhausted | Persistent failure | Check network and credentials |