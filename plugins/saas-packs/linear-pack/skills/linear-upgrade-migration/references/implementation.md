# Implementation Guide

### Step 1: Check Current Version
```bash
# Check installed version
npm list @linear/sdk

# Check latest available version
npm view @linear/sdk version

# Check changelog
npm view @linear/sdk changelog
```

### Step 2: Review Breaking Changes
```bash
# View version history
npm view @linear/sdk versions --json | jq -r '.[-10:][]'

# Check GitHub releases for migration guides
open https://github.com/linear/linear/releases
```

### Step 3: Create Upgrade Branch
```bash
git checkout -b upgrade/linear-sdk-vX.Y.Z
```

### Step 4: Update SDK
```bash
# Upgrade to latest
npm install @linear/sdk@latest

# Or upgrade to specific version
npm install @linear/sdk@X.Y.Z

# Check for type errors
npx tsc --noEmit
```

### Step 5: Common Migration Patterns

#### Pattern A: Renamed Fields
```typescript
// Before (deprecated)
const issue = await client.issue("ABC-123");
console.log(issue.state); // Old field name

// After (new version)
const issue = await client.issue("ABC-123");
const state = await issue.state; // Now returns Promise
console.log(state?.name);
```

#### Pattern B: Changed Return Types
```typescript
// Before: Direct object return
const teams = await client.teams();
teams.forEach(team => console.log(team.name));

// After: Paginated connection
const teams = await client.teams();
teams.nodes.forEach(team => console.log(team.name));
```

#### Pattern C: New Required Parameters
```typescript
// Before
await client.createIssue({ title: "Issue" });

// After: teamId is required
await client.createIssue({
  title: "Issue",
  teamId: team.id, // Now required
});
```

#### Pattern D: Removed Methods
```typescript
// Check if method exists before using
if (typeof client.deprecatedMethod === "function") {
  await client.deprecatedMethod();
} else {
  await client.newMethod();
}
```

### Step 6: Create Compatibility Layer
```typescript
// lib/linear-compat.ts
import { LinearClient, Issue } from "@linear/sdk";

// Wrapper for breaking changes
export class LinearCompatClient {
  private client: LinearClient;

  constructor(apiKey: string) {
    this.client = new LinearClient({ apiKey });
  }

  // Normalize different SDK versions
  async getIssue(identifier: string): Promise<{
    id: string;
    title: string;
    stateName: string;
  }> {
    const issue = await this.client.issue(identifier);
    const state = await issue.state;

    return {
      id: issue.id,
      title: issue.title,
      stateName: state?.name ?? "Unknown",
    };
  }

  // Add backward-compatible methods as needed
}
```

### Step 7: Run Tests
```bash
# Run test suite
npm test

# Run type checking
npx tsc --noEmit

# Run linting
npm run lint
```

### Step 8: Test in Staging
```bash
# Deploy to staging
npm run deploy:staging

# Run integration tests against staging
npm run test:integration
```

### Step 9: Gradual Rollout
```typescript
// Feature flag for new SDK behavior
const USE_NEW_SDK = process.env.LINEAR_SDK_V2 === "true";

async function getIssues() {
  if (USE_NEW_SDK) {
    // New SDK logic
    return newGetIssues();
  } else {
    // Legacy SDK logic
    return legacyGetIssues();
  }
}
```