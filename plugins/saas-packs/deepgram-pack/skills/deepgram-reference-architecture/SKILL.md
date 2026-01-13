---
name: deepgram-reference-architecture
description: |
  Implement Deepgram reference architecture for scalable transcription systems.
  Use when designing transcription pipelines, building production architectures,
  or planning Deepgram integration at scale.
  Trigger with phrases like "deepgram architecture", "transcription pipeline",
  "deepgram system design", "deepgram at scale", "enterprise deepgram".
allowed-tools: Read, Write, Edit, Bash
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Deepgram Reference Architecture

## Overview
Reference architectures for building scalable, production-ready transcription systems with Deepgram.

## Architecture Patterns

### 1. Synchronous API
Direct API calls for small files and low latency requirements.

### 2. Asynchronous Queue
Queue-based processing for batch workloads.

### 3. Real-time Streaming
WebSocket-based live transcription.

### 4. Hybrid Architecture
Combination of patterns for different use cases.

## Pattern 1: Synchronous API Architecture

```
+----------+     +------------+     +----------+
|  Client  | --> | API Server | --> | Deepgram |
+----------+     +------------+     +----------+
                       |
                       v
                 +-----------+
                 | Database  |
                 +-----------+
```

**Best for:**
- Short audio files (<60 seconds)
- Low latency requirements
- Simple integration

### Implementation
```typescript
// architecture/sync/server.ts
import express from 'express';
import { createClient } from '@deepgram/sdk';
import { db } from './database';

const app = express();
const deepgram = createClient(process.env.DEEPGRAM_API_KEY!);

app.post('/transcribe', async (req, res) => {
  const { audioUrl, userId } = req.body;

  try {
    const { result, error } = await deepgram.listen.prerecorded.transcribeUrl(
      { url: audioUrl },
      { model: 'nova-2', smart_format: true }
    );

    if (error) throw error;

    const transcript = result.results.channels[0].alternatives[0].transcript;

    // Store result
    await db.transcripts.create({
      userId,
      audioUrl,
      transcript,
      metadata: result.metadata,
    });

    res.json({ transcript, requestId: result.metadata.request_id });
  } catch (err) {
    res.status(500).json({ error: 'Transcription failed' });
  }
});
```

## Pattern 2: Asynchronous Queue Architecture

```
+----------+     +-------+     +--------+     +----------+
|  Client  | --> | Queue | --> | Worker | --> | Deepgram |
+----------+     +-------+     +--------+     +----------+
      ^                             |
      |                             v
      |                      +-----------+
      +----------------------| Database  |
            (poll/webhook)   +-----------+
```

**Best for:**
- Long audio files
- Batch processing
- High throughput

### Implementation
```typescript
// architecture/async/producer.ts
import { Queue } from 'bullmq';
import { v4 as uuidv4 } from 'uuid';
import { redis } from './redis';

const transcriptionQueue = new Queue('transcription', {
  connection: redis,
});

export async function submitTranscription(
  audioUrl: string,
  options: { priority?: number; userId?: string } = {}
): Promise<string> {
  const jobId = uuidv4();

  await transcriptionQueue.add(
    'transcribe',
    { audioUrl, userId: options.userId },
    {
      jobId,
      priority: options.priority ?? 0,
      attempts: 3,
      backoff: {
        type: 'exponential',
        delay: 5000,
      },
    }
  );

  return jobId;
}

// architecture/async/worker.ts
import { Worker, Job } from 'bullmq';
import { createClient } from '@deepgram/sdk';
import { db } from './database';
import { notifyClient } from './notifications';

const deepgram = createClient(process.env.DEEPGRAM_API_KEY!);

const worker = new Worker(
  'transcription',
  async (job: Job) => {
    const { audioUrl, userId } = job.data;

    const { result, error } = await deepgram.listen.prerecorded.transcribeUrl(
      { url: audioUrl },
      { model: 'nova-2', smart_format: true }
    );

    if (error) throw error;

    const transcript = result.results.channels[0].alternatives[0].transcript;

    await db.transcripts.create({
      jobId: job.id,
      userId,
      audioUrl,
      transcript,
      metadata: result.metadata,
    });

    await notifyClient(userId, {
      jobId: job.id,
      status: 'completed',
      transcript,
    });

    return { transcript };
  },
  {
    connection: redis,
    concurrency: 10,
  }
);

worker.on('completed', (job) => {
  console.log(`Job ${job.id} completed`);
});

worker.on('failed', (job, error) => {
  console.error(`Job ${job?.id} failed:`, error);
});
```

## Pattern 3: Real-time Streaming Architecture

```
+----------+     +-----------+     +----------+
|  Client  | <-> | WebSocket | <-> | Deepgram |
+----------+     |  Server   |     |   Live   |
                 +-----------+     +----------+
                       |
                       v
                 +-----------+
                 |  Storage  |
                 +-----------+
```

**Best for:**
- Live transcription
- Voice interfaces
- Real-time applications

### Implementation
```typescript
// architecture/streaming/server.ts
import { WebSocketServer, WebSocket } from 'ws';
import { createClient, LiveTranscriptionEvents } from '@deepgram/sdk';

const wss = new WebSocketServer({ port: 8080 });
const deepgram = createClient(process.env.DEEPGRAM_API_KEY!);

wss.on('connection', (clientWs: WebSocket) => {
  console.log('Client connected');

  // Create Deepgram connection
  const dgConnection = deepgram.listen.live({
    model: 'nova-2',
    smart_format: true,
    interim_results: true,
  });

  dgConnection.on(LiveTranscriptionEvents.Open, () => {
    console.log('Deepgram connected');
  });

  dgConnection.on(LiveTranscriptionEvents.Transcript, (data) => {
    clientWs.send(JSON.stringify({
      type: 'transcript',
      transcript: data.channel.alternatives[0].transcript,
      isFinal: data.is_final,
    }));
  });

  dgConnection.on(LiveTranscriptionEvents.Error, (error) => {
    clientWs.send(JSON.stringify({
      type: 'error',
      error: error.message,
    }));
  });

  // Forward audio from client to Deepgram
  clientWs.on('message', (data: Buffer) => {
    dgConnection.send(data);
  });

  clientWs.on('close', () => {
    dgConnection.finish();
    console.log('Client disconnected');
  });
});
```

