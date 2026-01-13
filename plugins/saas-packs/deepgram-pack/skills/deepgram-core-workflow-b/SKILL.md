---
name: deepgram-core-workflow-b
license: MIT
allowed-tools: Read, Write, Edit, Bash, Grep
description: Implement real-time streaming transcription with deepgram. use when building
  live transcription, voice interfaces, or real-time audio processing applications.
  trigger with phrases like "deepgram streaming", "real-time transcription", "live
  transcr...
---
# Deepgram Core Workflow B: Real-time Streaming

## Overview
Implement real-time streaming transcription using Deepgram's WebSocket API for live audio processing.

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
| Error | Cause | Solution |
|-------|-------|----------|
| Connection Closed | Network interruption | Implement auto-reconnect |
| Buffer Overflow | Too much audio data | Reduce sample rate or chunk size |
| No Transcripts | Silent audio | Check audio levels and format |
| High Latency | Network/processing delay | Use interim results |

## Examples

### TypeScript WebSocket Client
```typescript
// services/live-transcription.ts
import { createClient, LiveTranscriptionEvents } from '@deepgram/sdk';

export interface LiveTranscriptionOptions {
  model?: 'nova-2' | 'nova' | 'enhanced' | 'base';
  language?: string;
  punctuate?: boolean;
  interimResults?: boolean;
  endpointing?: number;
  vadEvents?: boolean;
}

export class LiveTranscriptionService {
  private client;
  private connection: any = null;

  constructor(apiKey: string) {
    this.client = createClient(apiKey);
  }

  async start(
    options: LiveTranscriptionOptions = {},
    handlers: {
      onTranscript?: (transcript: string, isFinal: boolean) => void;
      onError?: (error: Error) => void;
      onClose?: () => void;
    } = {}
  ): Promise<void> {
    this.connection = this.client.listen.live({
      model: options.model || 'nova-2',
      language: options.language || 'en',
      punctuate: options.punctuate ?? true,
      interim_results: options.interimResults ?? true,
      endpointing: options.endpointing ?? 300,
      vad_events: options.vadEvents ?? true,
    });

    this.connection.on(LiveTranscriptionEvents.Open, () => {
      console.log('Deepgram connection opened');
    });

    this.connection.on(LiveTranscriptionEvents.Transcript, (data: any) => {
      const transcript = data.channel.alternatives[0].transcript;
      const isFinal = data.is_final;

      if (transcript && handlers.onTranscript) {
        handlers.onTranscript(transcript, isFinal);
      }
    });

    this.connection.on(LiveTranscriptionEvents.Error, (error: Error) => {
      console.error('Deepgram error:', error);
      handlers.onError?.(error);
    });

    this.connection.on(LiveTranscriptionEvents.Close, () => {
      console.log('Deepgram connection closed');
      handlers.onClose?.();
    });
  }

  send(audioData: Buffer): void {
    if (this.connection) {
      this.connection.send(audioData);
    }
  }

  async stop(): Promise<void> {
    if (this.connection) {
      this.connection.finish();
      this.connection = null;
    }
  }
}
```

### Browser Microphone Integration
```typescript
// services/microphone.ts
import { LiveTranscriptionService } from './live-transcription';

export async function startMicrophoneTranscription(
  onTranscript: (text: string, isFinal: boolean) => void
): Promise<{ stop: () => void }> {
  const service = new LiveTranscriptionService(process.env.DEEPGRAM_API_KEY!);

  // Get microphone access
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

  // Create audio context and processor
  const audioContext = new AudioContext({ sampleRate: 16000 });
  const source = audioContext.createMediaStreamSource(stream);
  const processor = audioContext.createScriptProcessor(4096, 1, 1);

  // Start transcription
  await service.start({
    model: 'nova-2',
    interimResults: true,
    punctuate: true,
  }, {
    onTranscript,
    onError: console.error,
  });

  // Process audio
  processor.onaudioprocess = (event) => {
    const inputData = event.inputBuffer.getChannelData(0);
    const pcmData = new Int16Array(inputData.length);

    for (let i = 0; i < inputData.length; i++) {
      pcmData[i] = Math.max(-32768, Math.min(32767, inputData[i] * 32768));
    }

    service.send(Buffer.from(pcmData.buffer));
  };

  source.connect(processor);
  processor.connect(audioContext.destination);

  return {
    stop: () => {
      processor.disconnect();
      source.disconnect();
      stream.getTracks().forEach(track => track.stop());
      service.stop();
    }
  };
}
```

