---
name: gamma-observability
license: MIT
allowed-tools: Read, Write, Edit
description: Implement comprehensive observability for gamma integrations. use when
  setting up monitoring, logging, tracing, or building dashboards for gamma api usage.
  trigger with phrases like "gamma monitoring", "gamma logging", "gamma metrics",
  "gamma obse...
---
# Gamma Observability

## Overview
Implement comprehensive monitoring, logging, and tracing for Gamma integrations.

## Prerequisites
- Observability stack (Prometheus, Grafana, or cloud equivalent)
- Log aggregation (ELK, CloudWatch, or similar)
- APM tool (Datadog, New Relic, or OpenTelemetry)

## Three Pillars of Observability

### 1. Metrics

```typescript
// lib/gamma-metrics.ts
import { Counter, Histogram, Gauge, Registry } from 'prom-client';

const registry = new Registry();

// Request metrics
const requestCounter = new Counter({
  name: 'gamma_requests_total',
  help: 'Total Gamma API requests',
  labelNames: ['method', 'endpoint', 'status'],
  registers: [registry],
});

const requestDuration = new Histogram({
  name: 'gamma_request_duration_seconds',
  help: 'Gamma API request duration',
  labelNames: ['method', 'endpoint'],
  buckets: [0.1, 0.5, 1, 2, 5, 10, 30],
  registers: [registry],
});

// Business metrics
const presentationsCreated = new Counter({
  name: 'gamma_presentations_created_total',
  help: 'Total presentations created',
  labelNames: ['style', 'user_tier'],
  registers: [registry],
});

const rateLimitRemaining = new Gauge({
  name: 'gamma_rate_limit_remaining',
  help: 'Remaining API calls in rate limit window',
  registers: [registry],
});

// Instrumented client
export function createInstrumentedClient() {
  return new GammaClient({
    apiKey: process.env.GAMMA_API_KEY,
    interceptors: {
      request: (config) => {
        config._startTime = Date.now();
        return config;
      },
      response: (response, config) => {
        const duration = (Date.now() - config._startTime) / 1000;
        const endpoint = config.path.split('/')[1];

        requestCounter.inc({
          method: config.method,
          endpoint,
          status: response.status,
        });

        requestDuration.observe(
          { method: config.method, endpoint },
          duration
        );

        // Update rate limit gauge
        const remaining = response.headers['x-ratelimit-remaining'];
        if (remaining) {
          rateLimitRemaining.set(parseInt(remaining, 10));
        }

        return response;
      },
    },
  });
}
```

### 2. Logging

```typescript
// lib/gamma-logger.ts
import winston from 'winston';

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  defaultMeta: { service: 'gamma-integration' },
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'gamma-error.log', level: 'error' }),
    new winston.transports.File({ filename: 'gamma-combined.log' }),
  ],
});

// Structured logging for Gamma operations
export function logGammaRequest(operation: string, params: object) {
  logger.info('Gamma API request', {
    operation,
    params: sanitizeParams(params),
    timestamp: new Date().toISOString(),
  });
}

export function logGammaResponse(operation: string, response: object, duration: number) {
  logger.info('Gamma API response', {
    operation,
    duration,
    success: true,
    responseId: response.id,
  });
}

export function logGammaError(operation: string, error: Error, context: object) {
  logger.error('Gamma API error', {
    operation,
    error: error.message,
    stack: error.stack,
    context,
  });
}

function sanitizeParams(params: object): object {
  const sanitized = { ...params };
  // Remove sensitive fields
  delete sanitized.apiKey;
  delete sanitized.secret;
  return sanitized;
}
```

### 3. Distributed Tracing

```typescript
// lib/gamma-tracing.ts
import { trace, SpanKind, SpanStatusCode } from '@opentelemetry/api';

const tracer = trace.getTracer('gamma-integration');

export async function traceGammaCall<T>(
  operationName: string,
  fn: () => Promise<T>
): Promise<T> {
  return tracer.startActiveSpan(
    `gamma.${operationName}`,
    { kind: SpanKind.CLIENT },
    async (span) => {
      try {
        const result = await fn();

        span.setAttributes({
          'gamma.operation': operationName,
          'gamma.success': true,
        });

        span.setStatus({ code: SpanStatusCode.OK });
        return result;
      } catch (error) {
        span.setAttributes({
          'gamma.operation': operationName,
          'gamma.success': false,
          'gamma.error': error.message,
        });

        span.setStatus({
          code: SpanStatusCode.ERROR,
          message: error.message,
        });

        span.recordException(error);
        throw error;
      } finally {
        span.end();
      }
    }
  );
}

// Usage
const presentation = await traceGammaCall('presentations.create', () =>
  gamma.presentations.create({ title: 'My Deck', prompt: 'AI content' })
);
```

## Dashboard Configuration

### Grafana Dashboard
```json
{
  "title": "Gamma Integration",
  "panels": [
    {
      "title": "Request Rate",
      "type": "graph",
      "targets": [
        { "expr": "rate(gamma_requests_total[5m])" }
      ]
    },
    {
      "title": "Latency P95",
      "type": "graph",
      "targets": [
        { "expr": "histogram_quantile(0.95, rate(gamma_request_duration_seconds_bucket[5m]))" }
      ]
    },
    {
      "title": "Error Rate",
      "type": "stat",
      "targets": [
        { "expr": "rate(gamma_requests_total{status=~'5..'}[5m]) / rate(gamma_requests_total[5m])" }
      ]
    },
    {
      "title": "Rate Limit Remaining",
      "type": "gauge",
      "targets": [
        { "expr": "gamma_rate_limit_remaining" }
      ]
    }
  ]
}
```

### Alert Rules
```yaml
# prometheus/alerts.yml
groups:
  - name: gamma
    rules:
      - alert: GammaHighErrorRate
        expr: rate(gamma_requests_total{status=~"5.."}[5m]) / rate(gamma_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: High Gamma API error rate

      - alert: GammaRateLimitLow
        expr: gamma_rate_limit_remaining < 10
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: Gamma rate limit nearly exhausted

      - alert: GammaHighLatency
        expr: histogram_quantile(0.95, rate(gamma_request_duration_seconds_bucket[5m])) > 5
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: Gamma API latency is high
```

## Health Check Endpoint

```typescript
// routes/health.ts
app.get('/health/gamma', async (req, res) => {
  const health = {
    status: 'unknown',
    latency: 0,
    rateLimit: { remaining: 0, limit: 0 },
    timestamp: new Date().toISOString(),
  };

  try {
    const start = Date.now();
    const response = await gamma.ping();
    health.latency = Date.now() - start;
    health.status = response.ok ? 'healthy' : 'degraded';
    health.rateLimit = {
      remaining: response.rateLimit.remaining,
      limit: response.rateLimit.limit,
    };
  } catch (error) {
    health.status = 'unhealthy';
  }

  const statusCode = health.status === 'healthy' ? 200 : 503;
  res.status(statusCode).json(health);
});
```

## Resources
- [OpenTelemetry Documentation](https://opentelemetry.io/docs/)
- [Prometheus Best Practices](https://prometheus.io/docs/practices/)
- [Grafana Dashboards](https://grafana.com/docs/grafana/latest/dashboards/)

## Next Steps
Proceed to `gamma-incident-runbook` for incident response.
