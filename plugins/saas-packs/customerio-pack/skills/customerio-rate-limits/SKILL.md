---
allowed-tools: Read, Grep, Bash
license: MIT
description: Implement customer.io rate limiting and backoff. use when handling high-volume
  api calls, implementing retry logic, or optimizing api usage. trigger with phrases
  like "customer.io rate limit", "customer.io throttle", "customer.io 429", "customer.i...
name: customerio-rate-limits
---
# Customerio Rate Limits


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Token bucket rate limiter
- Exponential backoff with jitter
- Rate-limited Customer.io client
- Queue-based rate limiting

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [API Rate Limits](https://customer.io/docs/api/track/#section/Limits)
- [Best Practices](https://customer.io/docs/best-practices/)
