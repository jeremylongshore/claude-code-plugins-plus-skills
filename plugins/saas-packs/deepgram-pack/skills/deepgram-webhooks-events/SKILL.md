---
name: deepgram-webhooks-events
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Implement deepgram callback and webhook handling for async transcription.
  use when implementing callback urls, processing async transcription results, or
  handling deepgram event notifications. trigger with phrases like "deepgram callback",
  "deepgr...
---
# Deepgram Webhooks Events

## Overview
Implement callback URL handling for asynchronous Deepgram transcription workflows.

## Prerequisites
- Publicly accessible HTTPS endpoint
- Deepgram API key with transcription permissions
- Request validation capabilities
- Secure storage for transcription results

## Deepgram Callback Flow

1. Client sends transcription request with callback URL
2. Deepgram processes audio asynchronously
3. Deepgram POSTs results to callback URL
4. Your server processes and stores results

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

### TypeScript Callback Server (Express)
```typescript
// server/callback.ts
import express from 'express';
import crypto from 'crypto';
import { logger } from './logger';
import { storeTranscription, notifyClient } from './services';

const app = express();

// Raw body for signature verification
app.use('/webhooks/deepgram', express.raw({ type: 'application/json' }));
app.use(express.json());

interface DeepgramCallback {
  request_id: string;
  metadata: {
    request_id: string;
    transaction_key: string;
    sha256: string;
    created: string;
    duration: number;
    channels: number;
    models: string[];
  };
  results: {
    channels: Array<{
      alternatives: Array<{
        transcript: string;
        confidence: number;
        words: Array<{
          word: string;
          start: number;
          end: number;
          confidence: number;
        }>;
      }>;
    }>;
  };
}

// Verify callback is from Deepgram
function verifyDeepgramSignature(
  payload: Buffer,
  signature: string | undefined,
  secret: string
): boolean {
  if (!signature) return false;

  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');

  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );
}

app.post('/webhooks/deepgram', async (req, res) => {
  const requestId = req.headers['x-request-id'] as string;

  logger.info('Received Deepgram callback', { requestId });

  try {
    // Verify signature if using webhook secret
    const signature = req.headers['x-deepgram-signature'] as string;
    const webhookSecret = process.env.DEEPGRAM_WEBHOOK_SECRET;

    if (webhookSecret && !verifyDeepgramSignature(req.body, signature, webhookSecret)) {
      logger.warn('Invalid signature', { requestId });
      return res.status(401).json({ error: 'Invalid signature' });
    }

    const callback: DeepgramCallback = JSON.parse(req.body.toString());

    // Extract transcript
    const transcript = callback.results.channels[0]?.alternatives[0]?.transcript;
    const confidence = callback.results.channels[0]?.alternatives[0]?.confidence;

    logger.info('Processing transcription', {
      requestId: callback.request_id,
      duration: callback.metadata.duration,
      confidence,
    });

    // Store result
    await storeTranscription({
      requestId: callback.request_id,
      transcript,
      confidence,
      metadata: callback.metadata,
      words: callback.results.channels[0]?.alternatives[0]?.words,
    });

    // Notify client (WebSocket, email, etc.)
    await notifyClient(callback.request_id, {
      status: 'completed',
      transcript,
    });

    res.status(200).json({ received: true });
  } catch (error) {
    logger.error('Callback processing failed', {
      requestId,
      error: error instanceof Error ? error.message : 'Unknown error',
    });

    res.status(500).json({ error: 'Processing failed' });
  }
});

// Health check
app.get('/health', (_, res) => {
  res.json({ status: 'ok' });
});

export default app;
```

