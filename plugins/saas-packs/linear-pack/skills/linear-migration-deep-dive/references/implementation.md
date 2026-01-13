# Implementation Guide

### Step 1: Export from Source System

**Jira Export:**
```typescript
// migration/jira-export.ts
import JiraClient from "jira-client";

const jira = new JiraClient({
  host: process.env.JIRA_HOST,
  basic_auth: {
    email: process.env.JIRA_EMAIL,
    api_token: process.env.JIRA_API_TOKEN,
  },
});

interface JiraIssue {
  key: string;
  fields: {
    summary: string;
    description: string;
    status: { name: string };
    priority: { name: string };
    issuetype: { name: string };
    assignee: { emailAddress: string } | null;
    reporter: { emailAddress: string };
    created: string;
    updated: string;
    parent?: { key: string };
    subtasks: { key: string }[];
    labels: string[];
    customfield_10001?: number; // Story points
  };
}

export async function exportJiraProject(projectKey: string): Promise<JiraIssue[]> {
  const issues: JiraIssue[] = [];
  let startAt = 0;
  const maxResults = 100;

  while (true) {
    const result = await jira.searchJira(
      `project = ${projectKey} ORDER BY created ASC`,
      {
        startAt,
        maxResults,
        fields: [
          "summary",
          "description",
          "status",
          "priority",
          "issuetype",
          "assignee",
          "reporter",
          "created",
          "updated",
          "parent",
          "subtasks",
          "labels",
          "customfield_10001", // Story points
        ],
      }
    );

    issues.push(...result.issues);

    if (issues.length >= result.total) break;
    startAt += maxResults;

    console.log(`Exported ${issues.length}/${result.total} issues...`);
  }

  // Save to file for backup
  await fs.writeFile(
    `jira-export-${projectKey}-${Date.now()}.json`,
    JSON.stringify(issues, null, 2)
  );

  return issues;
}
```

**Asana Export:**
```typescript
// migration/asana-export.ts
import Asana from "asana";

const asana = Asana.Client.create().useAccessToken(process.env.ASANA_TOKEN);

export async function exportAsanaProject(projectGid: string) {
  const tasks = [];

  const result = await asana.tasks.getTasks({
    project: projectGid,
    opt_fields: [
      "name",
      "notes",
      "assignee",
      "due_on",
      "completed",
      "memberships.section.name",
      "tags.name",
      "parent.gid",
      "subtasks.gid",
      "created_at",
      "modified_at",
    ],
  });

  for await (const task of result) {
    tasks.push(task);
  }

  return tasks;
}
```

### Step 2: Transform Data

```typescript
// migration/transform.ts
import { LinearClient } from "@linear/sdk";

interface LinearIssueInput {
  teamId: string;
  title: string;
  description?: string;
  priority?: number;
  stateId?: string;
  assigneeId?: string;
  labelIds?: string[];
  estimate?: number;
  parentId?: string;
}

interface TransformContext {
  linearClient: LinearClient;
  teamId: string;
  stateMap: Map<string, string>;
  userMap: Map<string, string>;
  labelMap: Map<string, string>;
  issueIdMap: Map<string, string>; // sourceId -> linearId
}

export async function transformJiraIssue(
  jiraIssue: JiraIssue,
  context: TransformContext
): Promise<LinearIssueInput> {
  // Map status to Linear state
  const linearStatus = JIRA_STATUS_MAP[jiraIssue.fields.status.name] || "Todo";
  const stateId = context.stateMap.get(linearStatus);

  // Map priority
  const priority = JIRA_PRIORITY_MAP[jiraIssue.fields.priority?.name] || 0;

  // Map assignee
  const assigneeEmail = jiraIssue.fields.assignee?.emailAddress;
  const assigneeId = assigneeEmail ? context.userMap.get(assigneeEmail) : undefined;

  // Map labels
  const labelIds: string[] = [];

  // Add issue type as label
  const typeLabel = JIRA_TYPE_MAP[jiraIssue.fields.issuetype.name];
  if (typeLabel && context.labelMap.has(typeLabel.labelName)) {
    labelIds.push(context.labelMap.get(typeLabel.labelName)!);
  }

  // Add Jira labels
  for (const label of jiraIssue.fields.labels) {
    const linearLabelId = context.labelMap.get(label);
    if (linearLabelId) {
      labelIds.push(linearLabelId);
    }
  }

  // Convert description
  const description = convertJiraToMarkdown(jiraIssue.fields.description);

  return {
    teamId: context.teamId,
    title: `[${jiraIssue.key}] ${jiraIssue.fields.summary}`,
    description,
    priority,
    stateId,
    assigneeId,
    labelIds,
    estimate: jiraIssue.fields.customfield_10001, // Story points
  };
}

function convertJiraToMarkdown(jiraMarkup: string | null): string {
  if (!jiraMarkup) return "";

  let md = jiraMarkup;

  // Headers
  md = md.replace(/h1\. /g, "# ");
  md = md.replace(/h2\. /g, "## ");
  md = md.replace(/h3\. /g, "### ");

  // Bold and italic
  md = md.replace(/\*([^*]+)\*/g, "**$1**");
  md = md.replace(/_([^_]+)_/g, "*$1*");

  // Code blocks
  md = md.replace(/\{code(:([^}]+))?\}([\s\S]*?)\{code\}/g, "```$2\n$3\n```");
  md = md.replace(/\{noformat\}([\s\S]*?)\{noformat\}/g, "```\n$1\n```");

  // Lists
  md = md.replace(/^# /gm, "1. ");
  md = md.replace(/^\* /gm, "- ");

  // Links
  md = md.replace(/\[([^\]|]+)\|([^\]]+)\]/g, "[$1]($2)");
  md = md.replace(/\[([^\]]+)\]/g, "[$1]($1)");

  return md;
}
```

