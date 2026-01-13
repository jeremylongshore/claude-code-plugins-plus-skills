---
allowed-tools: Read, Write, Edit
license: MIT
description: Implement perplexity rate limiting, backoff, and idempotency patterns.
  use when handling rate limit errors, implementing retry logic, or optimizing api
  request throughput for perplexity. trigger with phrases like "perplexity rate limit",
  "perplexi...
name: perplexity-rate-limits
---
# Perplexity Rate Limits

This skill provides automated assistance for perplexity rate limits tasks.

## Prerequisites
- Perplexity SDK installed
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
- [Perplexity Rate Limits](https://docs.perplexity.com/rate-limits)
- [p-queue Documentation](https://github.com/sindresorhus/p-queue)