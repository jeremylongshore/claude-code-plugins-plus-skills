---
name: juicebox-rate-limits
description: |
  Implement juicebox rate limiting and backoff. use when handling api quotas, implementing retry logic, or optimizing request throughput. trigger with phrases like "juicebox rate limit", "juicebox quota", "juicebox throttling", "juicebox backoff".
allowed-tools: Read, Grep, Bash(cmd:*)
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Juicebox Rate Limits


See `{baseDir}/references/implementation.md` for detailed implementation guide.

## Output
- Rate limiter with queue
- Exponential backoff handler
- Quota tracking system
- Header parsing utilities

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Resources
- [Rate Limits Documentation](https://juicebox.ai/docs/rate-limits)
- [Quota Dashboard](https://app.juicebox.ai/usage)
