---
name: instantly-rate-limits
description: |
  Implement instantly rate limiting, backoff, and idempotency patterns. use when handling rate limit errors, implementing retry logic, or optimizing api request throughput for instantly. trigger with phrases like "instantly rate limit", "instantly t...
allowed-tools: Read, Write, Edit
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Instantly Rate Limits

This skill provides automated assistance for instantly rate limits tasks.

## Prerequisites
- Instantly SDK installed
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
- [Instantly Rate Limits](https://docs.instantly.com/rate-limits)
- [p-queue Documentation](https://github.com/sindresorhus/p-queue)