# Production Configuration

## Production Configuration

### TypeScript Production Client
```typescript
// lib/deepgram-production.ts
import { createClient, DeepgramClient } from '@deepgram/sdk';
import { getSecret } from './secrets';
import { metrics } from './metrics';
import { logger } from './logger';

interface ProductionConfig {
  timeout: number;
  retries: number;
  model: string;
}

const config: ProductionConfig = {
  timeout: 30000,
  retries: 3,
  model: 'nova-2',
};

let client: DeepgramClient | null = null;

export async function getProductionClient(): Promise<DeepgramClient> {
  if (client) return client;

  const apiKey = await getSecret('DEEPGRAM_API_KEY');
  client = createClient(apiKey, {
    global: {
      fetch: {
        options: {
          timeout: config.timeout,
        },
      },
    },
  });

  return client;
}

export async function transcribeProduction(
  audioUrl: string,
  options: { language?: string; callback?: string } = {}
) {
  const startTime = Date.now();
  const requestId = crypto.randomUUID();

  logger.info('Starting transcription', { requestId, audioUrl: sanitize(audioUrl) });

  try {
    const deepgram = await getProductionClient();

    const { result, error } = await deepgram.listen.prerecorded.transcribeUrl(
      { url: audioUrl },
      {
        model: config.model,
        language: options.language || 'en',
        smart_format: true,
        punctuate: true,
        callback: options.callback,
      }
    );

    const duration = Date.now() - startTime;
    metrics.histogram('deepgram.transcription.duration', duration);

    if (error) {
      metrics.increment('deepgram.transcription.error');
      logger.error('Transcription failed', { requestId, error: error.message });
      throw new Error(error.message);
    }

    metrics.increment('deepgram.transcription.success');
    logger.info('Transcription complete', {
      requestId,
      deepgramRequestId: result.metadata?.request_id,
      duration,
    });

    return result;
  } catch (err) {
    metrics.increment('deepgram.transcription.exception');
    logger.error('Transcription exception', {
      requestId,
      error: err instanceof Error ? err.message : 'Unknown error',
    });
    throw err;
  }
}

function sanitize(url: string): string {
  try {
    const parsed = new URL(url);
    return `${parsed.protocol}//${parsed.host}${parsed.pathname}`;
  } catch {
    return '[invalid-url]';
  }
}
```

### Health Check Endpoint
```typescript
// routes/health.ts
import { getProductionClient } from '../lib/deepgram-production';

interface HealthStatus {
  status: 'healthy' | 'degraded' | 'unhealthy';
  timestamp: string;
  checks: {
    deepgram: {
      status: 'pass' | 'fail';
      latency?: number;
      message?: string;
    };
  };
}

export async function healthCheck(): Promise<HealthStatus> {
  const checks: HealthStatus['checks'] = {
    deepgram: { status: 'fail' },
  };

  // Test Deepgram API
  const startTime = Date.now();
  try {
    const client = await getProductionClient();
    const { error } = await client.manage.getProjects();

    checks.deepgram = {
      status: error ? 'fail' : 'pass',
      latency: Date.now() - startTime,
      message: error?.message,
    };
  } catch (err) {
    checks.deepgram = {
      status: 'fail',
      latency: Date.now() - startTime,
      message: err instanceof Error ? err.message : 'Unknown error',
    };
  }

  const allPassing = Object.values(checks).every(c => c.status === 'pass');
  const anyFailing = Object.values(checks).some(c => c.status === 'fail');

  return {
    status: allPassing ? 'healthy' : anyFailing ? 'unhealthy' : 'degraded',
    timestamp: new Date().toISOString(),
    checks,
  };
}
```

### Production Metrics
```typescript
// lib/metrics.ts
import { Counter, Histogram, Registry } from 'prom-client';

export const registry = new Registry();

export const transcriptionDuration = new Histogram({
  name: 'deepgram_transcription_duration_seconds',
  help: 'Duration of Deepgram transcription requests',
  labelNames: ['status', 'model'],
  buckets: [0.1, 0.5, 1, 2, 5, 10, 30, 60],
  registers: [registry],
});

export const transcriptionTotal = new Counter({
  name: 'deepgram_transcription_total',
  help: 'Total number of transcription requests',
  labelNames: ['status', 'error_code'],
  registers: [registry],
});

export const audioProcessedSeconds = new Counter({
  name: 'deepgram_audio_processed_seconds_total',
  help: 'Total seconds of audio processed',
  registers: [registry],
});

export const rateLimitHits = new Counter({
  name: 'deepgram_rate_limit_hits_total',
  help: 'Number of rate limit errors encountered',
  registers: [registry],
});

export const metrics = {
  recordTranscription(status: 'success' | 'error', duration: number, audioSeconds?: number) {
    transcriptionDuration.labels(status, 'nova-2').observe(duration / 1000);
    transcriptionTotal.labels(status, '').inc();
    if (audioSeconds) {
      audioProcessedSeconds.inc(audioSeconds);
    }
  },

  recordRateLimitHit() {
    rateLimitHits.inc();
  },
};
```

### Alerting Configuration
```yaml
# prometheus/alerts/deepgram.yml
groups:
  - name: deepgram
    rules:
      - alert: DeepgramHighErrorRate
        expr: |
          sum(rate(deepgram_transcription_total{status="error"}[5m])) /
          sum(rate(deepgram_transcription_total[5m])) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: High Deepgram error rate
          description: Error rate is above 5% for the last 5 minutes

      - alert: DeepgramHighLatency
        expr: |
          histogram_quantile(0.95,
            sum(rate(deepgram_transcription_duration_seconds_bucket[5m])) by (le)
          ) > 10
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: High Deepgram latency
          description: P95 latency is above 10 seconds

      - alert: DeepgramRateLimiting
        expr: increase(deepgram_rate_limit_hits_total[1h]) > 10
        for: 0m
        labels:
          severity: warning
        annotations:
          summary: Deepgram rate limiting detected
          description: More than 10 rate limit hits in the last hour

      - alert: DeepgramDown
        expr: up{job="deepgram-health"} == 0
        for: 2m
        labels:
          severity: critical
        annotations:
          summary: Deepgram health check failing
          description: Health check has been failing for 2 minutes
```

### Runbook Template
```markdown
# Deepgram Incident Runbook