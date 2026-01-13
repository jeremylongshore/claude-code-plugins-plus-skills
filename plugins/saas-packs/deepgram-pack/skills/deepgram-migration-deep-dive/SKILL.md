---
name: deepgram-migration-deep-dive
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Deep dive into complex deepgram migrations and provider transitions.
  use when migrating from other transcription providers, planning large-scale migrations,
  or implementing phased rollout strategies. trigger with phrases like "deepgram migration",...
---
# Deepgram Migration Deep Dive

## Overview
Comprehensive guide for migrating to Deepgram from other transcription providers or legacy systems.

## Common Migration Sources

| Source Provider | Complexity | Key Differences |
|-----------------|------------|-----------------|
| AWS Transcribe | Medium | Async-first vs sync options |
| Google Cloud STT | Medium | Different model naming |
| Azure Speech | Medium | Authentication model |
| OpenAI Whisper | Low | Self-hosted vs API |
| Rev.ai | Low | Similar API structure |
| AssemblyAI | Low | Similar feature set |

## Migration Strategy

### Phase 1: Assessment
- Audit current usage
- Map features to Deepgram equivalents
- Estimate costs
- Plan timeline

### Phase 2: Parallel Running
- Run both providers simultaneously
- Compare results
- Build confidence

### Phase 3: Gradual Rollout
- Shift traffic incrementally
- Monitor quality
- Address issues

### Phase 4: Cutover
- Complete migration
- Decommission old provider
- Documentation update

## Implementation

### Migration Adapter Pattern
```typescript
// adapters/transcription-adapter.ts
export interface TranscriptionResult {
  transcript: string;
  confidence: number;
  words?: Array<{
    word: string;
    start: number;
    end: number;
    confidence: number;
  }>;
  speakers?: Array<{
    speaker: number;
    start: number;
    end: number;
  }>;
  language?: string;
  provider: string;
}

export interface TranscriptionOptions {
  language?: string;
  diarization?: boolean;
  punctuation?: boolean;
  profanityFilter?: boolean;
}

export interface TranscriptionAdapter {
  name: string;
  transcribe(
    audioUrl: string,
    options: TranscriptionOptions
  ): Promise<TranscriptionResult>;
  transcribeFile(
    audioBuffer: Buffer,
    options: TranscriptionOptions
  ): Promise<TranscriptionResult>;
}
```

### Deepgram Adapter
```typescript
// adapters/deepgram-adapter.ts
import { createClient } from '@deepgram/sdk';
import { TranscriptionAdapter, TranscriptionResult, TranscriptionOptions } from './transcription-adapter';

export class DeepgramAdapter implements TranscriptionAdapter {
  name = 'deepgram';
  private client;

  constructor(apiKey: string) {
    this.client = createClient(apiKey);
  }

  async transcribe(
    audioUrl: string,
    options: TranscriptionOptions
  ): Promise<TranscriptionResult> {
    const { result, error } = await this.client.listen.prerecorded.transcribeUrl(
      { url: audioUrl },
      {
        model: 'nova-2',
        language: options.language || 'en',
        diarize: options.diarization ?? false,
        punctuate: options.punctuation ?? true,
        profanity_filter: options.profanityFilter ?? false,
        smart_format: true,
      }
    );

    if (error) throw error;

    return this.normalizeResult(result);
  }

  async transcribeFile(
    audioBuffer: Buffer,
    options: TranscriptionOptions
  ): Promise<TranscriptionResult> {
    const { result, error } = await this.client.listen.prerecorded.transcribeFile(
      audioBuffer,
      {
        model: 'nova-2',
        language: options.language || 'en',
        diarize: options.diarization ?? false,
        punctuate: options.punctuation ?? true,
        smart_format: true,
      }
    );

    if (error) throw error;

    return this.normalizeResult(result);
  }

  private normalizeResult(result: any): TranscriptionResult {
    const channel = result.results.channels[0];
    const alternative = channel.alternatives[0];

    return {
      transcript: alternative.transcript,
      confidence: alternative.confidence,
      words: alternative.words?.map((w: any) => ({
        word: w.punctuated_word || w.word,
        start: w.start,
        end: w.end,
        confidence: w.confidence,
      })),
      language: channel.detected_language,
      provider: this.name,
    };
  }
}
```

