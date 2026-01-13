---
allowed-tools: Read, Write, Edit
license: MIT
description: Implement retell ai rate limiting, backoff, and idempotency patterns.
  use when handling rate limit errors, implementing retry logic, or optimizing api
  request throughput for retell ai. trigger with phrases like "retellai rate limit",
  "retellai thr...
name: retellai-rate-limits
---
# Retellai Rate Limits

This skill provides automated assistance for retellai rate limits tasks.

## Prerequisites
- Retell AI SDK installed
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
- [Retell AI Rate Limits](https://docs.retellai.com/rate-limits)
- [p-queue Documentation](https://github.com/sindresorhus/p-queue)