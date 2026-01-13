# Metrics With Prometheus

## Metrics with Prometheus

```typescript
// src/lib/apollo/metrics.ts
import { Registry, Counter, Histogram, Gauge } from 'prom-client';

const register = new Registry();

// Request metrics
export const apolloRequestsTotal = new Counter({
  name: 'apollo_requests_total',
  help: 'Total number of Apollo API requests',
  labelNames: ['endpoint', 'method', 'status'],
  registers: [register],
});

export const apolloRequestDuration = new Histogram({
  name: 'apollo_request_duration_seconds',
  help: 'Duration of Apollo API requests in seconds',
  labelNames: ['endpoint', 'method'],
  buckets: [0.1, 0.25, 0.5, 1, 2.5, 5, 10],
  registers: [register],
});

// Rate limit metrics
export const apolloRateLimitRemaining = new Gauge({
  name: 'apollo_rate_limit_remaining',
  help: 'Remaining Apollo API rate limit',
  labelNames: ['endpoint'],
  registers: [register],
});

export const apolloRateLimitHits = new Counter({
  name: 'apollo_rate_limit_hits_total',
  help: 'Number of times rate limit was hit',
  registers: [register],
});

// Cache metrics
export const apolloCacheHits = new Counter({
  name: 'apollo_cache_hits_total',
  help: 'Number of Apollo cache hits',
  labelNames: ['endpoint'],
  registers: [register],
});

export const apolloCacheMisses = new Counter({
  name: 'apollo_cache_misses_total',
  help: 'Number of Apollo cache misses',
  labelNames: ['endpoint'],
  registers: [register],
});

// Credit usage
export const apolloCreditsUsed = new Counter({
  name: 'apollo_credits_used_total',
  help: 'Total Apollo credits consumed',
  labelNames: ['operation'],
  registers: [register],
});

// Error tracking
export const apolloErrors = new Counter({
  name: 'apollo_errors_total',
  help: 'Total Apollo API errors',
  labelNames: ['endpoint', 'error_type'],
  registers: [register],
});

export { register };
```

### Instrumented Client

```typescript
// src/lib/apollo/instrumented-client.ts
import { apolloRequestsTotal, apolloRequestDuration, apolloErrors } from './metrics';

export class InstrumentedApolloClient {
  async request<T>(endpoint: string, options: RequestOptions): Promise<T> {
    const labels = { endpoint, method: options.method || 'POST' };
    const endTimer = apolloRequestDuration.startTimer(labels);

    try {
      const response = await this.baseClient.request(endpoint, options);

      apolloRequestsTotal.inc({ ...labels, status: 'success' });

      // Track rate limit from headers
      const remaining = response.headers['x-ratelimit-remaining'];
      if (remaining) {
        apolloRateLimitRemaining.set({ endpoint }, parseInt(remaining));
      }

      return response.data;
    } catch (error: any) {
      const errorType = this.classifyError(error);
      apolloRequestsTotal.inc({ ...labels, status: 'error' });
      apolloErrors.inc({ endpoint, error_type: errorType });

      if (error.response?.status === 429) {
        apolloRateLimitHits.inc();
      }

      throw error;
    } finally {
      endTimer();
    }
  }

  private classifyError(error: any): string {
    const status = error.response?.status;
    if (status === 401) return 'auth_error';
    if (status === 403) return 'permission_error';
    if (status === 422) return 'validation_error';
    if (status === 429) return 'rate_limit';
    if (status >= 500) return 'server_error';
    if (error.code === 'ECONNREFUSED') return 'connection_error';
    if (error.code === 'ETIMEDOUT') return 'timeout';
    return 'unknown';
  }
}
```