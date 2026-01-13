# Implementation Guide

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