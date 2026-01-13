# Monitoring Architecture

## Monitoring Architecture

```typescript
// architecture/monitoring/dashboard.ts
import { Registry, collectDefaultMetrics, Counter, Histogram, Gauge } from 'prom-client';

export const registry = new Registry();
collectDefaultMetrics({ register: registry });

// Metrics
export const requestsTotal = new Counter({
  name: 'transcription_requests_total',
  help: 'Total transcription requests',
  labelNames: ['status', 'model', 'region'],
  registers: [registry],
});

export const latencyHistogram = new Histogram({
  name: 'transcription_latency_seconds',
  help: 'Transcription latency',
  labelNames: ['model'],
  buckets: [0.5, 1, 2, 5, 10, 30, 60, 120],
  registers: [registry],
});

export const queueDepth = new Gauge({
  name: 'transcription_queue_depth',
  help: 'Number of jobs in queue',
  registers: [registry],
});

export const activeConnections = new Gauge({
  name: 'deepgram_active_connections',
  help: 'Active Deepgram connections',
  registers: [registry],
});
```