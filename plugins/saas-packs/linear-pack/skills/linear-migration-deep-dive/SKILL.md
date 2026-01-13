---
name: linear-migration-deep-dive
license: MIT
allowed-tools: Read, Write, Edit, Bash, Grep
description: Migrate from jira, asana, github issues, or other tools to linear. use
  when planning a migration to linear, executing data transfer, or mapping workflows
  between tools. trigger with phrases like "migrate to linear", "jira to linear",
  "asana to lin...
---
# Linear Migration Deep Dive

## Overview
Comprehensive guide for migrating from other issue trackers to Linear.

## Prerequisites
- Admin access to source system
- Linear workspace with admin access
- API access to both systems
- Migration timeline and rollback plan

## Migration Planning

### Phase 1: Assessment
```markdown
## Migration Assessment Checklist

### Data Volume
- [ ] Count total issues: ____
- [ ] Count total projects: ____
- [ ] Count total users: ____
- [ ] Attachments size: ____ GB
- [ ] Custom fields count: ____

### Workflow Analysis
- [ ] Document current statuses/states
- [ ] Map status transitions
- [ ] Identify automation rules
- [ ] List integrations in use

### User Mapping
- [ ] Export user list from source
- [ ] Map to Linear users
- [ ] Plan for unmapped users

### Timeline
- [ ] Migration window: ____
- [ ] Parallel run period: ____
- [ ] Cutover date: ____
- [ ] Rollback deadline: ____
```

### Phase 2: Workflow Mapping

```typescript
// migration/workflow-mapping.ts

// Jira to Linear status mapping
const JIRA_STATUS_MAP: Record<string, string> = {
  "To Do": "Todo",
  "In Progress": "In Progress",
  "In Review": "In Review",
  "Done": "Done",
  "Closed": "Done",
  "Backlog": "Backlog",
  "Blocked": "In Progress", // Linear uses labels for blocked
};

// Jira to Linear priority mapping
const JIRA_PRIORITY_MAP: Record<string, number> = {
  "Highest": 1, // Urgent
  "High": 2,
  "Medium": 3,
  "Low": 4,
  "Lowest": 4,
};

// Jira to Linear issue type mapping
const JIRA_TYPE_MAP: Record<string, { labelName: string }> = {
  "Bug": { labelName: "Bug" },
  "Story": { labelName: "Feature" },
  "Task": { labelName: "Task" },
  "Epic": { labelName: "Epic" },
  "Subtask": { labelName: "Subtask" },
};

// Asana to Linear mapping
const ASANA_SECTION_MAP: Record<string, string> = {
  "To Do": "Todo",
  "Doing": "In Progress",
  "Review": "In Review",
  "Complete": "Done",
};
```

## Instructions

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

## Statistics
- Total issues: ${stats.total}
- Successfully imported: ${stats.created}
- Skipped (duplicates): ${stats.skipped}
- Errors: ${stats.errors.length}

## ID Mapping
${Array.from(context.issueIdMap.entries())
  .map(([source, linear]) => `- ${source} -> ${linear}`)
  .join("\n")}

## Errors
${stats.errors.map(e => `- ${e.sourceId}: ${e.error}`).join("\n") || "None"}

## Next Steps
1. Verify critical issues manually
2. Update integrations to use Linear
3. Archive source project after parallel run
4. Train team on Linear workflows
`;

  await fs.writeFile("migration-report.md", report);
  return report;
}
```

## Migration Checklist
```
## Pre-Migration
[ ] Backup source system data
[ ] Create Linear workspace and teams
[ ] Set up workflow states and labels
[ ] Map users between systems
[ ] Create API credentials

## Migration
[ ] Export data from source
[ ] Transform to Linear format
[ ] Import in batches
[ ] Validate sample issues
[ ] Import attachments (if needed)

## Post-Migration
[ ] Run full validation
[ ] Set up redirects (if applicable)
[ ] Update integrations
[ ] Train team
[ ] Run parallel for 1-2 weeks
[ ] Archive source after cutover
```

## Error Handling
| Error | Cause | Solution |
|-------|-------|----------|
| `User not found` | Unmapped user | Add to user mapping |
| `Rate limited` | Too fast import | Add delays between requests |
| `State not found` | Unmapped status | Update state mapping |
| `Parent not found` | Import order wrong | Sort by hierarchy |

## Resources
- [Linear Import Documentation](https://linear.app/docs/import-issues)
- [Jira API Reference](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/)
- [Asana API Reference](https://developers.asana.com/reference)

## Conclusion
You have completed the Linear Flagship Skill Pack. You now have comprehensive knowledge of Linear integrations from basic setup through enterprise deployment.
