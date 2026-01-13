---
name: deepgram-performance-tuning
description: |
  Optimize Deepgram API performance for faster transcription and lower latency.
  Use when improving transcription speed, reducing latency,
  or optimizing audio processing pipelines.
  Trigger with phrases like "deepgram performance", "speed up deepgram",
  "optimize transcription", "deepgram latency", "deepgram faster".
allowed-tools: Read, Write, Edit, Bash
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Deepgram Performance Tuning

## Overview
Optimize Deepgram integration performance through audio preprocessing, connection management, and configuration tuning.

## Prerequisites
- Working Deepgram integration
- Performance monitoring in place
- Audio processing capabilities
- Baseline metrics established

## Performance Factors

| Factor | Impact | Optimization |
|--------|--------|--------------|
| Audio Format | High | Use optimal encoding |
| Sample Rate | Medium | Match model requirements |
| File Size | High | Stream large files |
| Model Choice | High | Balance accuracy vs speed |
| Network Latency | Medium | Use closest region |
| Concurrency | Medium | Manage connections |

## Instructions

### Step 1: Optimize Audio Format
Preprocess audio for optimal transcription.

### Step 2: Configure Connection Pooling
Reuse connections for better throughput.

### Step 3: Tune API Parameters
Select appropriate model and features.

### Step 4: Implement Streaming
Use streaming for real-time and large files.

## Examples

### Audio Preprocessing
```typescript
// lib/audio-optimizer.ts
import ffmpeg from 'fluent-ffmpeg';
import { Readable } from 'stream';

interface OptimizedAudio {
  buffer: Buffer;
  mimetype: string;
  sampleRate: number;
  channels: number;
  duration: number;
}

export async function optimizeAudio(inputPath: string): Promise<OptimizedAudio> {
  return new Promise((resolve, reject) => {
    const chunks: Buffer[] = [];

    // Optimal settings for Deepgram
    ffmpeg(inputPath)
      .audioCodec('pcm_s16le')      // 16-bit PCM
      .audioChannels(1)              // Mono
      .audioFrequency(16000)         // 16kHz (optimal for speech)
      .format('wav')
      .on('error', reject)
      .on('end', () => {
        const buffer = Buffer.concat(chunks);
        resolve({
          buffer,
          mimetype: 'audio/wav',
          sampleRate: 16000,
          channels: 1,
          duration: buffer.length / (16000 * 2), // 16-bit = 2 bytes
        });
      })
      .pipe()
      .on('data', (chunk: Buffer) => chunks.push(chunk));
  });
}

// For already loaded audio data
export async function optimizeAudioBuffer(
  audioBuffer: Buffer,
  inputFormat: string
): Promise<Buffer> {
  return new Promise((resolve, reject) => {
    const chunks: Buffer[] = [];
    const readable = new Readable();
    readable.push(audioBuffer);
    readable.push(null);

    ffmpeg(readable)
      .inputFormat(inputFormat)
      .audioCodec('pcm_s16le')
      .audioChannels(1)
      .audioFrequency(16000)
      .format('wav')
      .on('error', reject)
      .on('end', () => resolve(Buffer.concat(chunks)))
      .pipe()
      .on('data', (chunk: Buffer) => chunks.push(chunk));
  });
}
```

