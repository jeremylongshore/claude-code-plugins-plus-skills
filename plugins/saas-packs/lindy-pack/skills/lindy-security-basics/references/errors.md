# Error Handling Reference

| Risk | Mitigation | Implementation |
|------|------------|----------------|
| Key exposure | Secret manager | Use cloud secrets |
| Wrong env | Validation | Check key prefix |
| Over-permission | Least privilege | Restrict agent tools |
| No audit | Logging | Log all operations |