# Structured Logging

## Structured Logging

```typescript
// src/lib/apollo/logger.ts
import pino from 'pino';

const logger = pino({
  level: process.env.LOG_LEVEL || 'info',
  formatters: {
    level: (label) => ({ level: label }),
  },
  redact: {
    paths: ['api_key', '*.email', '*.phone', 'headers.authorization'],
    censor: '[REDACTED]',
  },
  base: {
    service: 'apollo-integration',
    environment: process.env.NODE_ENV,
  },
});

export const apolloLogger = logger.child({ component: 'apollo' });

// Request/response logging
export function logApolloRequest(context: {
  endpoint: string;
  method: string;
  params?: object;
  requestId: string;
}): void {
  apolloLogger.info({
    type: 'apollo_request',
    ...context,
    timestamp: new Date().toISOString(),
  });
}

export function logApolloResponse(context: {
  endpoint: string;
  status: number;
  durationMs: number;
  requestId: string;
  resultCount?: number;
}): void {
  apolloLogger.info({
    type: 'apollo_response',
    ...context,
    timestamp: new Date().toISOString(),
  });
}

export function logApolloError(context: {
  endpoint: string;
  error: Error;
  requestId: string;
  retryCount?: number;
}): void {
  apolloLogger.error({
    type: 'apollo_error',
    endpoint: context.endpoint,
    error: {
      name: context.error.name,
      message: context.error.message,
      stack: context.error.stack,
    },
    requestId: context.requestId,
    retryCount: context.retryCount,
    timestamp: new Date().toISOString(),
  });
}
```