# Implementation Guide

### Step 1: Query Your Teams
```typescript
import { LinearClient } from "@linear/sdk";

const client = new LinearClient({ apiKey: process.env.LINEAR_API_KEY });

// Get all teams you have access to
const teams = await client.teams();
console.log("Your teams:");
teams.nodes.forEach(team => {
  console.log(`  - ${team.name} (${team.key})`);
});
```

### Step 2: Create Your First Issue
```typescript
// Get the first team
const team = teams.nodes[0];

// Create an issue
const issueCreate = await client.createIssue({
  teamId: team.id,
  title: "My first Linear issue from the API",
  description: "This issue was created using the Linear SDK!",
});

if (issueCreate.success) {
  const issue = await issueCreate.issue;
  console.log(`Created issue: ${issue?.identifier} - ${issue?.title}`);
  console.log(`URL: ${issue?.url}`);
}
```

### Step 3: Query Issues
```typescript
// Get recent issues from your team
const issues = await client.issues({
  filter: {
    team: { key: { eq: team.key } },
  },
  first: 10,
});

console.log("Recent issues:");
issues.nodes.forEach(issue => {
  console.log(`  ${issue.identifier}: ${issue.title} [${issue.state?.name}]`);
});
```