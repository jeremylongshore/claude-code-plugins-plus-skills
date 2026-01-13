# Implementation Guide

### Step 1: Structured Logging
```typescript
// lib/logger.ts
import pino from 'pino';

export const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  formatters: {
    level: (label) => ({ level: label }),
  },
  base: {
    service: 'lindy-integration',
    environment: process.env.NODE_ENV,
  },
});

// Lindy-specific logger
export function lindyLogger(operation: string) {
  return logger.child({ component: 'lindy', operation });
}
```

### Step 2: Instrumented Client
```typescript
// lib/instrumented-lindy.ts
import { Lindy } from '@lindy-ai/sdk';
import { lindyLogger } from './logger';
import { metrics } from './metrics';
import { tracer } from './tracer';

export class InstrumentedLindy {
  private lindy: Lindy;

  constructor() {
    this.lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });
  }

  async runAgent(agentId: string, input: string) {
    const log = lindyLogger('runAgent');
    const span = tracer.startSpan('lindy.agent.run');

    const startTime = Date.now();

    try {
      span.setAttributes({
        'lindy.agent_id': agentId,
        'lindy.input_length': input.length,
      });

      log.info({ agentId, inputLength: input.length }, 'Starting agent run');

      const result = await this.lindy.agents.run(agentId, { input });

      const duration = Date.now() - startTime;

      // Record metrics
      metrics.histogram('lindy.agent.duration', duration, { agentId });
      metrics.counter('lindy.agent.success', 1, { agentId });

      // Log success
      log.info({
        agentId,
        duration,
        outputLength: result.output.length,
      }, 'Agent run completed');

      span.setAttributes({
        'lindy.duration_ms': duration,
        'lindy.output_length': result.output.length,
        'lindy.status': 'success',
      });

      return result;
    } catch (error: any) {
      const duration = Date.now() - startTime;

      // Record error metrics
      metrics.counter('lindy.agent.error', 1, {
        agentId,
        errorCode: error.code,
      });

      // Log error
      log.error({
        agentId,
        duration,
        error: error.message,
        errorCode: error.code,
      }, 'Agent run failed');

      span.setAttributes({
        'lindy.status': 'error',
        'lindy.error': error.message,
      });
      span.recordException(error);

      throw error;
    } finally {
      span.end();
    }
  }
}
```

### Step 3: Metrics Collection
```typescript
// lib/metrics.ts
import { Counter, Histogram, Registry } from 'prom-client';

const registry = new Registry();

export const metrics = {
  agentDuration: new Histogram({
    name: 'lindy_agent_duration_ms',
    help: 'Duration of Lindy agent runs in milliseconds',
    labelNames: ['agent_id', 'status'],
    buckets: [100, 500, 1000, 2000, 5000, 10000, 30000],
    registers: [registry],
  }),

  agentRuns: new Counter({
    name: 'lindy_agent_runs_total',
    help: 'Total number of Lindy agent runs',
    labelNames: ['agent_id', 'status'],
    registers: [registry],
  }),

  apiCalls: new Counter({
    name: 'lindy_api_calls_total',
    help: 'Total Lindy API calls',
    labelNames: ['endpoint', 'status'],
    registers: [registry],
  }),

  // Helper methods
  histogram(name: string, value: number, labels: Record<string, string>) {
    const metric = registry.getSingleMetric(name) as Histogram;
    metric?.observe(labels, value);
  },

  counter(name: string, value: number, labels: Record<string, string>) {
    const metric = registry.getSingleMetric(name) as Counter;
    metric?.inc(labels, value);
  },
};

// Metrics endpoint
export function getMetrics(): Promise<string> {
  return registry.metrics();
}
```

### Step 4: Distributed Tracing
```typescript
// lib/tracer.ts
import { trace, SpanStatusCode } from '@opentelemetry/api';
import { NodeTracerProvider } from '@opentelemetry/sdk-trace-node';
import { SimpleSpanProcessor } from '@opentelemetry/sdk-trace-base';
import { OTLPTraceExporter } from '@opentelemetry/exporter-trace-otlp-http';

const provider = new NodeTracerProvider();

provider.addSpanProcessor(
  new SimpleSpanProcessor(
    new OTLPTraceExporter({
      url: process.env.OTEL_EXPORTER_OTLP_ENDPOINT,
    })
  )
);

provider.register();

export const tracer = trace.getTracer('lindy-integration');
```

### Step 5: Dashboard Configuration
```yaml
# grafana/dashboards/lindy.json
{
  "title": "Lindy AI Monitoring",
  "panels": [
    {
      "title": "Agent Runs per Minute",
      "type": "graph",
      "targets": [
        {
          "expr": "rate(lindy_agent_runs_total[1m])",
          "legendFormat": "{{agent_id}}"
        }
      ]
    },
    {
      "title": "P95 Latency",
      "type": "stat",
      "targets": [
        {
          "expr": "histogram_quantile(0.95, rate(lindy_agent_duration_ms_bucket[5m]))"
        }
      ]
    },
    {
      "title": "Error Rate",
      "type": "graph",
      "targets": [
        {
          "expr": "rate(lindy_agent_runs_total{status='error'}[5m]) / rate(lindy_agent_runs_total[5m])"
        }
      ]
    }
  ]
}
```