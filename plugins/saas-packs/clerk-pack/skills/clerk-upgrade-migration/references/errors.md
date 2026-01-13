# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| Type errors after upgrade | API changes | Check changelog, update types |
| Middleware not executing | Matcher syntax changed | Update matcher regex |
| auth() returns Promise | Now async in v6 | Add await to auth() calls |
| Import errors | Path changes | Update to @clerk/nextjs/server |