---
allowed-tools: Read, Grep, Bash
license: MIT
description: Implement deepgram rate limiting and backoff strategies. use when handling
  api quotas, implementing request throttling, or dealing with rate limit errors.
  trigger with phrases like "deepgram rate limit", "deepgram throttling", "429 error
  deepgram"...
name: deepgram-rate-limits
---
# Deepgram Rate Limits

This skill provides automated assistance for deepgram rate limits tasks.

## Instructions

### Step 1: Implement Request Queue
Create a queue to manage concurrent request limits.

### Step 2: Add Exponential Backoff
Handle rate limit responses with intelligent retry.

### Step 3: Monitor Usage
Track request counts and audio duration.

### Step 4: Implement Circuit Breaker
Prevent cascade failures during rate limiting.

## Output
- Rate-limited request queue
- Exponential backoff handler
- Usage monitoring dashboard
- Circuit breaker implementation

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Deepgram Pricing & Limits](https://deepgram.com/pricing)
- [Rate Limiting Best Practices](https://developers.deepgram.com/docs/rate-limits)
- [API Usage Dashboard](https://console.deepgram.com/usage)