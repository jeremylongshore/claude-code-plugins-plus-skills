# Error Handling Reference

| Pattern | When to Use |
|---------|-------------|
| Singleton | Always - ensures single client instance |
| Retry | Network errors, 429/500 responses |
| Pagination | Large result sets (>100 records) |
| Batching | Multiple enrichment calls |
| Custom Errors | Distinguish error types in catch blocks |