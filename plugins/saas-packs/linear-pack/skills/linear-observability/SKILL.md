---
name: linear-observability
license: MIT
allowed-tools: Read, Write, Edit, Grep
description: Implement monitoring, logging, and alerting for linear integrations.
  use when setting up metrics collection, creating dashboards, or configuring alerts
  for linear api usage. trigger with phrases like "linear monitoring", "linear observability",
  "l...
---
# Linear Observability

## Overview
Comprehensive monitoring, logging, and alerting for Linear integrations.

## Prerequisites
- Linear integration deployed
- Metrics infrastructure (Prometheus, Datadog, etc.)
- Logging infrastructure (ELK, CloudWatch, etc.)
- Alerting system configured

## Instructions

### Step 1: Metrics Collection
```typescript
// lib/metrics.ts
import { Counter, Histogram, Gauge, Registry } from "prom-client";

const registry = new Registry();

// Request metrics
export const linearRequestsTotal = new Counter({
  name: "linear_api_requests_total",
  help: "Total Linear API requests",
  labelNames: ["operation", "status"],
  registers: [registry],
});

export const linearRequestDuration = new Histogram({
  name: "linear_api_request_duration_seconds",
  help: "Linear API request duration in seconds",
  labelNames: ["operation"],
  buckets: [0.1, 0.25, 0.5, 1, 2.5, 5, 10],
  registers: [registry],
});

export const linearComplexityCost = new Histogram({
  name: "linear_api_complexity_cost",
  help: "Linear API query complexity cost",
  labelNames: ["operation"],
  buckets: [10, 50, 100, 250, 500, 1000, 2500],
  registers: [registry],
});

// Rate limit metrics
export const linearRateLimitRemaining = new Gauge({
  name: "linear_rate_limit_remaining",
  help: "Remaining Linear API rate limit",
  registers: [registry],
});

export const linearComplexityRemaining = new Gauge({
  name: "linear_complexity_remaining",
  help: "Remaining Linear complexity quota",
  registers: [registry],
});

// Webhook metrics
export const linearWebhooksReceived = new Counter({
  name: "linear_webhooks_received_total",
  help: "Total Linear webhooks received",
  labelNames: ["type", "action"],
  registers: [registry],
});

export const linearWebhookProcessingDuration = new Histogram({
  name: "linear_webhook_processing_duration_seconds",
  help: "Linear webhook processing duration",
  labelNames: ["type"],
  buckets: [0.01, 0.05, 0.1, 0.25, 0.5, 1, 2.5],
  registers: [registry],
});

// Cache metrics
export const linearCacheHits = new Counter({
  name: "linear_cache_hits_total",
  help: "Total Linear cache hits",
  registers: [registry],
});

export const linearCacheMisses = new Counter({
  name: "linear_cache_misses_total",
  help: "Total Linear cache misses",
  registers: [registry],
});

export { registry };
```

### Step 2: Instrumented Client Wrapper
```typescript
// lib/instrumented-client.ts
import { LinearClient } from "@linear/sdk";
import {
  linearRequestsTotal,
  linearRequestDuration,
  linearRateLimitRemaining,
  linearComplexityRemaining,
} from "./metrics";

export function createInstrumentedClient(apiKey: string): LinearClient {
  const client = new LinearClient({
    apiKey,
    fetch: async (url, init) => {
      const operation = extractOperationName(init?.body);
      const timer = linearRequestDuration.startTimer({ operation });

      try {
        const response = await fetch(url, init);

        // Record rate limit headers
        const remaining = response.headers.get("x-ratelimit-remaining");
        const complexity = response.headers.get("x-complexity-remaining");

        if (remaining) linearRateLimitRemaining.set(parseInt(remaining));
        if (complexity) linearComplexityRemaining.set(parseInt(complexity));

        // Record success/failure
        const status = response.ok ? "success" : "error";
        linearRequestsTotal.inc({ operation, status });

        timer();
        return response;
      } catch (error) {
        linearRequestsTotal.inc({ operation, status: "error" });
        timer();
        throw error;
      }
    },
  });

  return client;
}

function extractOperationName(body: BodyInit | undefined): string {
  if (!body || typeof body !== "string") return "unknown";

  try {
    const parsed = JSON.parse(body);
    // Extract operation name from GraphQL query
    const match = parsed.query?.match(/(?:query|mutation)\s+(\w+)/);
    return match?.[1] || "anonymous";
  } catch {
    return "unknown";
  }
}
```

### Step 3: Structured Logging
```typescript
// lib/logger.ts
import pino from "pino";

export const logger = pino({
  level: process.env.LOG_LEVEL || "info",
  formatters: {
    level: (label) => ({ level: label }),
  },
  base: {
    service: "linear-integration",
    environment: process.env.NODE_ENV,
  },
});

// Linear-specific logger
export const linearLogger = logger.child({ component: "linear" });

// Log API calls
export function logApiCall(operation: string, duration: number, success: boolean) {
  linearLogger.info({
    event: "api_call",
    operation,
    duration_ms: duration,
    success,
  });
}

// Log webhook events
export function logWebhook(type: string, action: string, id: string) {
  linearLogger.info({
    event: "webhook_received",
    webhook_type: type,
    webhook_action: action,
    entity_id: id,
  });
}

// Log errors with context
export function logError(error: Error, context: Record<string, unknown>) {
  linearLogger.error({
    event: "error",
    error_message: error.message,
    error_stack: error.stack,
    ...context,
  });
}
```