### Connection Pooling
```typescript
// lib/connection-pool.ts
import { createClient, DeepgramClient } from '@deepgram/sdk';

interface PoolConfig {
  minSize: number;
  maxSize: number;
  acquireTimeout: number;
  idleTimeout: number;
}

class DeepgramConnectionPool {
  private pool: DeepgramClient[] = [];
  private inUse: Set<DeepgramClient> = new Set();
  private waiting: Array<(client: DeepgramClient) => void> = [];
  private config: PoolConfig;
  private apiKey: string;

  constructor(apiKey: string, config: Partial<PoolConfig> = {}) {
    this.apiKey = apiKey;
    this.config = {
      minSize: config.minSize ?? 2,
      maxSize: config.maxSize ?? 10,
      acquireTimeout: config.acquireTimeout ?? 10000,
      idleTimeout: config.idleTimeout ?? 60000,
    };

    // Initialize minimum connections
    for (let i = 0; i < this.config.minSize; i++) {
      this.pool.push(createClient(this.apiKey));
    }
  }

  async acquire(): Promise<DeepgramClient> {
    // Try to get from pool
    if (this.pool.length > 0) {
      const client = this.pool.pop()!;
      this.inUse.add(client);
      return client;
    }

    // Create new if under max
    if (this.inUse.size < this.config.maxSize) {
      const client = createClient(this.apiKey);
      this.inUse.add(client);
      return client;
    }

    // Wait for available connection
    return new Promise((resolve, reject) => {
      const timeout = setTimeout(() => {
        const index = this.waiting.indexOf(resolve);
        if (index > -1) this.waiting.splice(index, 1);
        reject(new Error('Connection acquire timeout'));
      }, this.config.acquireTimeout);

      this.waiting.push((client) => {
        clearTimeout(timeout);
        resolve(client);
      });
    });
  }

  release(client: DeepgramClient): void {
    this.inUse.delete(client);

    if (this.waiting.length > 0) {
      const waiter = this.waiting.shift()!;
      this.inUse.add(client);
      waiter(client);
    } else {
      this.pool.push(client);
    }
  }

  async execute<T>(fn: (client: DeepgramClient) => Promise<T>): Promise<T> {
    const client = await this.acquire();
    try {
      return await fn(client);
    } finally {
      this.release(client);
    }
  }

  getStats() {
    return {
      poolSize: this.pool.length,
      inUse: this.inUse.size,
      waiting: this.waiting.length,
    };
  }
}

export const pool = new DeepgramConnectionPool(process.env.DEEPGRAM_API_KEY!);
```

### Streaming for Large Files
```typescript
// lib/streaming-transcription.ts
import { createClient } from '@deepgram/sdk';
import { createReadStream, statSync } from 'fs';

interface StreamingOptions {
  chunkSize: number;
  model: string;
}

export async function streamLargeFile(
  filePath: string,
  options: Partial<StreamingOptions> = {}
): Promise<string> {
  const { chunkSize = 1024 * 1024, model = 'nova-2' } = options;
  const client = createClient(process.env.DEEPGRAM_API_KEY!);

  const fileSize = statSync(filePath).size;
  const transcripts: string[] = [];

  // Use live transcription for streaming
  const connection = client.listen.live({
    model,
    smart_format: true,
    punctuate: true,
  });

  return new Promise((resolve, reject) => {
    connection.on('open', () => {
      const stream = createReadStream(filePath, { highWaterMark: chunkSize });

      stream.on('data', (chunk: Buffer) => {
        connection.send(chunk);
      });

      stream.on('end', () => {
        connection.finish();
      });

      stream.on('error', reject);
    });

    connection.on('transcript', (data) => {
      if (data.is_final) {
        transcripts.push(data.channel.alternatives[0].transcript);
      }
    });

    connection.on('close', () => {
      resolve(transcripts.join(' '));
    });

    connection.on('error', reject);
  });
}
```

### Model Selection for Speed
```typescript
// lib/model-selector.ts
interface ModelConfig {
  name: string;
  accuracy: 'high' | 'medium' | 'low';
  speed: 'fast' | 'medium' | 'slow';
  costPerMinute: number;
}

const models: Record<string, ModelConfig> = {
  'nova-2': {
    name: 'Nova-2',
    accuracy: 'high',
    speed: 'fast',
    costPerMinute: 0.0043,
  },
  'nova': {
    name: 'Nova',
    accuracy: 'high',
    speed: 'fast',
    costPerMinute: 0.0043,
  },
  'enhanced': {
    name: 'Enhanced',
    accuracy: 'medium',
    speed: 'fast',
    costPerMinute: 0.0145,
  },
  'base': {
    name: 'Base',
    accuracy: 'low',
    speed: 'fast',
    costPerMinute: 0.0048,
  },
};

export function selectModel(requirements: {
  prioritize: 'accuracy' | 'speed' | 'cost';
  minAccuracy?: 'high' | 'medium' | 'low';
}): string {
  const { prioritize, minAccuracy = 'low' } = requirements;

  const accuracyOrder = ['high', 'medium', 'low'];
  const minAccuracyIndex = accuracyOrder.indexOf(minAccuracy);

  const eligible = Object.entries(models).filter(([_, config]) =>
    accuracyOrder.indexOf(config.accuracy) <= minAccuracyIndex
  );

  if (prioritize === 'accuracy') {
    return eligible.reduce((best, [name, config]) =>
      accuracyOrder.indexOf(config.accuracy) < accuracyOrder.indexOf(models[best].accuracy)
        ? name : best
    , eligible[0][0]);
  }

  if (prioritize === 'cost') {
    return eligible.reduce((best, [name, config]) =>
      config.costPerMinute < models[best].costPerMinute ? name : best
    , eligible[0][0]);
  }

  // Default: balance speed and accuracy
  return 'nova-2';
}
```

