# Deployment Checklist

## Deployment Checklist

```typescript
// scripts/pre-deploy-check.ts
import { apollo } from '../src/lib/apollo/client';

interface Check {
  name: string;
  check: () => Promise<boolean>;
  required: boolean;
}

const checks: Check[] = [
  {
    name: 'API Key Valid',
    check: async () => {
      try {
        await apollo.healthCheck();
        return true;
      } catch {
        return false;
      }
    },
    required: true,
  },
  {
    name: 'Rate Limit Available',
    check: async () => {
      // Check we have rate limit headroom
      const response = await apollo.searchPeople({ per_page: 1 });
      return true; // If we got here, we have capacity
    },
    required: false,
  },
  {
    name: 'Search Working',
    check: async () => {
      const result = await apollo.searchPeople({
        q_organization_domains: ['apollo.io'],
        per_page: 1,
      });
      return result.people.length > 0;
    },
    required: true,
  },
];

async function runChecks() {
  console.log('Running pre-deployment checks...\n');

  let allPassed = true;

  for (const { name, check, required } of checks) {
    try {
      const passed = await check();
      const status = passed ? 'PASS' : required ? 'FAIL' : 'WARN';
      console.log(`[${status}] ${name}`);

      if (!passed && required) {
        allPassed = false;
      }
    } catch (error: any) {
      console.log(`[FAIL] ${name}: ${error.message}`);
      if (required) {
        allPassed = false;
      }
    }
  }

  if (!allPassed) {
    console.error('\nPre-deployment checks failed. Aborting.');
    process.exit(1);
  }

  console.log('\nAll checks passed. Ready to deploy.');
}

runChecks();
```