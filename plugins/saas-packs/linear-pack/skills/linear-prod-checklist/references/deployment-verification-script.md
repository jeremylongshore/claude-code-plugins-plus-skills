# Deployment Verification Script

## Deployment Verification Script

```typescript
// scripts/verify-deployment.ts
import { LinearClient } from "@linear/sdk";

async function verifyDeployment(): Promise<void> {
  console.log("Verifying Linear integration deployment...\n");

  const checks: { name: string; check: () => Promise<boolean> }[] = [
    {
      name: "Environment variables set",
      check: async () => {
        return !!(
          process.env.LINEAR_API_KEY &&
          process.env.LINEAR_WEBHOOK_SECRET
        );
      },
    },
    {
      name: "API authentication works",
      check: async () => {
        const client = new LinearClient({
          apiKey: process.env.LINEAR_API_KEY!,
        });
        await client.viewer;
        return true;
      },
    },
    {
      name: "Can access teams",
      check: async () => {
        const client = new LinearClient({
          apiKey: process.env.LINEAR_API_KEY!,
        });
        const teams = await client.teams();
        return teams.nodes.length > 0;
      },
    },
    {
      name: "Webhook endpoint reachable",
      check: async () => {
        const response = await fetch(
          `${process.env.APP_URL}/webhooks/linear`,
          { method: "GET" }
        );
        return response.status !== 404;
      },
    },
  ];

  let passed = 0;
  let failed = 0;

  for (const { name, check } of checks) {
    try {
      const result = await check();
      if (result) {
        console.log(`✓ ${name}`);
        passed++;
      } else {
        console.log(`✗ ${name}`);
        failed++;
      }
    } catch (error) {
      console.log(`✗ ${name}: ${error}`);
      failed++;
    }
  }

  console.log(`\nResults: ${passed} passed, ${failed} failed`);

  if (failed > 0) {
    process.exit(1);
  }
}

verifyDeployment();
```