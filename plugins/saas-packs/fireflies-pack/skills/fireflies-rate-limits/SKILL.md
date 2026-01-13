---
name: fireflies-rate-limits
description: |
  Implement fireflies.ai rate limiting, backoff, and idempotency patterns. use when handling rate limit errors, implementing retry logic, or optimizing api request throughput for fireflies.ai. trigger with phrases like "fireflies rate limit", "firef...
allowed-tools: Read, Write, Edit
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Fireflies Rate Limits

This skill provides automated assistance for fireflies rate limits tasks.

## Prerequisites
- Fireflies.ai SDK installed
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
- [Fireflies.ai Rate Limits](https://docs.fireflies.com/rate-limits)
- [p-queue Documentation](https://github.com/sindresorhus/p-queue)