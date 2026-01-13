# Pattern 1: Synchronous Api Architecture

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