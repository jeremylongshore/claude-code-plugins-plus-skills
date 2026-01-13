---
name: linear-data-handling
description: |
  Data synchronization, backup, and consistency patterns for Linear.
  Use when implementing data sync, creating backups,
  or ensuring data consistency across systems.
  Trigger with phrases like "linear data sync", "backup linear",
  "linear data consistency", "sync linear issues", "linear data export".
allowed-tools: Read, Write, Edit, Grep, Bash
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Linear Data Handling

## Overview
Implement reliable data synchronization, backup, and consistency for Linear integrations.

## Prerequisites
- Linear API access
- Database for local storage
- Understanding of eventual consistency

## Instructions

### Step 1: Data Model Mapping
```typescript
// models/linear-entities.ts
import { z } from "zod";

// Core entity schemas
export const LinearIssueSchema = z.object({
  id: z.string(),
  identifier: z.string(),
  title: z.string(),
  description: z.string().nullable(),
  priority: z.number(),
  estimate: z.number().nullable(),
  stateId: z.string(),
  stateName: z.string(),
  teamId: z.string(),
  teamKey: z.string(),
  assigneeId: z.string().nullable(),
  projectId: z.string().nullable(),
  cycleId: z.string().nullable(),
  createdAt: z.string(),
  updatedAt: z.string(),
  completedAt: z.string().nullable(),
  canceledAt: z.string().nullable(),
});

export type LinearIssue = z.infer<typeof LinearIssueSchema>;

export const LinearProjectSchema = z.object({
  id: z.string(),
  name: z.string(),
  description: z.string().nullable(),
  state: z.string(),
  progress: z.number(),
  targetDate: z.string().nullable(),
  createdAt: z.string(),
  updatedAt: z.string(),
});

export type LinearProject = z.infer<typeof LinearProjectSchema>;
```

### Step 2: Full Sync Implementation
```typescript
// sync/full-sync.ts
import { LinearClient, Issue } from "@linear/sdk";
import { db } from "../lib/database";
import { LinearIssueSchema } from "../models/linear-entities";

interface SyncStats {
  total: number;
  created: number;
  updated: number;
  deleted: number;
  errors: number;
}

export async function fullSync(client: LinearClient): Promise<SyncStats> {
  const stats: SyncStats = { total: 0, created: 0, updated: 0, deleted: 0, errors: 0 };

  console.log("Starting full sync...");

  // Fetch all issues with pagination
  const remoteIssues = new Map<string, LinearIssue>();
  let hasMore = true;
  let cursor: string | undefined;

  while (hasMore) {
    const issues = await client.issues({
      first: 100,
      after: cursor,
      includeArchived: false,
    });

    for (const issue of issues.nodes) {
      const state = await issue.state;
      const team = await issue.team;

      const mapped: LinearIssue = {
        id: issue.id,
        identifier: issue.identifier,
        title: issue.title,
        description: issue.description,
        priority: issue.priority,
        estimate: issue.estimate,
        stateId: state?.id ?? "",
        stateName: state?.name ?? "Unknown",
        teamId: team?.id ?? "",
        teamKey: team?.key ?? "",
        assigneeId: issue.assigneeId,
        projectId: issue.projectId,
        cycleId: issue.cycleId,
        createdAt: issue.createdAt.toISOString(),
        updatedAt: issue.updatedAt.toISOString(),
        completedAt: issue.completedAt?.toISOString() ?? null,
        canceledAt: issue.canceledAt?.toISOString() ?? null,
      };

      remoteIssues.set(issue.id, mapped);
    }

    hasMore = issues.pageInfo.hasNextPage;
    cursor = issues.pageInfo.endCursor;

    console.log(`  Fetched ${remoteIssues.size} issues...`);
  }

  stats.total = remoteIssues.size;

  // Get local issues
  const localIssues = await db.select().from(issuesTable);
  const localIssueMap = new Map(localIssues.map(i => [i.id, i]));

  // Process changes
  await db.transaction(async (tx) => {
    // Upsert remote issues
    for (const [id, issue] of remoteIssues) {
      const existing = localIssueMap.get(id);

      if (!existing) {
        await tx.insert(issuesTable).values(issue);
        stats.created++;
      } else if (existing.updatedAt !== issue.updatedAt) {
        await tx.update(issuesTable).set(issue).where(eq(issuesTable.id, id));
        stats.updated++;
      }
    }

    // Mark deleted issues
    for (const [id, local] of localIssueMap) {
      if (!remoteIssues.has(id) && !local.deletedAt) {
        await tx.update(issuesTable)
          .set({ deletedAt: new Date().toISOString() })
          .where(eq(issuesTable.id, id));
        stats.deleted++;
      }
    }
  });

  console.log("Full sync complete:", stats);
  return stats;
}
```