### AWS Transcribe Adapter (for comparison)
```typescript
// adapters/aws-transcribe-adapter.ts
import {
  TranscribeClient,
  StartTranscriptionJobCommand,
  GetTranscriptionJobCommand,
} from '@aws-sdk/client-transcribe';
import { S3Client, GetObjectCommand } from '@aws-sdk/client-s3';
import { TranscriptionAdapter, TranscriptionResult, TranscriptionOptions } from './transcription-adapter';

export class AWSTranscribeAdapter implements TranscriptionAdapter {
  name = 'aws-transcribe';
  private transcribe: TranscribeClient;
  private s3: S3Client;

  constructor() {
    this.transcribe = new TranscribeClient({});
    this.s3 = new S3Client({});
  }

  async transcribe(
    audioUrl: string,
    options: TranscriptionOptions
  ): Promise<TranscriptionResult> {
    const jobName = `job-${Date.now()}`;

    // Start transcription job
    await this.transcribe.send(new StartTranscriptionJobCommand({
      TranscriptionJobName: jobName,
      Media: { MediaFileUri: audioUrl },
      LanguageCode: options.language || 'en-US',
      Settings: {
        ShowSpeakerLabels: options.diarization,
        MaxSpeakerLabels: options.diarization ? 10 : undefined,
      },
    }));

    // Poll for completion
    const result = await this.waitForJob(jobName);

    return this.normalizeResult(result);
  }

  async transcribeFile(
    audioBuffer: Buffer,
    options: TranscriptionOptions
  ): Promise<TranscriptionResult> {
    // AWS requires S3, so upload first
    throw new Error('Use transcribe() with S3 URL for AWS Transcribe');
  }

  private async waitForJob(jobName: string): Promise<any> {
    while (true) {
      const { TranscriptionJob } = await this.transcribe.send(
        new GetTranscriptionJobCommand({ TranscriptionJobName: jobName })
      );

      if (TranscriptionJob?.TranscriptionJobStatus === 'COMPLETED') {
        // Fetch result from S3
        const resultUrl = TranscriptionJob.Transcript?.TranscriptFileUri;
        // Parse and return
        return {}; // Simplified
      }

      if (TranscriptionJob?.TranscriptionJobStatus === 'FAILED') {
        throw new Error('Transcription failed');
      }

      await new Promise(r => setTimeout(r, 5000));
    }
  }

  private normalizeResult(result: any): TranscriptionResult {
    // Normalize AWS format to common format
    return {
      transcript: result.results?.transcripts?.[0]?.transcript || '',
      confidence: 0.9, // AWS doesn't provide overall confidence
      provider: this.name,
    };
  }
}
```

### Migration Router
```typescript
// services/migration-router.ts
import { TranscriptionAdapter, TranscriptionOptions, TranscriptionResult } from '../adapters/transcription-adapter';
import { DeepgramAdapter } from '../adapters/deepgram-adapter';
import { AWSTranscribeAdapter } from '../adapters/aws-transcribe-adapter';

interface MigrationConfig {
  deepgramPercentage: number; // 0-100
  compareResults: boolean;
  logDifferences: boolean;
}

export class MigrationRouter {
  private deepgram: TranscriptionAdapter;
  private legacy: TranscriptionAdapter;
  private config: MigrationConfig;

  constructor(config: MigrationConfig) {
    this.deepgram = new DeepgramAdapter(process.env.DEEPGRAM_API_KEY!);
    this.legacy = new AWSTranscribeAdapter();
    this.config = config;
  }

  async transcribe(
    audioUrl: string,
    options: TranscriptionOptions
  ): Promise<TranscriptionResult> {
    // Decide which provider to use
    const useDeepgram = Math.random() * 100 < this.config.deepgramPercentage;

    if (this.config.compareResults) {
      // Run both and compare
      const [deepgramResult, legacyResult] = await Promise.all([
        this.deepgram.transcribe(audioUrl, options).catch(e => null),
        this.legacy.transcribe(audioUrl, options).catch(e => null),
      ]);

      if (deepgramResult && legacyResult) {
        this.compareAndLog(deepgramResult, legacyResult, audioUrl);
      }

      // Return based on routing decision
      if (useDeepgram && deepgramResult) {
        return deepgramResult;
      }
      if (legacyResult) {
        return legacyResult;
      }
      throw new Error('Both providers failed');
    }

    // Single provider mode
    const provider = useDeepgram ? this.deepgram : this.legacy;
    return provider.transcribe(audioUrl, options);
  }

  private compareAndLog(
    deepgram: TranscriptionResult,
    legacy: TranscriptionResult,
    audioUrl: string
  ): void {
    const similarity = this.calculateSimilarity(
      deepgram.transcript,
      legacy.transcript
    );

    const comparison = {
      audioUrl,
      similarity,
      deepgramConfidence: deepgram.confidence,
      legacyConfidence: legacy.confidence,
      deepgramLength: deepgram.transcript.length,
      legacyLength: legacy.transcript.length,
    };

    if (this.config.logDifferences && similarity < 0.95) {
      console.log('Significant difference detected:', comparison);
      // Could also store to database for analysis
    }
  }

  private calculateSimilarity(a: string, b: string): number {
    const wordsA = a.toLowerCase().split(/\s+/);
    const wordsB = b.toLowerCase().split(/\s+/);

    const setA = new Set(wordsA);
    const setB = new Set(wordsB);

    const intersection = new Set([...setA].filter(x => setB.has(x)));
    const union = new Set([...setA, ...setB]);

    return intersection.size / union.size;
  }

  async setDeepgramPercentage(percentage: number): Promise<void> {
    if (percentage < 0 || percentage > 100) {
      throw new Error('Percentage must be 0-100');
    }
    this.config.deepgramPercentage = percentage;
  }
}
```

