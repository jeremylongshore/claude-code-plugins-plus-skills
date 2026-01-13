# Pattern 3: Real-Time Streaming Architecture

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