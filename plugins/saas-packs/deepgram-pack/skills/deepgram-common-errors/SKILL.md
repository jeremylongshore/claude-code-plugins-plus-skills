---
name: deepgram-common-errors
description: |
  Diagnose and fix common Deepgram errors and issues.
  Use when troubleshooting Deepgram API errors, debugging transcription failures,
  or resolving integration issues.
  Trigger with phrases like "deepgram error", "deepgram not working",
  "fix deepgram", "deepgram troubleshoot", "transcription failed".
allowed-tools: Read, Grep, Bash
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Deepgram Common Errors

## Overview
Comprehensive guide to diagnosing and fixing common Deepgram integration errors.

## Quick Diagnostic
```bash
# Test API connectivity
curl -X POST 'https://api.deepgram.com/v1/listen?model=nova-2' \
  -H "Authorization: Token $DEEPGRAM_API_KEY" \
  -H "Content-Type: audio/wav" \
  --data-binary @test.wav
```

## Common Errors

### Authentication Errors

#### 401 Unauthorized
```json
{"err_code": "INVALID_AUTH", "err_msg": "Invalid credentials"}
```

**Causes:**
- Missing or invalid API key
- Expired API key
- Incorrect Authorization header format

**Solutions:**
```bash
# Check API key is set
echo $DEEPGRAM_API_KEY

# Verify API key format (should start with valid prefix)
# Test with curl
curl -X GET 'https://api.deepgram.com/v1/projects' \
  -H "Authorization: Token $DEEPGRAM_API_KEY"
```

#### 403 Forbidden
```json
{"err_code": "ACCESS_DENIED", "err_msg": "Access denied"}
```

**Causes:**
- API key lacks required permissions
- Feature not enabled on account
- IP restriction blocking request

**Solutions:**
- Check API key permissions in Console
- Verify account tier supports requested feature
- Check IP allowlist settings

### Audio Processing Errors

#### 400 Bad Request - Invalid Audio
```json
{"err_code": "BAD_REQUEST", "err_msg": "Audio could not be processed"}
```

**Causes:**
- Corrupted audio file
- Unsupported audio format
- Empty or silent audio
- Wrong Content-Type header

**Solutions:**
```typescript
// Validate audio before sending
import { createClient } from '@deepgram/sdk';
import { readFileSync, statSync } from 'fs';

function validateAudioFile(filePath: string): boolean {
  const stats = statSync(filePath);

  // Check file size (minimum 100 bytes, maximum 2GB)
  if (stats.size < 100 || stats.size > 2 * 1024 * 1024 * 1024) {
    console.error('Invalid file size');
    return false;
  }

  // Check file header for valid audio format
  const buffer = readFileSync(filePath, { length: 12 });
  const header = buffer.toString('hex', 0, 4);

  const validHeaders = {
    '52494646': 'WAV',   // RIFF
    'fff3': 'MP3',       // MP3
    'fff2': 'MP3',
    'fffb': 'MP3',
    '664c6143': 'FLAC',  // fLaC
    '4f676753': 'OGG',   // OggS
  };

  return Object.keys(validHeaders).some(h => header.startsWith(h));
}
```

#### 413 Payload Too Large
```json
{"err_code": "PAYLOAD_TOO_LARGE", "err_msg": "Audio file exceeds size limit"}
```

**Solutions:**
```typescript
// Split large files
import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

async function splitAudio(inputPath: string, chunkDuration: number = 300) {
  const outputPattern = inputPath.replace('.wav', '_chunk_%03d.wav');

  await execAsync(
    `ffmpeg -i ${inputPath} -f segment -segment_time ${chunkDuration} ` +
    `-c copy ${outputPattern}`
  );
}
```

### Rate Limiting Errors

#### 429 Too Many Requests
```json
{"err_code": "RATE_LIMIT_EXCEEDED", "err_msg": "Rate limit exceeded"}
```