### Feature Mapping
```typescript
// config/feature-mapping.ts
interface FeatureMap {
  source: string;
  deepgram: string;
  notes: string;
}

export const awsToDeepgram: FeatureMap[] = [
  {
    source: 'LanguageCode: en-US',
    deepgram: 'language: "en"',
    notes: 'Deepgram uses ISO 639-1 codes',
  },
  {
    source: 'ShowSpeakerLabels: true',
    deepgram: 'diarize: true',
    notes: 'Similar functionality',
  },
  {
    source: 'VocabularyName: custom',
    deepgram: 'keywords: ["term:1.5"]',
    notes: 'Use keywords with boost values',
  },
  {
    source: 'ContentRedaction',
    deepgram: 'redact: ["pci", "ssn"]',
    notes: 'Built-in PII redaction',
  },
];

export const googleToDeepgram: FeatureMap[] = [
  {
    source: 'encoding: LINEAR16',
    deepgram: 'mimetype: "audio/wav"',
    notes: 'Auto-detected by Deepgram',
  },
  {
    source: 'enableWordTimeOffsets: true',
    deepgram: 'Default behavior',
    notes: 'Always included in Deepgram',
  },
  {
    source: 'enableAutomaticPunctuation: true',
    deepgram: 'punctuate: true',
    notes: 'Same functionality',
  },
  {
    source: 'model: video',
    deepgram: 'model: "nova-2"',
    notes: 'Nova-2 handles all use cases',
  },
];
```

