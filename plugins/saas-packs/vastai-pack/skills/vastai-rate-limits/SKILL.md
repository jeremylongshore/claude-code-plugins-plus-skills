---
allowed-tools: Read, Write, Edit
license: MIT
description: Implement vast.ai rate limiting, backoff, and idempotency patterns. use
  when handling rate limit errors, implementing retry logic, or optimizing api request
  throughput for vast.ai. trigger with phrases like "vastai rate limit", "vastai throttling"...
name: vastai-rate-limits
---
# Vastai Rate Limits

This skill provides automated assistance for vastai rate limits tasks.

## Prerequisites
- Vast.ai SDK installed
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
- [Vast.ai Rate Limits](https://docs.vastai.com/rate-limits)
- [p-queue Documentation](https://github.com/sindresorhus/p-queue)