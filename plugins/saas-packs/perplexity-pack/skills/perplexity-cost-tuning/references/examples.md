# Examples

### Quick Cost Check
```typescript
// Estimate monthly cost for your usage
const estimate = estimatePerplexityCost(yourMonthlyRequests);
console.log(`Tier: ${estimate.tier}, Cost: $${estimate.estimatedCost}`);
if (estimate.recommendation) {
  console.log(`💡 ${estimate.recommendation}`);
}
```