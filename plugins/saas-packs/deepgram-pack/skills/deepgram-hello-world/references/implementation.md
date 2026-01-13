# Implementation Guide

### Step 1: Create Entry File
Create a new file for your hello world example.

### Step 2: Import and Initialize Client
```typescript
import { createClient } from '@deepgram/sdk';

const deepgram = createClient(process.env.DEEPGRAM_API_KEY);
```

### Step 3: Transcribe Audio from URL
```typescript
async function transcribe() {
  const { result, error } = await deepgram.listen.prerecorded.transcribeUrl(
    { url: 'https://static.deepgram.com/examples/nasa-podcast.wav' },
    { model: 'nova-2', smart_format: true }
  );

  if (error) throw error;
  console.log(result.results.channels[0].alternatives[0].transcript);
}

transcribe();
```