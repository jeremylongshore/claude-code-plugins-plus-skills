---
name: linear-cost-tuning
license: MIT
allowed-tools: Read, Write, Edit, Grep
description: Optimize Linear API usage and manage costs effectively. Use when reducing
  API calls, managing rate limits efficiently, or optimizing integration costs. Trigger
  with phrases like "linear cost", "reduce linear API calls", "linear efficiency",
  "linea...
---
# Linear Cost Tuning

## Overview
Optimize Linear API usage to maximize efficiency and minimize costs.

## Prerequisites
- Working Linear integration
- Monitoring in place
- Understanding of usage patterns

## Cost Factors

### API Request Costs
| Factor | Impact | Optimization Strategy |
|--------|--------|----------------------|
| Request count | Direct rate limit | Batch operations |
| Query complexity | Complexity limit | Minimal field selection |
| Payload size | Bandwidth/latency | Pagination, filtering |
| Webhook volume | Processing costs | Event filtering |

## Instructions

### Step 1: Audit Current Usage
```typescript
// lib/usage-tracker.ts
interface UsageStats {
  requests: number;
  complexity: number;
  bytesTransferred: number;
  period: { start: Date; end: Date };
}

class UsageTracker {
  private stats: UsageStats = {
    requests: 0,
    complexity: 0,
    bytesTransferred: 0,
    period: { start: new Date(), end: new Date() },
  };

  recordRequest(complexity: number, bytes: number): void {
    this.stats.requests++;
    this.stats.complexity += complexity;
    this.stats.bytesTransferred += bytes;
    this.stats.period.end = new Date();
  }

  getStats(): UsageStats {
    return { ...this.stats };
  }

  getDaily(): {
    avgRequestsPerHour: number;
    avgComplexityPerRequest: number;
    projectedMonthlyRequests: number;
  } {
    const hours =
      (this.stats.period.end.getTime() - this.stats.period.start.getTime()) /
      (1000 * 60 * 60);

    return {
      avgRequestsPerHour: this.stats.requests / Math.max(hours, 1),
      avgComplexityPerRequest: this.stats.complexity / Math.max(this.stats.requests, 1),
      projectedMonthlyRequests: (this.stats.requests / Math.max(hours, 1)) * 24 * 30,
    };
  }

  reset(): void {
    this.stats = {
      requests: 0,
      complexity: 0,
      bytesTransferred: 0,
      period: { start: new Date(), end: new Date() },
    };
  }
}

export const usageTracker = new UsageTracker();
```

### Step 2: Reduce Request Volume

**Polling vs Webhooks:**
```typescript
// BAD: Polling every minute
setInterval(async () => {
  const issues = await client.issues({ first: 100 });
  await syncIssues(issues.nodes);
}, 60000);

// GOOD: Use webhooks for real-time updates
// See linear-webhooks-events skill
app.post("/webhooks/linear", async (req, res) => {
  const event = req.body;
  await handleEvent(event);
  res.sendStatus(200);
});
```

**Conditional Fetching:**
```typescript
// lib/conditional-fetch.ts
interface ETagCache {
  data: any;
  etag: string;
  timestamp: Date;
}

const etagCache = new Map<string, ETagCache>();

async function fetchWithETag(key: string, fetcher: () => Promise<any>) {
  const cached = etagCache.get(key);

  // Only fetch if cache is stale (> 5 minutes)
  if (cached && Date.now() - cached.timestamp.getTime() < 5 * 60 * 1000) {
    return cached.data;
  }

  const data = await fetcher();
  etagCache.set(key, {
    data,
    etag: JSON.stringify(data).slice(0, 50), // Simple hash
    timestamp: new Date(),
  });

  return data;
}
```

### Step 3: Optimize Query Complexity

**Calculate Complexity:**
```typescript
// Linear complexity estimation
// - Each field costs 1
// - Each connection costs 1 + (first * child_complexity)
// - Nested connections multiply

// BAD: High complexity query (~500 complexity)
const expensiveQuery = `
  query {
    issues(first: 50) {
      nodes {
        id
        title
        assignee { name }
        labels { nodes { name } }
        comments(first: 10) {
          nodes { body user { name } }
        }
      }
    }
  }