### Step 4: Health Check Endpoint
```typescript
// api/health.ts
import { LinearClient } from "@linear/sdk";
import { registry } from "../lib/metrics";

interface HealthStatus {
  status: "healthy" | "degraded" | "unhealthy";
  checks: {
    linear_api: { status: string; latency_ms?: number; error?: string };
    cache: { status: string; hit_rate?: number };
    rate_limit: { status: string; remaining?: number; percentage?: number };
  };
  timestamp: string;
}

export async function healthCheck(client: LinearClient): Promise<HealthStatus> {
  const checks: HealthStatus["checks"] = {
    linear_api: { status: "unknown" },
    cache: { status: "unknown" },
    rate_limit: { status: "unknown" },
  };

  // Check Linear API
  const start = Date.now();
  try {
    await client.viewer;
    checks.linear_api = {
      status: "healthy",
      latency_ms: Date.now() - start,
    };
  } catch (error) {
    checks.linear_api = {
      status: "unhealthy",
      error: error instanceof Error ? error.message : "Unknown error",
    };
  }

  // Check rate limit status
  const metrics = await registry.getMetricsAsJSON();
  const rateLimitMetric = metrics.find(m => m.name === "linear_rate_limit_remaining");
  if (rateLimitMetric) {
    const remaining = (rateLimitMetric as any).values?.[0]?.value || 0;
    const percentage = (remaining / 1500) * 100;
    checks.rate_limit = {
      status: percentage > 10 ? "healthy" : percentage > 5 ? "degraded" : "unhealthy",
      remaining,
      percentage: Math.round(percentage),
    };
  }

  // Determine overall status
  const statuses = Object.values(checks).map(c => c.status);
  let status: HealthStatus["status"] = "healthy";
  if (statuses.includes("unhealthy")) status = "unhealthy";
  else if (statuses.includes("degraded")) status = "degraded";

  return {
    status,
    checks,
    timestamp: new Date().toISOString(),
  };
}
```

### Step 5: Alerting Rules
```yaml
# prometheus/alerts.yml
groups:
  - name: linear-integration
    rules:
      # High error rate
      - alert: LinearHighErrorRate
        expr: |
          sum(rate(linear_api_requests_total{status="error"}[5m]))
          / sum(rate(linear_api_requests_total[5m])) > 0.05
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: High Linear API error rate
          description: "Linear API error rate is {{ $value | humanizePercentage }}"

      # Rate limit approaching
      - alert: LinearRateLimitLow
        expr: linear_rate_limit_remaining < 100
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: Linear rate limit running low
          description: "Only {{ $value }} requests remaining in rate limit window"

      # Slow API responses
      - alert: LinearSlowResponses
        expr: |
          histogram_quantile(0.95, rate(linear_api_request_duration_seconds_bucket[5m])) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: Slow Linear API responses
          description: "95th percentile response time is {{ $value }}s"

      # Webhook processing errors
      - alert: LinearWebhookErrors
        expr: |
          sum(rate(linear_webhooks_received_total{status="error"}[5m])) > 0.1
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: Linear webhook processing errors
          description: "Webhook error rate: {{ $value }} per second"
```

### Step 6: Grafana Dashboard
```json
{
  "dashboard": {
    "title": "Linear Integration",
    "panels": [
      {
        "title": "API Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(linear_api_requests_total[5m])) by (status)",
            "legendFormat": "{{ status }}"
          }
        ]
      },
      {
        "title": "Request Latency (p95)",
        "type": "gauge",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(linear_api_request_duration_seconds_bucket[5m]))"
          }
        ]
      },
      {
        "title": "Rate Limit Remaining",
        "type": "stat",
        "targets": [
          {
            "expr": "linear_rate_limit_remaining"
          }
        ]
      },
      {
        "title": "Webhooks by Type",
        "type": "piechart",
        "targets": [
          {
            "expr": "sum(linear_webhooks_received_total) by (type)"
          }
        ]
      }
    ]
  }
}
```

## Error Handling
| Error | Cause | Solution |
|-------|-------|----------|
| `Metrics not collecting` | Missing instrumentation | Add metrics to client wrapper |
| `Alerts not firing` | Wrong threshold | Adjust alert thresholds |
| `Missing labels` | Logger misconfigured | Check logger configuration |

## Resources
- [Prometheus Client Library](https://github.com/siimon/prom-client)
- [Grafana Dashboards](https://grafana.com/docs/grafana/latest/dashboards/)
- [Pino Logger](https://getpino.io/)

## Next Steps
Create incident runbooks with `linear-incident-runbook`.
