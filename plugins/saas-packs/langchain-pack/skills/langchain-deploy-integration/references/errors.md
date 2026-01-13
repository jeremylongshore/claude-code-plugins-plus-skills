# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Container Crash | Missing env vars | Check secrets injection |
| Cold Start Timeout | LLM init slow | Use min-instances > 0 |
| Memory OOM | Large context | Increase memory limits |
| Connection Refused | Port mismatch | Verify EXPOSE and --port match |