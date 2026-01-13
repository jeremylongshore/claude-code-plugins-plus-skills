# Pattern 4: Hybrid Architecture

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