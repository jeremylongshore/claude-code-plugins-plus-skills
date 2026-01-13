---
allowed-tools: Read, Write, Edit, Grep
license: MIT
description: Handle linear api rate limiting and quotas effectively. use when dealing
  with rate limit errors, implementing throttling, or optimizing api usage patterns.
  trigger with phrases like "linear rate limit", "linear throttling", "linear api
  quota", "li...
name: linear-rate-limits
---
# Linear Rate Limits

This skill provides automated assistance for linear rate limits tasks.

## Prerequisites
- Linear SDK configured
- Understanding of HTTP headers
- Familiarity with async patterns


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Rate limit monitoring
- Automatic retry with backoff
- Request queuing and throttling
- Batch processing utilities
- Optimized query patterns

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Linear Rate Limiting](https://developers.linear.app/docs/graphql/rate-limiting)
- [GraphQL Complexity](https://developers.linear.app/docs/graphql/complexity)
- [Best Practices](https://developers.linear.app/docs/graphql/best-practices)