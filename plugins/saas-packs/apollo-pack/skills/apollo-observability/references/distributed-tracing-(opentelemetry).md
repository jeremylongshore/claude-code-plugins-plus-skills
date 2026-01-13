# Distributed Tracing (Opentelemetry)

## Distributed Tracing (OpenTelemetry)

```typescript
// src/lib/apollo/tracing.ts
import { trace, Span, SpanStatusCode, context as otelContext } from '@opentelemetry/api';
import { W3CTraceContextPropagator } from '@opentelemetry/core';

const tracer = trace.getTracer('apollo-integration');
const propagator = new W3CTraceContextPropagator();

export function createApolloSpan(
  name: string,
  attributes: Record<string, any>
): Span {
  return tracer.startSpan(`apollo.${name}`, {
    attributes: {
      'apollo.endpoint': attributes.endpoint,
      'apollo.method': attributes.method,
      'service.name': 'apollo-integration',
    },
  });
}

export async function traceApolloRequest<T>(
  endpoint: string,
  requestFn: () => Promise<T>
): Promise<T> {
  const span = createApolloSpan('request', { endpoint });

  try {
    const result = await otelContext.with(
      trace.setSpan(otelContext.active(), span),
      requestFn
    );

    span.setStatus({ code: SpanStatusCode.OK });
    return result;
  } catch (error: any) {
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

// Middleware for Express
export function apolloTracingMiddleware(req: any, res: any, next: any) {
  const span = createApolloSpan('http_request', {
    endpoint: req.path,
    method: req.method,
  });

  req.apolloSpan = span;

  res.on('finish', () => {
    span.setAttribute('http.status_code', res.statusCode);
    span.end();
  });

  next();
}
```