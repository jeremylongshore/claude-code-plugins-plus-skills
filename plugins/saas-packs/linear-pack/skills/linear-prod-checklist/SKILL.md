---
name: linear-prod-checklist
license: MIT
allowed-tools: Read, Write, Edit, Grep
description: Production readiness checklist for linear integrations. use when preparing
  to deploy a linear integration to production, reviewing production requirements,
  or auditing existing deployments. trigger with phrases like "linear production checklist",
  ...
---
# Linear Production Checklist

## Overview
Comprehensive checklist for deploying Linear integrations to production.

## Prerequisites
- Working development integration
- Production Linear workspace
- Deployment infrastructure ready

## Pre-Production Checklist

### 1. Authentication & Security
```
[ ] Production API key generated (separate from dev)
[ ] API key stored in secure secret management (not .env files)
[ ] OAuth credentials configured for production redirect URIs
[ ] Webhook secrets are unique per environment
[ ] All secrets rotated from development values
[ ] HTTPS enforced for all endpoints
[ ] Webhook signature verification implemented
```

### 2. Error Handling
```
[ ] All API errors caught and handled gracefully
[ ] Rate limiting with exponential backoff implemented
[ ] Timeout handling for long-running operations
[ ] Graceful degradation when Linear is unavailable
[ ] Error logging with context (no secrets in logs)
[ ] Alerts configured for critical errors
```

### 3. Performance
```
[ ] Pagination implemented for all list queries
[ ] Caching layer for frequently accessed data
[ ] Request batching for bulk operations
[ ] Query complexity monitored and optimized
[ ] Connection pooling configured
[ ] Response times monitored
```

### 4. Monitoring & Observability
```
[ ] Health check endpoint implemented
[ ] API latency metrics collected
[ ] Error rate monitoring configured
[ ] Rate limit usage tracked
[ ] Structured logging implemented
[ ] Distributed tracing (if applicable)
```

### 5. Data Handling
```
[ ] No PII logged or exposed
[ ] Data retention policies defined
[ ] Backup strategy for synced data
[ ] Webhook event idempotency handled
[ ] Stale data detection and refresh
```

### 6. Infrastructure
```
[ ] Deployment pipeline configured
[ ] Rollback procedure documented
[ ] Auto-scaling configured (if needed)
[ ] Load testing completed
[ ] Disaster recovery plan documented
```

## Production Configuration Template

```typescript
// config/production.ts
import { LinearClient } from "@linear/sdk";

export const config = {
  linear: {
    // Use secret manager, not environment variables directly
    apiKey: await getSecret("linear-api-key-prod"),
    webhookSecret: await getSecret("linear-webhook-secret-prod"),
  },
  rateLimit: {
    maxRetries: 5,
    baseDelayMs: 1000,
    maxDelayMs: 30000,
  },
  cache: {
    ttlSeconds: 300, // 5 minutes
    maxEntries: 1000,
  },
  timeouts: {
    requestMs: 30000,
    webhookProcessingMs: 5000,
  },
};

export function createProductionClient(): LinearClient {
  return new LinearClient({
    apiKey: config.linear.apiKey,
    // Add production-specific configuration
  });
}
```

## Health Check Implementation

```typescript
// health/linear.ts
import { LinearClient } from "@linear/sdk";

interface HealthStatus {
  status: "healthy" | "degraded" | "unhealthy";
  latencyMs: number;
  details: {
    authentication: boolean;
    apiReachable: boolean;
    rateLimitOk: boolean;
  };
  timestamp: string;
}

export async function checkHealth(client: LinearClient): Promise<HealthStatus> {
  const start = Date.now();
  const details = {
    authentication: false,
    apiReachable: false,
    rateLimitOk: true,
  };

  try {
    // Test authentication
    const viewer = await client.viewer;
    details.authentication = true;
    details.apiReachable = true;

    // Check if we're close to rate limits
    // (Would need to track this from headers)

    return {
      status: "healthy",
      latencyMs: Date.now() - start,
      details,
      timestamp: new Date().toISOString(),
    };
  } catch (error: any) {
    details.apiReachable = error.type !== "NetworkError";

    return {
      status: "unhealthy",
      latencyMs: Date.now() - start,
      details,
      timestamp: new Date().toISOString(),
    };
  }
}
```

## Deployment Verification Script

```typescript
// scripts/verify-deployment.ts
import { LinearClient } from "@linear/sdk";

async function verifyDeployment(): Promise<void> {
  console.log("Verifying Linear integration deployment...\n");

  const checks: { name: string; check: () => Promise<boolean> }[] = [
    {
      name: "Environment variables set",
      check: async () => {
        return !!(
          process.env.LINEAR_API_KEY &&
          process.env.LINEAR_WEBHOOK_SECRET
        );
      },
    },
    {
      name: "API authentication works",
      check: async () => {
        const client = new LinearClient({
          apiKey: process.env.LINEAR_API_KEY!,
        });
        await client.viewer;
        return true;
      },
    },
    {
      name: "Can access teams",
      check: async () => {
        const client = new LinearClient({
          apiKey: process.env.LINEAR_API_KEY!,
        });
        const teams = await client.teams();
        return teams.nodes.length > 0;
      },
    },
    {
      name: "Webhook endpoint reachable",
      check: async () => {
        const response = await fetch(
          `${process.env.APP_URL}/webhooks/linear`,
          { method: "GET" }
        );
        return response.status !== 404;
      },
    },
  ];

  let passed = 0;
  let failed = 0;

  for (const { name, check } of checks) {
    try {
      const result = await check();
      if (result) {
        console.log(`✓ ${name}`);
        passed++;
      } else {
        console.log(`✗ ${name}`);
        failed++;
      }
    } catch (error) {
      console.log(`✗ ${name}: ${error}`);
      failed++;
    }
  }

  console.log(`\nResults: ${passed} passed, ${failed} failed`);

  if (failed > 0) {
    process.exit(1);
  }
}

verifyDeployment();
```

## Post-Deployment Monitoring

```typescript
// Monitor key metrics after deployment
const ALERTS = {
  errorRateThreshold: 0.01, // 1% error rate
  latencyP99Threshold: 2000, // 2 seconds
  rateLimitRemainingThreshold: 100,
};

// Set up alerts for:
// - Error rate exceeds threshold
// - P99 latency exceeds threshold
// - Rate limit remaining drops below threshold
// - Authentication failures spike
```

## Rollback Procedure

```markdown
## Rollback Steps

1. Identify the issue and confirm rollback is needed
2. Switch to previous deployment version
3. Verify Linear API connectivity with old version
4. Monitor error rates for 15 minutes
5. If stable, investigate root cause
6. Document incident in post-mortem
```

## Resources
- [Linear API Status](https://status.linear.app)
- [Linear Security Practices](https://linear.app/security)
- [API Changelog](https://developers.linear.app/docs/changelog)

## Next Steps
Learn SDK upgrade strategies with `linear-upgrade-migration`.
