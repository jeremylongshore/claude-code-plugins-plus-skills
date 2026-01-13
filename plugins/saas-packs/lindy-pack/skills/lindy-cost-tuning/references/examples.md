# Examples

### Monthly Cost Report
```typescript
async function generateCostReport() {
  const usage = await analyzeUsage();

  const report = `
# Lindy Cost Report - ${new Date().toISOString().slice(0, 7)}