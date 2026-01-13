# Implementation Guide

### Step 1: Project Setup
```bash
# Initialize project
mkdir linear-integration && cd linear-integration
npm init -y
npm install @linear/sdk typescript ts-node dotenv
npm install -D @types/node vitest

# Create tsconfig.json
npx tsc --init --target ES2022 --module NodeNext --moduleResolution NodeNext
```

### Step 2: Environment Configuration
```bash
# Create .env for local development
cat > .env << 'EOF'
LINEAR_API_KEY=lin_api_dev_xxxxxxxxxxxx
LINEAR_WEBHOOK_SECRET=your_webhook_secret
NODE_ENV=development
EOF

# Create .env.example (commit this)
cat > .env.example << 'EOF'
LINEAR_API_KEY=lin_api_xxxxxxxxxxxx
LINEAR_WEBHOOK_SECRET=
NODE_ENV=development
EOF

# Add to .gitignore
echo ".env" >> .gitignore
echo ".env.local" >> .gitignore
```

### Step 3: Create Development Client
```typescript
// src/client.ts
import { LinearClient } from "@linear/sdk";
import dotenv from "dotenv";

dotenv.config();

export const linearClient = new LinearClient({
  apiKey: process.env.LINEAR_API_KEY!,
});

export async function verifyClient(): Promise<boolean> {
  try {
    const viewer = await linearClient.viewer;
    console.log(`[Linear] Connected as ${viewer.name}`);
    return true;
  } catch (error) {
    console.error("[Linear] Connection failed:", error);
    return false;
  }
}
```

### Step 4: Create Test Utilities
```typescript
// src/test-utils.ts
import { linearClient } from "./client";

export async function createTestIssue(teamKey: string) {
  const teams = await linearClient.teams();
  const team = teams.nodes.find(t => t.key === teamKey);

  if (!team) throw new Error(`Team ${teamKey} not found`);

  const result = await linearClient.createIssue({
    teamId: team.id,
    title: `[TEST] ${new Date().toISOString()}`,
    description: "Automated test issue - safe to delete",
  });

  return result.issue;
}

export async function cleanupTestIssues(teamKey: string) {
  const issues = await linearClient.issues({
    filter: {
      team: { key: { eq: teamKey } },
      title: { startsWith: "[TEST]" },
    },
  });

  for (const issue of issues.nodes) {
    await issue.delete();
  }

  console.log(`Cleaned up ${issues.nodes.length} test issues`);
}
```

### Step 5: Set Up Watch Mode
```json
// package.json scripts
{
  "scripts": {
    "dev": "ts-node --watch src/index.ts",
    "test": "vitest",
    "test:watch": "vitest --watch",
    "verify": "ts-node src/verify.ts"
  }
}
```