### Step 3: Incremental Sync with Webhooks
```typescript
// sync/incremental-sync.ts
import { db } from "../lib/database";

interface WebhookEvent {
  action: "create" | "update" | "remove";
  type: string;
  data: Record<string, unknown>;
  createdAt: string;
}

export async function processWebhookSync(event: WebhookEvent): Promise<void> {
  const { action, type, data } = event;

  if (type !== "Issue") return;

  const issueData = data as any;

  switch (action) {
    case "create":
      await db.insert(issuesTable).values({
        id: issueData.id,
        identifier: issueData.identifier,
        title: issueData.title,
        // ... map all fields
        syncedAt: new Date().toISOString(),
      });
      break;

    case "update":
      await db.update(issuesTable)
        .set({
          title: issueData.title,
          // ... update changed fields
          syncedAt: new Date().toISOString(),
        })
        .where(eq(issuesTable.id, issueData.id));
      break;

    case "remove":
      await db.update(issuesTable)
        .set({ deletedAt: new Date().toISOString() })
        .where(eq(issuesTable.id, issueData.id));
      break;
  }
}
```

### Step 4: Data Export/Backup
```typescript
// backup/export.ts
import { LinearClient } from "@linear/sdk";
import { createWriteStream } from "fs";
import { pipeline } from "stream/promises";

interface BackupOptions {
  includeComments?: boolean;
  includeAttachments?: boolean;
  format?: "json" | "csv";
}

export async function createBackup(
  client: LinearClient,
  outputPath: string,
  options: BackupOptions = {}
): Promise<void> {
  const { includeComments = true, format = "json" } = options;

  const backup = {
    exportedAt: new Date().toISOString(),
    version: "1.0",
    data: {
      teams: [] as any[],
      projects: [] as any[],
      cycles: [] as any[],
      issues: [] as any[],
      comments: [] as any[],
    },
  };

  console.log("Creating backup...");

  // Export teams
  const teams = await client.teams();
  backup.data.teams = await Promise.all(
    teams.nodes.map(async (team) => ({
      id: team.id,
      name: team.name,
      key: team.key,
      description: team.description,
    }))
  );
  console.log(`  Exported ${backup.data.teams.length} teams`);

  // Export projects
  const projects = await client.projects();
  backup.data.projects = projects.nodes.map(p => ({
    id: p.id,
    name: p.name,
    description: p.description,
    state: p.state,
    targetDate: p.targetDate,
  }));
  console.log(`  Exported ${backup.data.projects.length} projects`);

  // Export issues with pagination
  let cursor: string | undefined;
  let hasMore = true;

  while (hasMore) {
    const issues = await client.issues({
      first: 100,
      after: cursor,
      includeArchived: true,
    });

    for (const issue of issues.nodes) {
      const issueData: any = {
        id: issue.id,
        identifier: issue.identifier,
        title: issue.title,
        description: issue.description,
        priority: issue.priority,
        createdAt: issue.createdAt,
        updatedAt: issue.updatedAt,
      };

      if (includeComments) {
        const comments = await issue.comments();
        issueData.comments = comments.nodes.map(c => ({
          id: c.id,
          body: c.body,
          createdAt: c.createdAt,
        }));
      }

      backup.data.issues.push(issueData);
    }

    hasMore = issues.pageInfo.hasNextPage;
    cursor = issues.pageInfo.endCursor;
  }
  console.log(`  Exported ${backup.data.issues.length} issues`);

  // Write to file
  const output = format === "json"
    ? JSON.stringify(backup, null, 2)
    : convertToCSV(backup);

  await fs.writeFile(outputPath, output);
  console.log(`Backup saved to ${outputPath}`);
}
```

