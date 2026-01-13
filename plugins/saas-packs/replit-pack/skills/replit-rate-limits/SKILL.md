---
name: replit-rate-limits
description: |
  Implement replit rate limiting, backoff, and idempotency patterns. use when handling rate limit errors, implementing retry logic, or optimizing api request throughput for replit. trigger with phrases like "replit rate limit", "replit throttling", ...
allowed-tools: Read, Write, Edit
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Replit Rate Limits

This skill provides automated assistance for replit rate limits tasks.

## Prerequisites
- Replit SDK installed
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
- [Replit Rate Limits](https://docs.replit.com/rate-limits)
- [p-queue Documentation](https://github.com/sindresorhus/p-queue)