## Pattern 4: Hybrid Architecture

```
                                +---------------+
                           +--> | Sync Handler  | --> Deepgram
                           |    +---------------+
+----------+     +-------+ |
|  Client  | --> | Router | |    +---------------+
+----------+     +-------+ +--> | Async Queue   | --> Worker --> Deepgram
                           |    +---------------+
                           |
                           |    +---------------+
                           +--> | Stream Handler| <-> Deepgram Live
                                +---------------+
```

### Implementation
```typescript
// architecture/hybrid/router.ts
import express from 'express';
import { syncHandler } from './handlers/sync';
import { asyncHandler } from './handlers/async';
import { streamHandler } from './handlers/stream';

const app = express();

// Route based on request characteristics
app.post('/transcribe', async (req, res) => {
  const { audioUrl, mode, audioDuration } = req.body;

  // Auto-select mode based on audio duration if not specified
  let selectedMode = mode;
  if (!selectedMode) {
    if (audioDuration && audioDuration < 60) {
      selectedMode = 'sync';
    } else if (audioDuration && audioDuration > 300) {
      selectedMode = 'async';
    } else {
      selectedMode = 'sync'; // default for unknown
    }
  }

  switch (selectedMode) {
    case 'sync':
      return syncHandler(req, res);
    case 'async':
      return asyncHandler(req, res);
    case 'stream':
      return streamHandler(req, res);
    default:
      return syncHandler(req, res);
  }
});
```

## Enterprise Architecture

```
                                    +------------------+
                                    |   Load Balancer  |
                                    +------------------+
                                            |
            +-------------------------------+-------------------------------+
            |                               |                               |
    +---------------+               +---------------+               +---------------+
    |  API Server   |               |  API Server   |               |  API Server   |
    |   (Region A)  |               |   (Region B)  |               |   (Region C)  |
    +---------------+               +---------------+               +---------------+
            |                               |                               |
            v                               v                               v
    +---------------+               +---------------+               +---------------+
    | Redis Cluster |<------------->| Redis Cluster |<------------->| Redis Cluster |
    +---------------+               +---------------+               +---------------+
            |                               |                               |
            v                               v                               v
    +---------------+               +---------------+               +---------------+
    | Worker Pool   |               | Worker Pool   |               | Worker Pool   |
    +---------------+               +---------------+               +---------------+
            |                               |                               |
            +-------------------------------+-------------------------------+
                                            |
                                    +------------------+
                                    |    Deepgram API  |
                                    +------------------+
```

### Enterprise Implementation
```typescript
// architecture/enterprise/config.ts
export const config = {
  regions: ['us-east-1', 'us-west-2', 'eu-west-1'],
  redis: {
    cluster: true,
    nodes: [
      { host: 'redis-us-east.example.com', port: 6379 },
      { host: 'redis-us-west.example.com', port: 6379 },
      { host: 'redis-eu-west.example.com', port: 6379 },
    ],
  },
  workers: {
    concurrency: 20,
    maxRetries: 5,
  },
  rateLimit: {
    maxRequestsPerMinute: 1000,
    maxConcurrent: 100,
  },
  monitoring: {
    metricsEndpoint: '/metrics',
    healthEndpoint: '/health',
    tracingEnabled: true,
  },
};

// architecture/enterprise/load-balancer.ts
import { Router } from 'express';
import { getHealthyRegion } from './health';
import { forwardRequest } from './proxy';

const router = Router();

router.use('/transcribe', async (req, res) => {
  // Find healthiest region
  const region = await getHealthyRegion();

  if (!region) {
    return res.status(503).json({ error: 'Service unavailable' });
  }

  // Forward request
  await forwardRequest(req, res, region);
});

export default router;
```

## Monitoring Architecture

```typescript
// architecture/monitoring/dashboard.ts
import { Registry, collectDefaultMetrics, Counter, Histogram, Gauge } from 'prom-client';

export const registry = new Registry();
collectDefaultMetrics({ register: registry });

// Metrics
export const requestsTotal = new Counter({
  name: 'transcription_requests_total',
  help: 'Total transcription requests',
  labelNames: ['status', 'model', 'region'],
  registers: [registry],
});

export const latencyHistogram = new Histogram({
  name: 'transcription_latency_seconds',
  help: 'Transcription latency',
  labelNames: ['model'],
  buckets: [0.5, 1, 2, 5, 10, 30, 60, 120],
  registers: [registry],
});

export const queueDepth = new Gauge({
  name: 'transcription_queue_depth',
  help: 'Number of jobs in queue',
  registers: [registry],
});

export const activeConnections = new Gauge({
  name: 'deepgram_active_connections',
  help: 'Active Deepgram connections',
  registers: [registry],
});
```

## Resources
- [Deepgram Architecture Guide](https://developers.deepgram.com/docs/architecture)
- [High Availability Patterns](https://developers.deepgram.com/docs/high-availability)
- [Scaling Best Practices](https://developers.deepgram.com/docs/scaling)

## Next Steps
Proceed to `deepgram-multi-env-setup` for multi-environment configuration.