`;

// GOOD: Low complexity query (~100 complexity)
const cheapQuery = `
  query {
    issues(first: 50) {
      nodes {
        id
        identifier
        title
        priority
      }
    }
  }
`;
```

### Step 4: Implement Request Coalescing
```typescript
// lib/coalesce.ts
class RequestCoalescer {
  private pending = new Map<string, Promise<any>>();

  async execute<T>(key: string, fn: () => Promise<T>): Promise<T> {
    // If same request is already in flight, reuse it
    const existing = this.pending.get(key);
    if (existing) {
      return existing;
    }

    const promise = fn().finally(() => {
      this.pending.delete(key);
    });

    this.pending.set(key, promise);
    return promise;
  }
}

const coalescer = new RequestCoalescer();

// Multiple simultaneous calls reuse the same request
const [teams1, teams2, teams3] = await Promise.all([
  coalescer.execute("teams", () => client.teams()),
  coalescer.execute("teams", () => client.teams()), // Reuses first request
  coalescer.execute("teams", () => client.teams()), // Reuses first request
]);
```

### Step 5: Webhook Event Filtering
```typescript
// Only process relevant events
async function shouldProcessEvent(event: any): boolean {
  // Skip events from bots
  if (event.data?.actor?.isBot) return false;

  // Only process certain issue states
  if (event.type === "Issue" && event.action === "update") {
    const importantFields = ["state", "priority", "assignee"];
    const changedFields = Object.keys(event.updatedFrom || {});

    if (!changedFields.some(f => importantFields.includes(f))) {
      return false; // Skip trivial updates
    }
  }

  // Only process issues from specific teams
  const allowedTeams = ["ENG", "PROD"];
  if (event.data?.team?.key && !allowedTeams.includes(event.data.team.key)) {
    return false;
  }

  return true;
}
```

### Step 6: Lazy Loading Pattern
```typescript
// lib/lazy-client.ts
class LazyLinearClient {
  private client: LinearClient;
  private teamsCache: any[] | null = null;
  private statesCache = new Map<string, any[]>();

  constructor(apiKey: string) {
    this.client = new LinearClient({ apiKey });
  }

  async getTeams() {
    if (!this.teamsCache) {
      const teams = await this.client.teams();
      this.teamsCache = teams.nodes;
    }
    return this.teamsCache;
  }

  async getStatesForTeam(teamKey: string) {
    if (!this.statesCache.has(teamKey)) {
      const teams = await this.client.teams({
        filter: { key: { eq: teamKey } },
      });
      const states = await teams.nodes[0].states();
      this.statesCache.set(teamKey, states.nodes);
    }
    return this.statesCache.get(teamKey)!;
  }

  // Invalidate on known changes
  invalidateTeams() {
    this.teamsCache = null;
    this.statesCache.clear();
  }
}
```

## Cost Reduction Checklist
- [ ] Replace polling with webhooks
- [ ] Implement request caching
- [ ] Use request coalescing
- [ ] Filter webhook events
- [ ] Minimize query complexity
- [ ] Batch related operations
- [ ] Use lazy loading for static data
- [ ] Monitor and track usage

## Monitoring Dashboard
```typescript
// Example metrics to track
const metrics = {
  // Request metrics
  totalRequests: counter("linear_requests_total"),
  requestDuration: histogram("linear_request_duration_seconds"),
  complexityCost: histogram("linear_complexity_cost"),

  // Cache metrics
  cacheHits: counter("linear_cache_hits_total"),
  cacheMisses: counter("linear_cache_misses_total"),

  // Webhook metrics
  webhooksReceived: counter("linear_webhooks_received_total"),
  webhooksFiltered: counter("linear_webhooks_filtered_total"),
};
```

## Resources
- [Linear Rate Limiting](https://developers.linear.app/docs/graphql/rate-limiting)
- [Query Complexity Guide](https://developers.linear.app/docs/graphql/complexity)
- [Webhook Best Practices](https://developers.linear.app/docs/graphql/webhooks)

## Next Steps
Learn production architecture with `linear-reference-architecture`.
