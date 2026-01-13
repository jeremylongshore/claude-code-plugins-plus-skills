# Deployment Validation Script

## Deployment Validation Script

```typescript
// scripts/validate-production.ts
import { apollo } from '../src/lib/apollo/client';

interface ValidationResult {
  check: string;
  status: 'pass' | 'fail' | 'warn';
  message: string;
}

async function validateProduction(): Promise<ValidationResult[]> {
  const results: ValidationResult[] = [];

  // 1. API Key Validation
  try {
    await apollo.healthCheck();
    results.push({
      check: 'API Key',
      status: 'pass',
      message: 'API key is valid and active',
    });
  } catch (error: any) {
    results.push({
      check: 'API Key',
      status: 'fail',
      message: `API key validation failed: ${error.message}`,
    });
  }

  // 2. People Search Test
  try {
    const searchResult = await apollo.searchPeople({
      q_organization_domains: ['apollo.io'],
      per_page: 1,
    });
    results.push({
      check: 'People Search',
      status: searchResult.people.length > 0 ? 'pass' : 'warn',
      message: `Found ${searchResult.pagination.total_entries} contacts`,
    });
  } catch (error: any) {
    results.push({
      check: 'People Search',
      status: 'fail',
      message: `Search failed: ${error.message}`,
    });
  }

  // 3. Organization Enrichment Test
  try {
    const orgResult = await apollo.enrichOrganization('apollo.io');
    results.push({
      check: 'Org Enrichment',
      status: orgResult.organization ? 'pass' : 'warn',
      message: orgResult.organization
        ? `Enriched: ${orgResult.organization.name}`
        : 'No organization data returned',
    });
  } catch (error: any) {
    results.push({
      check: 'Org Enrichment',
      status: 'fail',
      message: `Enrichment failed: ${error.message}`,
    });
  }

  // 4. Environment Variables
  const requiredEnvVars = ['APOLLO_API_KEY'];
  const optionalEnvVars = ['APOLLO_RATE_LIMIT', 'APOLLO_TIMEOUT'];

  for (const envVar of requiredEnvVars) {
    results.push({
      check: `Env: ${envVar}`,
      status: process.env[envVar] ? 'pass' : 'fail',
      message: process.env[envVar] ? 'Set' : 'Missing required variable',
    });
  }

  for (const envVar of optionalEnvVars) {
    results.push({
      check: `Env: ${envVar}`,
      status: process.env[envVar] ? 'pass' : 'warn',
      message: process.env[envVar] ? 'Set' : 'Using default value',
    });
  }

  // 5. Response Time Check
  const startTime = Date.now();
  try {
    await apollo.searchPeople({ per_page: 1 });
    const latency = Date.now() - startTime;
    results.push({
      check: 'Latency',
      status: latency < 2000 ? 'pass' : latency < 5000 ? 'warn' : 'fail',
      message: `Response time: ${latency}ms`,
    });
  } catch {
    results.push({
      check: 'Latency',
      status: 'fail',
      message: 'Could not measure latency',
    });
  }

  return results;
}

// Run validation
async function main() {
  console.log('=== Apollo Production Validation ===\n');

  const results = await validateProduction();

  // Display results
  for (const result of results) {
    const icon = result.status === 'pass' ? '[OK]' : result.status === 'warn' ? '[!!]' : '[XX]';
    console.log(`${icon} ${result.check}: ${result.message}`);
  }

  // Summary
  const passed = results.filter((r) => r.status === 'pass').length;
  const warned = results.filter((r) => r.status === 'warn').length;
  const failed = results.filter((r) => r.status === 'fail').length;

  console.log(`\n=== Summary ===`);
  console.log(`Passed: ${passed}, Warnings: ${warned}, Failed: ${failed}`);

  if (failed > 0) {
    console.error('\n[FAIL] Production validation failed. Fix issues before deploying.');
    process.exit(1);
  } else if (warned > 0) {
    console.warn('\n[WARN] Validation passed with warnings. Review before deploying.');
  } else {
    console.log('\n[PASS] All checks passed. Ready for production.');
  }
}

main().catch(console.error);
```