### Step 5: Data Consistency Checks
```typescript
// sync/consistency-check.ts
import { LinearClient } from "@linear/sdk";
import { db } from "../lib/database";

interface ConsistencyReport {
  timestamp: string;
  issues: {
    total: number;
    missing: string[];
    stale: string[];
    orphaned: string[];
  };
}

export async function checkConsistency(client: LinearClient): Promise<ConsistencyReport> {
  const report: ConsistencyReport = {
    timestamp: new Date().toISOString(),
    issues: {
      total: 0,
      missing: [],
      stale: [],
      orphaned: [],
    },
  };

  // Get sample of remote issues
  const remoteIssues = await client.issues({ first: 100 });
  report.issues.total = remoteIssues.nodes.length;

  // Check each remote issue exists locally
  for (const remote of remoteIssues.nodes) {
    const local = await db.query.issues.findFirst({
      where: eq(issues.id, remote.id),
    });

    if (!local) {
      report.issues.missing.push(remote.identifier);
    } else if (new Date(local.updatedAt) < remote.updatedAt) {
      report.issues.stale.push(remote.identifier);
    }
  }

  // Check for orphaned local issues
  const localIssues = await db.select({ id: issues.id, identifier: issues.identifier })
    .from(issues)
    .where(isNull(issues.deletedAt))
    .limit(100);

  for (const local of localIssues) {
    try {
      await client.issue(local.id);
    } catch {
      report.issues.orphaned.push(local.identifier);
    }
  }

  return report;
}

// Run periodically
export async function scheduleConsistencyChecks(): Promise<void> {
  cron.schedule("0 0 * * *", async () => {
    const client = new LinearClient({ apiKey: process.env.LINEAR_API_KEY! });
    const report = await checkConsistency(client);

    if (report.issues.missing.length > 0 || report.issues.stale.length > 10) {
      await alertOncall("Data consistency issues detected", report);
      await fullSync(client); // Trigger resync
    }
  });
}
```

### Step 6: Conflict Resolution
```typescript
// sync/conflict-resolution.ts
interface ConflictStrategy {
  strategy: "remote-wins" | "local-wins" | "merge" | "manual";
  mergeFields?: string[];
}

export async function resolveConflict(
  local: LinearIssue,
  remote: LinearIssue,
  config: ConflictStrategy
): Promise<LinearIssue> {
  switch (config.strategy) {
    case "remote-wins":
      return remote;

    case "local-wins":
      return local;

    case "merge":
      // Merge specific fields
      const merged = { ...remote };
      for (const field of config.mergeFields ?? []) {
        if (local[field as keyof LinearIssue] !== undefined) {
          (merged as any)[field] = local[field as keyof LinearIssue];
        }
      }
      return merged;

    case "manual":
      throw new ConflictError(local, remote);

    default:
      return remote;
  }
}
```

## Error Handling
| Error | Cause | Solution |
|-------|-------|----------|
| `Sync timeout` | Too many records | Use smaller batches |
| `Conflict detected` | Concurrent edits | Apply conflict resolution |
| `Stale data` | Missed webhooks | Trigger full sync |
| `Export failed` | API rate limit | Add delays between requests |

## Resources
- [Linear GraphQL API](https://developers.linear.app/docs/graphql/working-with-the-graphql-api)
- [Data Sync Patterns](https://martinfowler.com/articles/patterns-of-distributed-systems/)
- [Eventual Consistency](https://en.wikipedia.org/wiki/Eventual_consistency)

## Next Steps
Implement enterprise RBAC with `linear-enterprise-rbac`.
