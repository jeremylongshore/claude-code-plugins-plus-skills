# Error Handling Reference

| Scenario | Action |
|----------|--------|
| Partial deletion | Retry failed services, log for manual review |
| Export timeout | Queue export, email when complete |
| Consent sync fail | Retry with exponential backoff |