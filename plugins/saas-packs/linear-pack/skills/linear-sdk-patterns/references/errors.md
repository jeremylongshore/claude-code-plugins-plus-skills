# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| `Type mismatch` | SDK version incompatibility | Update @linear/sdk package |
| `Undefined property` | Nullable field access | Use optional chaining (?.) |
| `Promise rejection` | Unhandled async error | Wrap in try/catch or use wrapper |