---
name: linear-sdk-patterns
license: MIT
allowed-tools: Read, Write, Edit, Grep
description: Typescript/javascript sdk patterns and best practices for linear. use
  when learning sdk idioms, implementing common patterns, or optimizing linear api
  usage. trigger with phrases like "linear sdk patterns", "linear best practices",
  "linear typescr...
---
# Linear SDK Patterns

## Overview
Essential patterns and best practices for working with the Linear SDK.

## Prerequisites
- Linear SDK installed and configured
- TypeScript project setup
- Understanding of async/await patterns

## Core Patterns

### Pattern 1: Client Singleton
```typescript
// lib/linear.ts
import { LinearClient } from "@linear/sdk";

let client: LinearClient | null = null;

export function getLinearClient(): LinearClient {
  if (!client) {
    if (!process.env.LINEAR_API_KEY) {
      throw new Error("LINEAR_API_KEY environment variable not set");
    }
    client = new LinearClient({
      apiKey: process.env.LINEAR_API_KEY,
    });
  }
  return client;
}
```

### Pattern 2: Pagination Handling
```typescript
import { LinearClient, Issue, IssueConnection } from "@linear/sdk";

async function* getAllIssues(
  client: LinearClient,
  filter?: Record<string, unknown>
): AsyncGenerator<Issue> {
  let hasNextPage = true;
  let endCursor: string | undefined;

  while (hasNextPage) {
    const connection: IssueConnection = await client.issues({
      filter,
      first: 50, // Max per page
      after: endCursor,
    });

    for (const issue of connection.nodes) {
      yield issue;
    }

    hasNextPage = connection.pageInfo.hasNextPage;
    endCursor = connection.pageInfo.endCursor;
  }
}

// Usage
for await (const issue of getAllIssues(client, { state: { name: { eq: "Todo" } } })) {
  console.log(issue.identifier, issue.title);
}
```

### Pattern 3: Error Handling Wrapper
```typescript
import { LinearClient, LinearError } from "@linear/sdk";

interface LinearResult<T> {
  success: boolean;
  data?: T;
  error?: {
    message: string;
    code?: string;
    retryable: boolean;
  };
}

async function linearOperation<T>(
  operation: () => Promise<T>
): Promise<LinearResult<T>> {
  try {
    const data = await operation();
    return { success: true, data };
  } catch (error) {
    if (error instanceof LinearError) {
      return {
        success: false,
        error: {
          message: error.message,
          code: error.type,
          retryable: error.type === "RateLimitedError",
        },
      };
    }
    return {
      success: false,
      error: {
        message: error instanceof Error ? error.message : "Unknown error",
        retryable: false,
      },
    };
  }
}

// Usage
const result = await linearOperation(() => client.createIssue({
  teamId: team.id,
  title: "New issue",
}));

if (result.success) {
  console.log("Issue created:", result.data);
} else if (result.error?.retryable) {
  // Implement retry logic
}
```

### Pattern 4: Batch Operations
```typescript
async function batchUpdateIssues(
  client: LinearClient,
  issueIds: string[],
  update: { stateId?: string; priority?: number }
): Promise<{ success: number; failed: number }> {
  const results = await Promise.allSettled(
    issueIds.map(id => client.updateIssue(id, update))
  );

  return {
    success: results.filter(r => r.status === "fulfilled").length,
    failed: results.filter(r => r.status === "rejected").length,
  };
}
```

### Pattern 5: Caching Layer
```typescript
interface CacheEntry<T> {
  data: T;
  expiresAt: number;
}

class LinearCache {
  private cache = new Map<string, CacheEntry<unknown>>();
  private ttl: number;

  constructor(ttlSeconds = 60) {
    this.ttl = ttlSeconds * 1000;
  }

  async get<T>(key: string, fetcher: () => Promise<T>): Promise<T> {
    const cached = this.cache.get(key) as CacheEntry<T> | undefined;

    if (cached && cached.expiresAt > Date.now()) {
      return cached.data;
    }

    const data = await fetcher();
    this.cache.set(key, { data, expiresAt: Date.now() + this.ttl });
    return data;
  }

  invalidate(key: string): void {
    this.cache.delete(key);
  }
}

// Usage
const cache = new LinearCache(300); // 5 minute TTL

const teams = await cache.get("teams", () => client.teams());
```

### Pattern 6: Type-Safe Filters
```typescript
import { IssueFilter } from "@linear/sdk";

function buildIssueFilter(options: {
  teamKeys?: string[];
  states?: string[];
  assigneeId?: string;
  priority?: number[];
}): IssueFilter {
  const filter: IssueFilter = {};

  if (options.teamKeys?.length) {
    filter.team = { key: { in: options.teamKeys } };
  }

  if (options.states?.length) {
    filter.state = { name: { in: options.states } };
  }

  if (options.assigneeId) {
    filter.assignee = { id: { eq: options.assigneeId } };
  }

  if (options.priority?.length) {
    filter.priority = { in: options.priority };
  }

  return filter;
}
```

## Output
- Reusable client singleton
- Pagination iterator for large datasets
- Type-safe error handling
- Efficient batch operations
- Caching for performance

## Error Handling
| Error | Cause | Solution |
|-------|-------|----------|
| `Type mismatch` | SDK version incompatibility | Update @linear/sdk package |
| `Undefined property` | Nullable field access | Use optional chaining (?.) |
| `Promise rejection` | Unhandled async error | Wrap in try/catch or use wrapper |

## Resources
- [Linear SDK TypeScript](https://developers.linear.app/docs/sdk/getting-started)
- [GraphQL Schema Reference](https://developers.linear.app/docs/graphql/schema)
- [TypeScript Generics](https://www.typescriptlang.org/docs/handbook/2/generics.html)

## Next Steps
Apply these patterns in `linear-core-workflow-a` for issue management.