### Parallel Processing
```typescript
// lib/parallel-transcription.ts
import { pool } from './connection-pool';
import pLimit from 'p-limit';

interface TranscriptionResult {
  file: string;
  transcript: string;
  duration: number;
}

export async function transcribeMultiple(
  audioUrls: string[],
  concurrency = 5
): Promise<TranscriptionResult[]> {
  const limit = pLimit(concurrency);
  const startTime = Date.now();

  const results = await Promise.all(
    audioUrls.map((url, index) =>
      limit(async () => {
        const itemStart = Date.now();

        const result = await pool.execute(async (client) => {
          const { result, error } = await client.listen.prerecorded.transcribeUrl(
            { url },
            { model: 'nova-2', smart_format: true }
          );

          if (error) throw error;
          return result;
        });

        return {
          file: url,
          transcript: result.results.channels[0].alternatives[0].transcript,
          duration: Date.now() - itemStart,
        };
      })
    )
  );

  console.log(`Processed ${audioUrls.length} files in ${Date.now() - startTime}ms`);
  console.log(`Average per file: ${(Date.now() - startTime) / audioUrls.length}ms`);

  return results;
}
```

### Caching Results
```typescript
// lib/transcription-cache.ts
import { createHash } from 'crypto';
import { redis } from './redis';

interface CacheOptions {
  ttl: number; // seconds
}

export class TranscriptionCache {
  private ttl: number;

  constructor(options: Partial<CacheOptions> = {}) {
    this.ttl = options.ttl ?? 3600; // 1 hour default
  }

  private getCacheKey(audioUrl: string, options: Record<string, unknown>): string {
    const hash = createHash('sha256')
      .update(JSON.stringify({ audioUrl, options }))
      .digest('hex');
    return `transcription:${hash}`;
  }

  async get(
    audioUrl: string,
    options: Record<string, unknown>
  ): Promise<string | null> {
    const key = this.getCacheKey(audioUrl, options);
    return redis.get(key);
  }

  async set(
    audioUrl: string,
    options: Record<string, unknown>,
    transcript: string
  ): Promise<void> {
    const key = this.getCacheKey(audioUrl, options);
    await redis.setex(key, this.ttl, transcript);
  }

  async transcribeWithCache(
    transcribeFn: () => Promise<string>,
    audioUrl: string,
    options: Record<string, unknown>
  ): Promise<{ transcript: string; cached: boolean }> {
    const cached = await this.get(audioUrl, options);
    if (cached) {
      return { transcript: cached, cached: true };
    }

    const transcript = await transcribeFn();
    await this.set(audioUrl, options, transcript);

    return { transcript, cached: false };
  }
}
```

### Performance Metrics
```typescript
// lib/performance-metrics.ts
import { Histogram, Counter, Gauge } from 'prom-client';

export const transcriptionLatency = new Histogram({
  name: 'deepgram_transcription_latency_seconds',
  help: 'Latency of transcription requests',
  labelNames: ['model', 'status'],
  buckets: [0.5, 1, 2, 5, 10, 30, 60],
});

export const audioDuration = new Histogram({
  name: 'deepgram_audio_duration_seconds',
  help: 'Duration of audio files processed',
  buckets: [10, 30, 60, 120, 300, 600, 1800],
});

export const processingRatio = new Gauge({
  name: 'deepgram_processing_ratio',
  help: 'Ratio of processing time to audio duration',
  labelNames: ['model'],
});

export function measureTranscription(
  audioDurationSec: number,
  processingTimeSec: number,
  model: string
) {
  audioDuration.observe(audioDurationSec);
  processingRatio.labels(model).set(processingTimeSec / audioDurationSec);
}
```

## Resources
- [Deepgram Performance Guide](https://developers.deepgram.com/docs/performance-guide)
- [Audio Format Best Practices](https://developers.deepgram.com/docs/audio-best-practices)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)

## Next Steps
Proceed to `deepgram-cost-tuning` for cost optimization.
