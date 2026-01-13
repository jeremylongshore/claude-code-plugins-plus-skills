# Three Pillars Of Observability

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