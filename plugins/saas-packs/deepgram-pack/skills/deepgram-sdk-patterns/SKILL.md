---
name: deepgram-sdk-patterns
license: MIT
allowed-tools: Read, Write, Edit
description: Apply production-ready deepgram sdk patterns for typescript and python.
  use when implementing deepgram integrations, refactoring sdk usage, or establishing
  team coding standards for deepgram. trigger with phrases like "deepgram sdk patterns",
  "dee...
---
# Deepgram SDK Patterns

## Overview
Production-ready patterns for Deepgram SDK integration with proper error handling, typing, and structure.

## Prerequisites
- Completed `deepgram-install-auth` setup
- Familiarity with async/await patterns
- Understanding of error handling best practices

## Instructions

### Step 1: Create Type-Safe Client Singleton
Implement a singleton pattern for the Deepgram client.

### Step 2: Add Robust Error Handling
Wrap all API calls with proper error handling and logging.

### Step 3: Implement Response Validation
Validate API responses before processing.

### Step 4: Add Retry Logic
Implement exponential backoff for transient failures.

## Output
- Type-safe client singleton
- Robust error handling with structured logging
- Automatic retry with exponential backoff
- Runtime validation for API responses

## Error Handling
| Error | Cause | Solution |
|-------|-------|----------|
| Type Mismatch | Incorrect response shape | Add runtime validation |
| Client Undefined | Singleton not initialized | Call init() before use |
| Memory Leak | Multiple client instances | Use singleton pattern |
| Timeout | Large audio file | Increase timeout settings |

## Examples

### TypeScript Client Singleton
```typescript
// lib/deepgram.ts
import { createClient, DeepgramClient } from '@deepgram/sdk';

let client: DeepgramClient | null = null;

export function getDeepgramClient(): DeepgramClient {
  if (!client) {
    const apiKey = process.env.DEEPGRAM_API_KEY;
    if (!apiKey) {
      throw new Error('DEEPGRAM_API_KEY environment variable not set');
    }
    client = createClient(apiKey);
  }
  return client;
}

export function resetClient(): void {
  client = null;
}
```

### Typed Transcription Response
```typescript
// types/deepgram.ts
export interface TranscriptWord {
  word: string;
  start: number;
  end: number;
  confidence: number;
  punctuated_word?: string;
}

export interface TranscriptAlternative {
  transcript: string;
  confidence: number;
  words: TranscriptWord[];
}

export interface TranscriptChannel {
  alternatives: TranscriptAlternative[];
}

export interface TranscriptResult {
  results: {
    channels: TranscriptChannel[];
    utterances?: Array<{
      start: number;
      end: number;
      transcript: string;
      speaker: number;
    }>;
  };
  metadata: {
    request_id: string;
    model_uuid: string;
    model_info: Record<string, unknown>;
  };
}
```

### Error Handling Wrapper
```typescript
// lib/transcribe.ts
import { getDeepgramClient } from './deepgram';
import { TranscriptResult } from '../types/deepgram';

export class TranscriptionError extends Error {
  constructor(
    message: string,
    public readonly code: string,
    public readonly requestId?: string
  ) {
    super(message);
    this.name = 'TranscriptionError';
  }
}

export async function transcribeUrl(
  url: string,
  options: { model?: string; language?: string } = {}
): Promise<TranscriptResult> {
  const client = getDeepgramClient();

  try {
    const { result, error } = await client.listen.prerecorded.transcribeUrl(
      { url },
      {
        model: options.model || 'nova-2',
        language: options.language || 'en',
        smart_format: true,
        punctuate: true,
      }
    );

    if (error) {
      throw new TranscriptionError(
        error.message || 'Transcription failed',
        error.code || 'UNKNOWN_ERROR'
      );
    }

    return result as TranscriptResult;
  } catch (err) {
    if (err instanceof TranscriptionError) throw err;
    throw new TranscriptionError(
      err instanceof Error ? err.message : 'Unknown error',
      'NETWORK_ERROR'
    );
  }
}
```

### Retry with Exponential Backoff
```typescript
// lib/retry.ts
interface RetryOptions {
  maxRetries?: number;
  baseDelay?: number;
  maxDelay?: number;
}

export async function withRetry<T>(
  fn: () => Promise<T>,
  options: RetryOptions = {}
): Promise<T> {
  const { maxRetries = 3, baseDelay = 1000, maxDelay = 10000 } = options;

  let lastError: Error | undefined;

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error instanceof Error ? error : new Error(String(error));

      // Don't retry on auth errors
      if (lastError.message.includes('401') ||
          lastError.message.includes('403')) {
        throw lastError;
      }

      if (attempt < maxRetries) {
        const delay = Math.min(baseDelay * Math.pow(2, attempt), maxDelay);
        await new Promise(resolve => setTimeout(resolve, delay));
      }
    }
  }

  throw lastError;
}

// Usage
const result = await withRetry(() => transcribeUrl(audioUrl));
```

### Python Patterns
```python
# lib/deepgram_client.py
from deepgram import DeepgramClient, PrerecordedOptions
from functools import lru_cache
import os

@lru_cache(maxsize=1)
def get_deepgram_client() -> DeepgramClient:
    """Get or create Deepgram client singleton."""
    api_key = os.environ.get('DEEPGRAM_API_KEY')
    if not api_key:
        raise ValueError('DEEPGRAM_API_KEY environment variable not set')
    return DeepgramClient(api_key)

def transcribe_url(url: str, model: str = 'nova-2') -> dict:
    """Transcribe audio from URL with error handling."""
    client = get_deepgram_client()

    options = PrerecordedOptions(
        model=model,
        smart_format=True,
        punctuate=True,
    )

    try:
        response = client.listen.rest.v("1").transcribe_url(
            {"url": url},
            options
        )
        return response.to_dict()
    except Exception as e:
        raise TranscriptionError(str(e)) from e
```

## Resources
- [Deepgram SDK Reference](https://developers.deepgram.com/docs/sdk)
- [Deepgram TypeScript Types](https://github.com/deepgram/deepgram-js-sdk)
- [Error Handling Best Practices](https://developers.deepgram.com/docs/error-handling)

## Next Steps
Proceed to `deepgram-core-workflow-a` for speech-to-text workflow implementation.