### Node.js with Audio File Streaming
```typescript
// stream-file.ts
import { createReadStream } from 'fs';
import { LiveTranscriptionService } from './services/live-transcription';

async function streamAudioFile(filePath: string) {
  const service = new LiveTranscriptionService(process.env.DEEPGRAM_API_KEY!);

  const finalTranscripts: string[] = [];

  await service.start({
    model: 'nova-2',
    punctuate: true,
    interimResults: false,
  }, {
    onTranscript: (transcript, isFinal) => {
      if (isFinal) {
        finalTranscripts.push(transcript);
        console.log('Final:', transcript);
      }
    },
    onClose: () => {
      console.log('Complete transcript:', finalTranscripts.join(' '));
    },
  });

  // Stream file in chunks
  const stream = createReadStream(filePath, { highWaterMark: 4096 });

  for await (const chunk of stream) {
    service.send(chunk);
    // Pace the streaming to match real-time
    await new Promise(resolve => setTimeout(resolve, 100));
  }

  await service.stop();
}
```

### Python Streaming Example
```python
# services/live_transcription.py
from deepgram import DeepgramClient, LiveTranscriptionEvents, LiveOptions
import asyncio

class LiveTranscriptionService:
    def __init__(self, api_key: str):
        self.client = DeepgramClient(api_key)
        self.connection = None
        self.transcripts = []

    async def start(self, on_transcript=None):
        self.connection = self.client.listen.asynclive.v("1")

        async def on_message(self, result, **kwargs):
            transcript = result.channel.alternatives[0].transcript
            if transcript and on_transcript:
                on_transcript(transcript, result.is_final)

        async def on_error(self, error, **kwargs):
            print(f"Error: {error}")

        self.connection.on(LiveTranscriptionEvents.Transcript, on_message)
        self.connection.on(LiveTranscriptionEvents.Error, on_error)

        options = LiveOptions(
            model="nova-2",
            language="en",
            punctuate=True,
            interim_results=True,
        )

        await self.connection.start(options)

    def send(self, audio_data: bytes):
        if self.connection:
            self.connection.send(audio_data)

    async def stop(self):
        if self.connection:
            await self.connection.finish()
```

### Auto-Reconnect Pattern
```typescript
// services/resilient-live.ts
export class ResilientLiveTranscription {
  private service: LiveTranscriptionService;
  private reconnectAttempts = 0;
  private maxReconnectAttempts = 5;

  async connect(options: LiveTranscriptionOptions) {
    try {
      await this.service.start(options, {
        onClose: () => this.handleDisconnect(options),
        onError: (err) => console.error('Stream error:', err),
      });
      this.reconnectAttempts = 0;
    } catch (error) {
      await this.handleDisconnect(options);
    }
  }

  private async handleDisconnect(options: LiveTranscriptionOptions) {
    if (this.reconnectAttempts < this.maxReconnectAttempts) {
      this.reconnectAttempts++;
      const delay = Math.pow(2, this.reconnectAttempts) * 1000;
      console.log(`Reconnecting in ${delay}ms...`);
      await new Promise(r => setTimeout(r, delay));
      await this.connect(options);
    }
  }
}
```

## Resources
- [Deepgram Live Streaming API](https://developers.deepgram.com/docs/getting-started-with-live-streaming-audio)
- [WebSocket Events](https://developers.deepgram.com/docs/live-streaming-events)
- [Endpointing Configuration](https://developers.deepgram.com/docs/endpointing)

## Next Steps
Proceed to `deepgram-common-errors` for error handling patterns.