### Async Transcription Request
```typescript
// services/async-transcription.ts
import { createClient } from '@deepgram/sdk';
import { v4 as uuidv4 } from 'uuid';
import { redis } from './redis';

interface AsyncTranscriptionOptions {
  language?: string;
  model?: string;
  diarize?: boolean;
  punctuate?: boolean;
}

export class AsyncTranscriptionService {
  private client;
  private callbackBaseUrl: string;

  constructor(apiKey: string, callbackBaseUrl: string) {
    this.client = createClient(apiKey);
    this.callbackBaseUrl = callbackBaseUrl;
  }

  async submitTranscription(
    audioUrl: string,
    options: AsyncTranscriptionOptions = {}
  ): Promise<{ jobId: string; requestId: string }> {
    const jobId = uuidv4();
    const callbackUrl = `${this.callbackBaseUrl}/webhooks/deepgram?job=${jobId}`;

    const { result, error } = await this.client.listen.prerecorded.transcribeUrl(
      { url: audioUrl },
      {
        model: options.model || 'nova-2',
        language: options.language || 'en',
        diarize: options.diarize ?? false,
        punctuate: options.punctuate ?? true,
        smart_format: true,
        callback: callbackUrl,
      }
    );

    if (error) {
      throw new Error(`Transcription submission failed: ${error.message}`);
    }

    // Store job tracking info
    await redis.hset(`transcription:${jobId}`, {
      status: 'processing',
      requestId: result.request_id,
      submittedAt: new Date().toISOString(),
      audioUrl,
    });

    // Set expiration (24 hours)
    await redis.expire(`transcription:${jobId}`, 86400);

    return {
      jobId,
      requestId: result.request_id,
    };
  }

  async getStatus(jobId: string): Promise<{
    status: string;
    result?: unknown;
  }> {
    const data = await redis.hgetall(`transcription:${jobId}`);

    if (!data || Object.keys(data).length === 0) {
      throw new Error('Job not found');
    }

    return {
      status: data.status,
      result: data.result ? JSON.parse(data.result) : undefined,
    };
  }
}
```

### Store and Notify Services
```typescript
// services/store.ts
import { redis } from './redis';
import { db } from './database';

interface TranscriptionResult {
  requestId: string;
  transcript: string;
  confidence: number;
  metadata: Record<string, unknown>;
  words?: Array<{
    word: string;
    start: number;
    end: number;
    confidence: number;
  }>;
}

export async function storeTranscription(result: TranscriptionResult): Promise<void> {
  // Store in database
  await db.transcriptions.insert({
    request_id: result.requestId,
    transcript: result.transcript,
    confidence: result.confidence,
    metadata: result.metadata,
    words: result.words,
    created_at: new Date(),
  });

  // Update Redis for quick access
  const jobId = await redis.get(`request:${result.requestId}:job`);
  if (jobId) {
    await redis.hset(`transcription:${jobId}`, {
      status: 'completed',
      result: JSON.stringify(result),
      completedAt: new Date().toISOString(),
    });
  }
}

// services/notify.ts
import { WebSocketServer } from './websocket';
import { emailService } from './email';

export async function notifyClient(
  requestId: string,
  data: { status: string; transcript?: string }
): Promise<void> {
  // Get client info for this request
  const clientId = await redis.get(`request:${requestId}:client`);

  if (clientId) {
    // WebSocket notification
    WebSocketServer.sendToClient(clientId, {
      type: 'transcription_complete',
      requestId,
      ...data,
    });
  }

  // Email notification (optional)
  const email = await redis.get(`request:${requestId}:email`);
  if (email) {
    await emailService.send({
      to: email,
      subject: 'Your transcription is ready',
      body: `Transcription for request ${requestId} is complete.`,
    });
  }
}
```

