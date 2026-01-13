---
name: klingai-rate-limits
license: MIT
allowed-tools: Read, Write, Edit, Grep
description: Handle kling ai rate limits with proper backoff strategies. use when
  experiencing 429 errors or building high-throughput systems. trigger with phrases
  like 'klingai rate limit', 'kling ai 429', 'klingai throttle', 'klingai backoff'.
---
# Klingai Rate Limits

## Overview

This skill teaches rate limit handling patterns including exponential backoff, token bucket algorithms, request queuing, and concurrent job management for reliable Kling AI integrations.

## Prerequisites

- Kling AI integration
- Understanding of HTTP status codes
- Python 3.8+ or Node.js 18+

## Instructions

Follow these steps to handle rate limits:

1. **Understand Limits**: Know the rate limit structure
2. **Implement Detection**: Detect rate limit responses
3. **Add Backoff**: Implement exponential backoff
4. **Queue Requests**: Add request queuing
5. **Monitor Usage**: Track rate limit consumption

## Output

Successful execution produces:
- Rate limit handling without errors
- Smooth request throughput
- Proper backoff behavior
- Concurrent job management

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [Kling AI Rate Limits](https://docs.klingai.com/rate-limits)
- [Exponential Backoff](https://cloud.google.com/iot/docs/how-tos/exponential-backoff)
- [Token Bucket Algorithm](https://en.wikipedia.org/wiki/Token_bucket)
