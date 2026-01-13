---
allowed-tools: Read, Write, Edit
license: MIT
description: Implement exa rate limiting, backoff, and idempotency patterns. use when
  handling rate limit errors, implementing retry logic, or optimizing api request
  throughput for exa. trigger with phrases like "exa rate limit", "exa throttling",
  "exa 429", "...
name: exa-rate-limits
---
# Exa Rate Limits

This skill provides automated assistance for exa rate limits tasks.

## Prerequisites
- Exa SDK installed
- Understanding of async/await patterns
- Access to rate limit headers


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Reliable API calls with automatic retry
- Idempotent requests preventing duplicates
- Rate limit headers properly handled

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Exa Rate Limits](https://docs.exa.com/rate-limits)
- [p-queue Documentation](https://github.com/sindresorhus/p-queue)