### Retry Mechanism for Callbacks
```typescript
// services/callback-retry.ts
import { logger } from './logger';

interface RetryConfig {
  maxRetries: number;
  baseDelay: number;
  maxDelay: number;
}

export class CallbackRetryHandler {
  private config: RetryConfig;
  private pendingRetries: Map<string, NodeJS.Timeout> = new Map();

  constructor(config: Partial<RetryConfig> = {}) {
    this.config = {
      maxRetries: config.maxRetries ?? 3,
      baseDelay: config.baseDelay ?? 5000,
      maxDelay: config.maxDelay ?? 60000,
    };
  }

  async processWithRetry(
    requestId: string,
    processor: () => Promise<void>
  ): Promise<void> {
    let attempt = 0;

    while (attempt < this.config.maxRetries) {
      try {
        await processor();
        return;
      } catch (error) {
        attempt++;
        logger.warn('Callback processing failed, will retry', {
          requestId,
          attempt,
          error: error instanceof Error ? error.message : 'Unknown',
        });

        if (attempt >= this.config.maxRetries) {
          throw error;
        }

        const delay = Math.min(
          this.config.baseDelay * Math.pow(2, attempt - 1),
          this.config.maxDelay
        );

        await new Promise(resolve => setTimeout(resolve, delay));
      }
    }
  }

  scheduleRetry(requestId: string, callback: () => Promise<void>, attempt: number): void {
    const delay = Math.min(
      this.config.baseDelay * Math.pow(2, attempt),
      this.config.maxDelay
    );

    const timeout = setTimeout(async () => {
      try {
        await callback();
        this.pendingRetries.delete(requestId);
      } catch (error) {
        if (attempt < this.config.maxRetries) {
          this.scheduleRetry(requestId, callback, attempt + 1);
        } else {
          logger.error('Callback retry exhausted', { requestId });
        }
      }
    }, delay);

    this.pendingRetries.set(requestId, timeout);
  }

  cancel(requestId: string): void {
    const timeout = this.pendingRetries.get(requestId);
    if (timeout) {
      clearTimeout(timeout);
      this.pendingRetries.delete(requestId);
    }
  }
}
```

### Testing Callbacks Locally
```bash
# Use ngrok to expose local server
ngrok http 3000

# Test callback endpoint
curl -X POST https://your-ngrok-url.ngrok.io/webhooks/deepgram \
  -H "Content-Type: application/json" \
  -d '{
    "request_id": "test-123",
    "metadata": {
      "request_id": "test-123",
      "duration": 10.5
    },
    "results": {
      "channels": [{
        "alternatives": [{
          "transcript": "This is a test transcript.",
          "confidence": 0.95
        }]
      }]
    }
  }'
```

### Client SDK for Async Transcription
```typescript
// client/async-client.ts
export class AsyncTranscriptionClient {
  private baseUrl: string;
  private pollInterval: number;

  constructor(baseUrl: string, pollInterval = 2000) {
    this.baseUrl = baseUrl;
    this.pollInterval = pollInterval;
  }

  async submit(audioUrl: string): Promise<string> {
    const response = await fetch(`${this.baseUrl}/transcribe/async`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ audioUrl }),
    });

    const { jobId } = await response.json();
    return jobId;
  }

  async waitForResult(jobId: string, timeout = 300000): Promise<{
    transcript: string;
    confidence: number;
  }> {
    const startTime = Date.now();

    while (Date.now() - startTime < timeout) {
      const response = await fetch(`${this.baseUrl}/transcribe/status/${jobId}`);
      const data = await response.json();

      if (data.status === 'completed') {
        return data.result;
      }

      if (data.status === 'failed') {
        throw new Error('Transcription failed');
      }

      await new Promise(r => setTimeout(r, this.pollInterval));
    }

    throw new Error('Transcription timeout');
  }

  async transcribe(audioUrl: string): Promise<{
    transcript: string;
    confidence: number;
  }> {
    const jobId = await this.submit(audioUrl);
    return this.waitForResult(jobId);
  }
}
```

## Resources
- [Deepgram Callback Documentation](https://developers.deepgram.com/docs/callback)
- [Webhook Best Practices](https://developers.deepgram.com/docs/webhook-best-practices)
- [ngrok Documentation](https://ngrok.com/docs)

## Next Steps
Proceed to `deepgram-performance-tuning` for optimization.