**Solutions:**
```typescript
// Implement rate limiting
class RateLimiter {
  private queue: Array<() => Promise<void>> = [];
  private processing = false;
  private lastRequest = 0;
  private minInterval = 100; // ms between requests

  async add<T>(fn: () => Promise<T>): Promise<T> {
    return new Promise((resolve, reject) => {
      this.queue.push(async () => {
        const now = Date.now();
        const elapsed = now - this.lastRequest;

        if (elapsed < this.minInterval) {
          await new Promise(r => setTimeout(r, this.minInterval - elapsed));
        }

        try {
          this.lastRequest = Date.now();
          resolve(await fn());
        } catch (error) {
          reject(error);
        }
      });

      this.process();
    });
  }

  private async process() {
    if (this.processing) return;
    this.processing = true;

    while (this.queue.length > 0) {
      const fn = this.queue.shift()!;
      await fn();
    }

    this.processing = false;
  }
}
```

### WebSocket Errors

#### Connection Refused
```
Error: WebSocket connection failed
```

**Causes:**
- Firewall blocking WebSocket
- Incorrect URL
- Network issues

**Solutions:**
```typescript
// Test WebSocket connectivity
async function testWebSocketConnection() {
  const ws = new WebSocket('wss://api.deepgram.com/v1/listen', {
    headers: {
      Authorization: `Token ${process.env.DEEPGRAM_API_KEY}`,
    },
  });

  return new Promise((resolve, reject) => {
    ws.onopen = () => {
      console.log('WebSocket connected');
      ws.close();
      resolve(true);
    };

    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
      reject(error);
    };

    setTimeout(() => reject(new Error('Connection timeout')), 10000);
  });
}
```

#### Connection Dropped
```
Error: WebSocket closed unexpectedly
```

**Solutions:**
```typescript
// Implement keep-alive
class DeepgramWebSocket {
  private keepAliveInterval: NodeJS.Timeout | null = null;

  start() {
    // Send keep-alive every 10 seconds
    this.keepAliveInterval = setInterval(() => {
      if (this.connection?.readyState === WebSocket.OPEN) {
        this.connection.send(JSON.stringify({ type: 'KeepAlive' }));
      }
    }, 10000);
  }

  stop() {
    if (this.keepAliveInterval) {
      clearInterval(this.keepAliveInterval);
    }
  }
}
```

### Transcription Quality Issues

#### Empty or Incorrect Transcripts

**Diagnostic Steps:**
1. Check audio sample rate (16kHz recommended)
2. Verify audio is mono or stereo
3. Test with known-good audio file
4. Check language setting matches audio

```typescript
// Debug transcription
async function debugTranscription(audioPath: string) {
  const client = createClient(process.env.DEEPGRAM_API_KEY!);

  const { result, error } = await client.listen.prerecorded.transcribeFile(
    readFileSync(audioPath),
    {
      model: 'nova-2',
      smart_format: true,
      // Enable all debug features
      alternatives: 3,
      words: true,
      utterances: true,
    }
  );

  if (error) {
    console.error('Error:', error);
    return;
  }

  // Check confidence scores
  const alt = result.results.channels[0].alternatives[0];
  console.log('Confidence:', alt.confidence);
  console.log('Word count:', alt.words?.length);
  console.log('Low confidence words:', alt.words?.filter(w => w.confidence < 0.7));
}
```

## Error Reference Table

| HTTP Code | Error Code | Common Cause | Solution |
|-----------|------------|--------------|----------|
| 400 | BAD_REQUEST | Invalid audio format | Check audio encoding |
| 401 | INVALID_AUTH | Missing/invalid API key | Verify API key |
| 403 | ACCESS_DENIED | Permission denied | Check account permissions |
| 404 | NOT_FOUND | Invalid endpoint | Check API URL |
| 413 | PAYLOAD_TOO_LARGE | File too large | Split audio file |
| 429 | RATE_LIMIT_EXCEEDED | Too many requests | Implement backoff |
| 500 | INTERNAL_ERROR | Server error | Retry with backoff |
| 503 | SERVICE_UNAVAILABLE | Service down | Check status page |

## Resources
- [Deepgram Error Codes](https://developers.deepgram.com/docs/error-handling)
- [Deepgram Status Page](https://status.deepgram.com)
- [Deepgram Support](https://developers.deepgram.com/support)

## Next Steps
Proceed to `deepgram-debug-bundle` for collecting debug evidence.