### Migration Validation
```typescript
// scripts/validate-migration.ts
import { MigrationRouter } from '../services/migration-router';

interface ValidationResult {
  totalTests: number;
  passed: number;
  failed: number;
  avgSimilarity: number;
  avgDeepgramLatency: number;
  avgLegacyLatency: number;
}

async function validateMigration(
  testAudioUrls: string[]
): Promise<ValidationResult> {
  const router = new MigrationRouter({
    deepgramPercentage: 50,
    compareResults: true,
    logDifferences: true,
  });

  const results = {
    totalTests: testAudioUrls.length,
    passed: 0,
    failed: 0,
    avgSimilarity: 0,
    avgDeepgramLatency: 0,
    avgLegacyLatency: 0,
  };

  const similarities: number[] = [];
  const deepgramLatencies: number[] = [];
  const legacyLatencies: number[] = [];

  for (const url of testAudioUrls) {
    try {
      // Measure Deepgram
      const dgStart = Date.now();
      const dgResult = await router['deepgram'].transcribe(url, {});
      deepgramLatencies.push(Date.now() - dgStart);

      // Measure Legacy
      const legStart = Date.now();
      const legResult = await router['legacy'].transcribe(url, {});
      legacyLatencies.push(Date.now() - legStart);

      // Calculate similarity
      const similarity = router['calculateSimilarity'](
        dgResult.transcript,
        legResult.transcript
      );
      similarities.push(similarity);

      if (similarity >= 0.90) {
        results.passed++;
      } else {
        results.failed++;
        console.log(`Low similarity for ${url}: ${similarity}`);
      }
    } catch (error) {
      results.failed++;
      console.error(`Test failed for ${url}:`, error);
    }
  }

  results.avgSimilarity = similarities.reduce((a, b) => a + b, 0) / similarities.length;
  results.avgDeepgramLatency = deepgramLatencies.reduce((a, b) => a + b, 0) / deepgramLatencies.length;
  results.avgLegacyLatency = legacyLatencies.reduce((a, b) => a + b, 0) / legacyLatencies.length;

  return results;
}

// Run validation
const testUrls = [
  'https://example.com/audio1.wav',
  'https://example.com/audio2.wav',
  // Add more test URLs
];

validateMigration(testUrls).then(results => {
  console.log('\n=== Migration Validation Results ===');
  console.log(`Total Tests: ${results.totalTests}`);
  console.log(`Passed: ${results.passed}`);
  console.log(`Failed: ${results.failed}`);
  console.log(`Avg Similarity: ${(results.avgSimilarity * 100).toFixed(1)}%`);
  console.log(`Avg Deepgram Latency: ${results.avgDeepgramLatency.toFixed(0)}ms`);
  console.log(`Avg Legacy Latency: ${results.avgLegacyLatency.toFixed(0)}ms`);

  if (results.passed / results.totalTests >= 0.95) {
    console.log('\n Migration validation PASSED');
  } else {
    console.log('\n Migration validation FAILED - review differences');
  }
});
```

### Rollback Plan
```typescript
// services/rollback.ts
import { MigrationRouter } from './migration-router';

export class RollbackManager {
  private router: MigrationRouter;
  private checkpoints: Array<{ timestamp: Date; percentage: number }> = [];

  constructor(router: MigrationRouter) {
    this.router = router;
  }

  async checkpoint(): Promise<void> {
    const current = await this.getCurrentPercentage();
    this.checkpoints.push({
      timestamp: new Date(),
      percentage: current,
    });
  }

  async rollback(): Promise<void> {
    const previous = this.checkpoints.pop();
    if (previous) {
      await this.router.setDeepgramPercentage(previous.percentage);
      console.log(`Rolled back to ${previous.percentage}%`);
    } else {
      await this.router.setDeepgramPercentage(0);
      console.log('Rolled back to 0% (full legacy)');
    }
  }

  async emergencyRollback(): Promise<void> {
    await this.router.setDeepgramPercentage(0);
    console.log('EMERGENCY: Rolled back to 0%');
  }

  private async getCurrentPercentage(): Promise<number> {
    return this.router['config'].deepgramPercentage;
  }
}
```

## Migration Checklist

```markdown
## Pre-Migration
- [ ] Inventory current usage (hours/month, features used)
- [ ] Map features to Deepgram equivalents
- [ ] Estimate Deepgram costs
- [ ] Set up Deepgram project and API keys
- [ ] Implement adapter pattern
- [ ] Create test dataset

## Validation Phase
- [ ] Run comparison tests
- [ ] Verify accuracy meets requirements
- [ ] Confirm latency is acceptable
- [ ] Test all required features
- [ ] Document any differences

## Rollout Phase
- [ ] Start at 5% traffic
- [ ] Monitor error rates
- [ ] Compare costs
- [ ] Increase to 25%
- [ ] Review for 1 week
- [ ] Increase to 50%
- [ ] Review for 1 week
- [ ] Increase to 100%

## Post-Migration
- [ ] Decommission legacy provider
- [ ] Update documentation
- [ ] Archive comparison data
- [ ] Update runbooks
- [ ] Train team on Deepgram specifics
```

## Resources
- [Deepgram Migration Guide](https://developers.deepgram.com/docs/migration)
- [Feature Comparison](https://developers.deepgram.com/docs/features)
- [Pricing Calculator](https://deepgram.com/pricing)

## Conclusion
This skill pack provides 24 comprehensive skills for Deepgram integration covering the full development lifecycle from initial setup through enterprise deployment and migration scenarios.
