---
allowed-tools: Read, Write, Edit, Bash
license: MIT
description: Implement deepgram callback and webhook handling for async transcription.
  use when implementing callback urls, processing async transcription results, or
  handling deepgram event notifications. trigger with phrases like "deepgram callback",
  "deepgr...
name: deepgram-webhooks-events
---
# Deepgram Webhooks Events

This skill provides automated assistance for deepgram webhooks events tasks.

## Prerequisites
- Publicly accessible HTTPS endpoint
- Deepgram API key with transcription permissions
- Request validation capabilities
- Secure storage for transcription results

## Instructions

### Step 1: Create Callback Endpoint
Set up an HTTPS endpoint to receive results.

### Step 2: Implement Request Validation
Verify callbacks are from Deepgram.

### Step 3: Process Results
Handle the transcription response.

### Step 4: Store and Notify
Save results and notify clients.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Deepgram Callback Documentation](https://developers.deepgram.com/docs/callback)
- [Webhook Best Practices](https://developers.deepgram.com/docs/webhook-best-practices)
- [ngrok Documentation](https://ngrok.com/docs)