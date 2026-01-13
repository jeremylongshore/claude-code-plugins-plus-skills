---
name: deepgram-observability
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Set up comprehensive observability for deepgram integrations with metrics,
  traces, and alerts. use when implementing monitoring for deepgram operations, setting
  up dashboards, or configuring alerting for deepgram integration health. trigger
  with p...
---
# Deepgram Observability

## Overview
Implement comprehensive observability for Deepgram integrations including metrics, distributed tracing, logging, and alerting.

## Prerequisites
- Prometheus or compatible metrics backend
- OpenTelemetry SDK installed
- Grafana or similar dashboarding tool
- AlertManager configured

## Observability Pillars

| Pillar | Tool | Purpose |
|--------|------|---------|
| Metrics | Prometheus | Performance & usage tracking |
| Traces | OpenTelemetry | Request flow visibility |
| Logs | Structured JSON | Debugging & audit |
| Alerts | AlertManager | Incident notification |

## Instructions

### Step 1: Set Up Metrics Collection
Implement Prometheus counters, histograms, and gauges for key operations.

### Step 2: Add Distributed Tracing
Integrate OpenTelemetry for end-to-end request tracing.

### Step 3: Configure Structured Logging
Set up JSON logging with consistent field names.

### Step 4: Create Alert Rules
Define alerting rules for error rates and latency.

## Examples

### Prometheus Metrics
```typescript
// lib/metrics.ts
import { Registry, Counter, Histogram, Gauge, collectDefaultMetrics } from 'prom-client';

export const registry = new Registry();
collectDefaultMetrics({ register: registry });

// Request counters
export const transcriptionRequests = new Counter({
  name: 'deepgram_transcription_requests_total',
  help: 'Total number of transcription requests',
  labelNames: ['status', 'model', 'type'],
  registers: [registry],
});

// Latency histogram
export const transcriptionLatency = new Histogram({
  name: 'deepgram_transcription_latency_seconds',
  help: 'Transcription request latency in seconds',
  labelNames: ['model', 'type'],
  buckets: [0.1, 0.5, 1, 2, 5, 10, 30, 60, 120],
  registers: [registry],
});

// Audio duration processed
export const audioProcessed = new Counter({
  name: 'deepgram_audio_processed_seconds_total',
  help: 'Total audio duration processed in seconds',
  labelNames: ['model'],
  registers: [registry],
});

// Active connections gauge
export const activeConnections = new Gauge({
  name: 'deepgram_active_connections',
  help: 'Number of active Deepgram connections',
  labelNames: ['type'],
  registers: [registry],
});

// Rate limit hits
export const rateLimitHits = new Counter({
  name: 'deepgram_rate_limit_hits_total',
  help: 'Number of rate limit responses',
  registers: [registry],
});

// Cost tracking
export const estimatedCost = new Counter({
  name: 'deepgram_estimated_cost_dollars',
  help: 'Estimated cost in dollars',
  labelNames: ['model'],
  registers: [registry],
});

// Metrics endpoint
export async function getMetrics(): Promise<string> {
  return registry.metrics();
}
```

