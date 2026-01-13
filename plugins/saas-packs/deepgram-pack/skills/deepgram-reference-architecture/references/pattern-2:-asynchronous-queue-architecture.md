# Pattern 2: Asynchronous Queue Architecture

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