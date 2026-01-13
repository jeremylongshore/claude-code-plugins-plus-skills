---
name: supabase-rate-limits
description: |
  Implement supabase rate limiting, backoff, and idempotency patterns. use when handling rate limit errors, implementing retry logic, or optimizing api request throughput for supabase. trigger with phrases like "supabase rate limit", "supabase throt...
allowed-tools: Read, Write, Edit
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Supabase Rate Limits

This skill provides automated assistance for supabase rate limits tasks.

## Prerequisites
- Supabase SDK installed
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
- [Supabase Rate Limits](https://supabase.com/docs/rate-limits)
- [p-queue Documentation](https://github.com/sindresorhus/p-queue)