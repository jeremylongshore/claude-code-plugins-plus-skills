---
name: apollo-rate-limits
description: |
  Implement apollo.io rate limiting and backoff. use when handling rate limits, implementing retry logic, or optimizing api request throughput. trigger with phrases like "apollo rate limit", "apollo 429", "apollo throttling", "apollo backoff", "apol...
allowed-tools: Read, Grep, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Apollo Rate Limits

This skill provides automated assistance for apollo rate limits tasks.

## Output
- Rate limiter class with token bucket algorithm
- Exponential backoff with jitter
- Request queue with concurrency control
- Priority-based request scheduling
- Rate limit monitoring and alerts

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Apollo Rate Limits](https://apolloio.github.io/apollo-api-docs/#rate-limits)
- [p-queue Library](https://github.com/sindresorhus/p-queue)
- [Exponential Backoff](https://cloud.google.com/storage/docs/exponential-backoff)