### Instrumented Transcription Client
```typescript
// lib/instrumented-client.ts
import { createClient, DeepgramClient } from '@deepgram/sdk';
import {
  transcriptionRequests,
  transcriptionLatency,
  audioProcessed,
  estimatedCost,
} from './metrics';
import { trace, context, SpanStatusCode } from '@opentelemetry/api';
import { logger } from './logger';

const tracer = trace.getTracer('deepgram-client');

const modelCosts: Record<string, number> = {
  'nova-2': 0.0043,
  'nova': 0.0043,
  'base': 0.0048,
};

export class InstrumentedDeepgramClient {
  private client: DeepgramClient;

  constructor(apiKey: string) {
    this.client = createClient(apiKey);
  }

  async transcribeUrl(url: string, options: { model?: string } = {}) {
    const model = options.model || 'nova-2';
    const startTime = Date.now();

    return tracer.startActiveSpan('deepgram.transcribe', async (span) => {
      span.setAttribute('deepgram.model', model);
      span.setAttribute('deepgram.audio_url', url);

      try {
        const { result, error } = await this.client.listen.prerecorded.transcribeUrl(
          { url },
          { model, smart_format: true }
        );

        const duration = (Date.now() - startTime) / 1000;

        if (error) {
          transcriptionRequests.labels('error', model, 'prerecorded').inc();
          span.setStatus({ code: SpanStatusCode.ERROR, message: error.message });

          logger.error('Transcription failed', {
            model,
            error: error.message,
            duration,
          });

          throw error;
        }

        // Record metrics
        transcriptionRequests.labels('success', model, 'prerecorded').inc();
        transcriptionLatency.labels(model, 'prerecorded').observe(duration);

        const audioDuration = result.metadata.duration;
        audioProcessed.labels(model).inc(audioDuration);

        const cost = (audioDuration / 60) * (modelCosts[model] || 0.0043);
        estimatedCost.labels(model).inc(cost);

        span.setAttribute('deepgram.request_id', result.metadata.request_id);
        span.setAttribute('deepgram.audio_duration', audioDuration);
        span.setAttribute('deepgram.processing_time', duration);
        span.setStatus({ code: SpanStatusCode.OK });

        logger.info('Transcription completed', {
          requestId: result.metadata.request_id,
          model,
          audioDuration,
          processingTime: duration,
          cost,
        });

        return result;
      } catch (err) {
        const duration = (Date.now() - startTime) / 1000;
        transcriptionRequests.labels('exception', model, 'prerecorded').inc();
        transcriptionLatency.labels(model, 'prerecorded').observe(duration);

        span.setStatus({
          code: SpanStatusCode.ERROR,
          message: err instanceof Error ? err.message : 'Unknown error',
        });

        logger.error('Transcription exception', {
          model,
          error: err instanceof Error ? err.message : 'Unknown',
          duration,
        });

        throw err;
      } finally {
        span.end();
      }
    });
  }
}
```

### OpenTelemetry Configuration
```typescript
// lib/tracing.ts
import { NodeSDK } from '@opentelemetry/sdk-node';
import { getNodeAutoInstrumentations } from '@opentelemetry/auto-instrumentations-node';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-grpc';
import { Resource } from '@opentelemetry/resources';
import { SemanticResourceAttributes } from '@opentelemetry/semantic-conventions';

const sdk = new NodeSDK({
  resource: new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: 'deepgram-service',
    [SemanticResourceAttributes.SERVICE_VERSION]: process.env.VERSION || '1.0.0',
    [SemanticResourceAttributes.DEPLOYMENT_ENVIRONMENT]: process.env.NODE_ENV || 'development',
  }),
  traceExporter: new OTLPTraceExporter({
    url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT || 'http://localhost:4317',
  }),
  instrumentations: [
    getNodeAutoInstrumentations({
      '@opentelemetry/instrumentation-http': {
        ignoreIncomingPaths: ['/health', '/metrics'],
      },
    }),
  ],
});

export function initTracing(): void {
  sdk.start();

  process.on('SIGTERM', () => {
    sdk.shutdown()
      .then(() => console.log('Tracing terminated'))
      .catch((error) => console.error('Error terminating tracing', error))
      .finally(() => process.exit(0));
  });
}
```

### Structured Logging
```typescript
// lib/logger.ts
import pino from 'pino';

export const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  formatters: {
    level: (label) => ({ level: label }),
  },
  base: {
    service: 'deepgram-service',
    version: process.env.VERSION || '1.0.0',
    environment: process.env.NODE_ENV || 'development',
  },
  timestamp: pino.stdTimeFunctions.isoTime,
});

// Specialized loggers
export const transcriptionLogger = logger.child({ component: 'transcription' });
export const metricsLogger = logger.child({ component: 'metrics' });
export const alertLogger = logger.child({ component: 'alerts' });
```

### Grafana Dashboard Configuration
```json
{
  "dashboard": {
    "title": "Deepgram Transcription Service",
    "panels": [
      {
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(deepgram_transcription_requests_total[5m])) by (status)",
            "legendFormat": "{{status}}"
          }
        ]
      },
      {
        "title": "Latency (P95)",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, sum(rate(deepgram_transcription_latency_seconds_bucket[5m])) by (le, model))",
            "legendFormat": "{{model}}"
          }
        ]
      },
      {
        "title": "Audio Processed (per hour)",
        "type": "stat",
        "targets": [
          {
            "expr": "sum(increase(deepgram_audio_processed_seconds_total[1h]))/60",
            "legendFormat": "Minutes"
          }
        ]
      },
      {
        "title": "Error Rate",
        "type": "gauge",
        "targets": [
          {
            "expr": "sum(rate(deepgram_transcription_requests_total{status='error'}[5m])) / sum(rate(deepgram_transcription_requests_total[5m])) * 100"
          }
        ]
      },
      {
        "title": "Estimated Cost Today",
        "type": "stat",
        "targets": [
          {
            "expr": "sum(increase(deepgram_estimated_cost_dollars[24h]))"
          }
        ]
      },
      {
        "title": "Active Connections",
        "type": "graph",
        "targets": [
          {
            "expr": "deepgram_active_connections",
            "legendFormat": "{{type}}"
          }
        ]
      }
    ]
  }
}
```

