---
name: deepgram-core-workflow-b
description: |
  Implement real-time streaming transcription with deepgram. use when building live transcription, voice interfaces, or real-time audio processing applications. trigger with phrases like "deepgram streaming", "real-time transcription", "live transcr...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Deepgram Core Workflow B

This skill provides automated assistance for deepgram core workflow b tasks.

## Prerequisites
- Completed `deepgram-install-auth` setup
- Understanding of WebSocket patterns
- Audio input source (microphone or stream)

## Instructions

### Step 1: Set Up WebSocket Connection
Initialize a live transcription connection with Deepgram.

### Step 2: Configure Stream Options
Set up interim results, endpointing, and language options.

### Step 3: Handle Events
Implement handlers for transcript events and connection lifecycle.

### Step 4: Stream Audio Data
Send audio chunks to the WebSocket connection.

## Output
- Live transcription WebSocket client
- Event handlers for real-time results
- Audio streaming pipeline
- Graceful connection management

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources
- [Deepgram Live Streaming API](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio)
- [WebSocket Events](https://developers.deepgram.com/docs/live-streaming-events)
- [Endpointing Configuration](https://developers.deepgram.com/docs/endpointing)