# Incident: Deepgram Service Outage

## Incident: Deepgram Service Outage

**Status:** Investigating
**Severity:** SEV1
**Started:** [TIME]
**Impact:** All transcription services unavailable

### Summary
We are experiencing a complete outage of our transcription service due to
Deepgram API unavailability.

### Current Actions
- [ ] Verified Deepgram status page shows incident
- [ ] Contacted Deepgram support
- [ ] Activated fallback queueing
- [ ] Notified affected customers

### Next Update
In 15 minutes or when status changes.
```

### SEV2: Major Degradation

**Symptoms:**
- 50%+ error rate
- Intermittent failures
- Significantly elevated latency

**Investigation Steps:**
```typescript
// scripts/investigate-degradation.ts
import { createClient } from '@deepgram/sdk';
import { logger } from './logger';

async function investigateDegradation() {
  const client = createClient(process.env.DEEPGRAM_API_KEY!);
  const testUrls = [
    'https://static.deepgram.com/examples/nasa-podcast.wav',
    'https://your-test-audio.com/sample1.wav',
    'https://your-test-audio.com/sample2.wav',
  ];

  console.log('Testing transcription across multiple samples...\n');

  const results = await Promise.allSettled(
    testUrls.map(async (url) => {
      const startTime = Date.now();
      const { result, error } = await client.listen.prerecorded.transcribeUrl(
        { url },
        { model: 'nova-2' }
      );

      return {
        url,
        success: !error,
        latency: Date.now() - startTime,
        error: error?.message,
        requestId: result?.metadata?.request_id,
      };
    })
  );

  // Analyze results
  const successful = results.filter(r => r.status === 'fulfilled' && r.value.success);
  const failed = results.filter(r => r.status === 'rejected' || !r.value?.success);

  console.log(`Success: ${successful.length}/${results.length}`);
  console.log(`Failed: ${failed.length}/${results.length}`);

  if (failed.length > 0) {
    console.log('\nFailed requests:');
    failed.forEach(f => {
      if (f.status === 'fulfilled') {
        console.log(`  - ${f.value.url}: ${f.value.error}`);
      } else {
        console.log(`  - Exception: ${f.reason}`);
      }
    });
  }

  // Check if it's a specific model or feature
  console.log('\nTesting different models...');
  for (const model of ['nova-2', 'nova', 'base']) {
    const { error } = await client.listen.prerecorded.transcribeUrl(
      { url: testUrls[0] },
      { model }
    );
    console.log(`  ${model}: ${error ? 'FAIL' : 'OK'}`);
  }
}

investigateDegradation().catch(console.error);
```

**Mitigation Options:**
1. Reduce request rate
2. Disable non-critical features
3. Switch to simpler model
4. Enable request retries

### SEV3: Minor Degradation

**Symptoms:**
- Elevated latency (2-3x normal)
- Occasional timeouts
- Reduced throughput

**Actions:**
```typescript
// Enable graceful degradation
const gracefulConfig = {
  // Increase timeouts
  timeout: 60000, // 60s instead of 30s

  // Enable aggressive retry
  retryConfig: {
    maxRetries: 5,
    baseDelay: 2000,
    maxDelay: 30000,
  },

  // Use simpler model for faster processing
  model: 'nova', // Instead of nova-2

  // Disable expensive features
  features: {
    diarization: false,
    smartFormat: true, // Keep basic formatting
  },
};
```

### Post-Incident Review

```markdown