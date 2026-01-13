# Error Handling Reference

| Issue | Cause | Solution |
|-------|-------|----------|
| Circular dependencies | Wrong layering | Separate concerns by layer |
| Config not loading | Wrong paths | Verify config file locations |
| Type errors | Missing types | Add Vast.ai types |
| Test isolation | Shared state | Use dependency injection |