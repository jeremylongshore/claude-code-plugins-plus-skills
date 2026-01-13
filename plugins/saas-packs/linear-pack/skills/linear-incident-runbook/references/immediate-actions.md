# Immediate Actions

## Immediate Actions

### Step 1: Confirm the Issue
```bash
# Check Linear API status
curl -s https://status.linear.app/api/v2/status.json | jq '.status'

# Quick health check
curl -s -H "Authorization: $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ viewer { name } }"}' \
  https://api.linear.app/graphql | jq

# Check your application health endpoint
curl -s https://yourapp.com/api/health | jq
```

### Step 2: Gather Initial Information
```typescript
// scripts/incident-info.ts
import { LinearClient } from "@linear/sdk";

async function gatherIncidentInfo() {
  const client = new LinearClient({ apiKey: process.env.LINEAR_API_KEY! });

  console.log("=== Linear Incident Information ===\n");

  // 1. Test authentication
  console.log("1. Authentication:");
  try {
    const viewer = await client.viewer;
    console.log(`   Status: OK (${viewer.name})`);
  } catch (error) {
    console.log(`   Status: FAILED - ${error}`);
  }

  // 2. Check teams access
  console.log("\n2. Team Access:");
  try {
    const teams = await client.teams();
    console.log(`   Accessible teams: ${teams.nodes.length}`);
  } catch (error) {
    console.log(`   Status: FAILED - ${error}`);
  }

  // 3. Test issue creation (dry run)
  console.log("\n3. Write Capability:");
  try {
    const teams = await client.teams();
    const result = await client.createIssue({
      teamId: teams.nodes[0].id,
      title: "[INCIDENT TEST] Delete immediately",
    });
    if (result.success) {
      const issue = await result.issue;
      await issue?.delete();
      console.log("   Status: OK (created and deleted test issue)");
    }
  } catch (error) {
    console.log(`   Status: FAILED - ${error}`);
  }

  console.log("\n=== End Information ===");
}

gatherIncidentInfo();
```