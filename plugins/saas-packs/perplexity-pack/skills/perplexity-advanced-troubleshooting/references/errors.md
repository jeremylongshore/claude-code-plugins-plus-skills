# Error Handling Reference

| Issue | Cause | Solution |
|-------|-------|----------|
| Can't reproduce | Race condition | Add timing analysis |
| Intermittent failure | Timing-dependent | Increase sample size |
| No useful logs | Missing instrumentation | Add debug logging |
| Memory growth | Resource leak | Use heap profiling |