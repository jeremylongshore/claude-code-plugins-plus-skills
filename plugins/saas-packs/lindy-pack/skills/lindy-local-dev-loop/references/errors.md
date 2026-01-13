# Error Handling Reference

| Error | Cause | Solution |
|-------|-------|----------|
| ts-node not found | Dev deps missing | `npm install -D ts-node` |
| ENV not loaded | dotenv not configured | Add `import 'dotenv/config'` |
| Type errors | Missing types | `npm install -D @types/node` |