### Step 3: Import to Linear

```typescript
// migration/import.ts
import { LinearClient } from "@linear/sdk";

interface ImportStats {
  total: number;
  created: number;
  skipped: number;
  errors: { sourceId: string; error: string }[];
}

export async function importToLinear(
  issues: JiraIssue[],
  context: TransformContext
): Promise<ImportStats> {
  const stats: ImportStats = {
    total: issues.length,
    created: 0,
    skipped: 0,
    errors: [],
  };

  // Sort issues: parents first, then children
  const sorted = sortByHierarchy(issues);

  for (const jiraIssue of sorted) {
    try {
      // Check if already imported
      if (context.issueIdMap.has(jiraIssue.key)) {
        stats.skipped++;
        continue;
      }

      const input = await transformJiraIssue(jiraIssue, context);

      // Set parent if exists
      if (jiraIssue.fields.parent) {
        input.parentId = context.issueIdMap.get(jiraIssue.fields.parent.key);
      }

      // Create in Linear
      const result = await context.linearClient.createIssue(input);

      if (result.success) {
        const issue = await result.issue;
        context.issueIdMap.set(jiraIssue.key, issue!.id);
        stats.created++;

        // Rate limit
        await sleep(100);
      } else {
        throw new Error("Create failed");
      }

      console.log(`Imported ${stats.created}/${stats.total}: ${jiraIssue.key}`);
    } catch (error) {
      stats.errors.push({
        sourceId: jiraIssue.key,
        error: error instanceof Error ? error.message : "Unknown error",
      });
      console.error(`Failed to import ${jiraIssue.key}:`, error);
    }
  }

  return stats;
}

function sortByHierarchy(issues: JiraIssue[]): JiraIssue[] {
  const byKey = new Map(issues.map(i => [i.key, i]));
  const sorted: JiraIssue[] = [];
  const processed = new Set<string>();

  function addWithDependencies(issue: JiraIssue): void {
    if (processed.has(issue.key)) return;

    // Add parent first
    if (issue.fields.parent) {
      const parent = byKey.get(issue.fields.parent.key);
      if (parent) addWithDependencies(parent);
    }

    sorted.push(issue);
    processed.add(issue.key);
  }

  for (const issue of issues) {
    addWithDependencies(issue);
  }

  return sorted;
}
```

### Step 4: Validation & Verification

```typescript
// migration/validate.ts

export async function validateMigration(
  sourceIssues: JiraIssue[],
  context: TransformContext
): Promise<{ valid: boolean; issues: string[] }> {
  const issues: string[] = [];

  // Check all issues were migrated
  for (const source of sourceIssues) {
    if (!context.issueIdMap.has(source.key)) {
      issues.push(`Missing: ${source.key}`);
    }
  }

  // Verify sample of migrated issues
  const sampleSize = Math.min(50, sourceIssues.length);
  const sample = sourceIssues.slice(0, sampleSize);

  for (const source of sample) {
    const linearId = context.issueIdMap.get(source.key);
    if (!linearId) continue;

    try {
      const linearIssue = await context.linearClient.issue(linearId);

      // Check title contains original key
      if (!linearIssue.title.includes(source.key)) {
        issues.push(`Title mismatch: ${source.key}`);
      }

      // Check priority mapping
      const expectedPriority = JIRA_PRIORITY_MAP[source.fields.priority?.name] || 0;
      if (linearIssue.priority !== expectedPriority) {
        issues.push(`Priority mismatch: ${source.key} (${linearIssue.priority} != ${expectedPriority})`);
      }
    } catch (error) {
      issues.push(`Verify failed: ${source.key} - ${error}`);
    }
  }

  return {
    valid: issues.length === 0,
    issues,
  };
}
```

### Step 5: Post-Migration

```typescript
// migration/post-migration.ts

export async function createMigrationReport(
  stats: ImportStats,
  context: TransformContext
): Promise<string> {
  const report = `
# Migration Report

**Date:** ${new Date().toISOString()}
**Source:** Jira
**Target:** Linear