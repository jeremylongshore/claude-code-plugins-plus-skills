---
name: posthog-rate-limits
description: |
  Implement posthog rate limiting, backoff, and idempotency patterns. use when handling rate limit errors, implementing retry logic, or optimizing api request throughput for posthog. trigger with phrases like "posthog rate limit", "posthog throttlin...
allowed-tools: Read, Write, Edit
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Posthog Rate Limits

This skill provides automated assistance for posthog rate limits tasks.

## Prerequisites
- PostHog SDK installed
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
- [PostHog Rate Limits](https://docs.posthog.com/rate-limits)
- [p-queue Documentation](https://github.com/sindresorhus/p-queue)