### AlertManager Rules
```yaml
# prometheus/rules/deepgram.yml
groups:
  - name: deepgram-alerts
    rules:
      - alert: DeepgramHighErrorRate
        expr: |
          sum(rate(deepgram_transcription_requests_total{status="error"}[5m])) /
          sum(rate(deepgram_transcription_requests_total[5m])) > 0.05
        for: 5m
        labels:
          severity: critical
          service: deepgram
        annotations:
          summary: "High Deepgram error rate (> 5%)"
          description: "Error rate is {{ $value | humanizePercentage }}"
          runbook: "https://wiki.example.com/runbooks/deepgram-errors"

      - alert: DeepgramHighLatency
        expr: |
          histogram_quantile(0.95,
            sum(rate(deepgram_transcription_latency_seconds_bucket[5m])) by (le)
          ) > 30
        for: 5m
        labels:
          severity: warning
          service: deepgram
        annotations:
          summary: "High Deepgram latency (P95 > 30s)"
          description: "P95 latency is {{ $value | humanizeDuration }}"

      - alert: DeepgramRateLimited
        expr: increase(deepgram_rate_limit_hits_total[1h]) > 10
        for: 0m
        labels:
          severity: warning
          service: deepgram
        annotations:
          summary: "Deepgram rate limiting detected"
          description: "{{ $value }} rate limit hits in the last hour"

      - alert: DeepgramCostSpike
        expr: |
          sum(increase(deepgram_estimated_cost_dollars[1h])) >
          sum(increase(deepgram_estimated_cost_dollars[1h] offset 1d)) * 2
        for: 30m
        labels:
          severity: warning
          service: deepgram
        annotations:
          summary: "Deepgram cost spike detected"
          description: "Current hour cost is 2x yesterday's average"

      - alert: DeepgramNoRequests
        expr: |
          sum(rate(deepgram_transcription_requests_total[15m])) == 0
          and sum(deepgram_transcription_requests_total) > 0
        for: 15m
        labels:
          severity: warning
          service: deepgram
        annotations:
          summary: "No Deepgram requests in 15 minutes"
          description: "Service may be down or disconnected"
```

### Health Check Endpoint
```typescript
// routes/health.ts
import express from 'express';
import { createClient } from '@deepgram/sdk';
import { getMetrics } from '../lib/metrics';

const router = express.Router();

interface HealthCheck {
  status: 'healthy' | 'degraded' | 'unhealthy';
  timestamp: string;
  checks: Record<string, {
    status: 'pass' | 'fail';
    latency?: number;
    message?: string;
  }>;
}

router.get('/health', async (req, res) => {
  const health: HealthCheck = {
    status: 'healthy',
    timestamp: new Date().toISOString(),
    checks: {},
  };

  // Check Deepgram API
  const startTime = Date.now();
  try {
    const client = createClient(process.env.DEEPGRAM_API_KEY!);
    const { error } = await client.manage.getProjects();

    health.checks.deepgram = {
      status: error ? 'fail' : 'pass',
      latency: Date.now() - startTime,
      message: error?.message,
    };
  } catch (err) {
    health.checks.deepgram = {
      status: 'fail',
      latency: Date.now() - startTime,
      message: err instanceof Error ? err.message : 'Unknown error',
    };
  }

  // Determine overall status
  const failedChecks = Object.values(health.checks).filter(c => c.status === 'fail');
  if (failedChecks.length > 0) {
    health.status = 'unhealthy';
  }

  const statusCode = health.status === 'healthy' ? 200 : 503;
  res.status(statusCode).json(health);
});

router.get('/metrics', async (req, res) => {
  res.set('Content-Type', 'text/plain');
  res.send(await getMetrics());
});

export default router;
```

## Resources
- [Prometheus Best Practices](https://prometheus.io/docs/practices/naming/)
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
- [Grafana Dashboard Examples](https://grafana.com/grafana/dashboards/)

## Next Steps
Proceed to `deepgram-incident-runbook` for incident response procedures.
