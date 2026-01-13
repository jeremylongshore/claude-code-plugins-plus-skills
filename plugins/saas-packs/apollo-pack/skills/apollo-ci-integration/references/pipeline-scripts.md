# Pipeline Scripts

## Pipeline Scripts

### package.json Scripts
```json
{
  "scripts": {
    "test:unit": "vitest run --config vitest.unit.config.ts",
    "test:integration": "vitest run --config vitest.integration.config.ts",
    "test:apollo": "vitest run tests/integration/apollo.test.ts",
    "apollo:validate": "tsx scripts/validate-apollo-config.ts",
    "apollo:health": "curl -sf 'https://api.apollo.io/v1/auth/health?api_key=$APOLLO_API_KEY'"
  }
}
```

### Validation Script
```typescript
// scripts/validate-apollo-config.ts
async function validateConfig() {
  const checks = [];

  // Check API key
  if (!process.env.APOLLO_API_KEY) {
    checks.push({ name: 'API Key', status: 'fail', message: 'Missing' });
  } else {
    checks.push({ name: 'API Key', status: 'pass', message: 'Present' });
  }

  // Check API connectivity
  try {
    const response = await fetch(
      `https://api.apollo.io/v1/auth/health?api_key=${process.env.APOLLO_API_KEY}`
    );
    checks.push({
      name: 'API Health',
      status: response.ok ? 'pass' : 'fail',
      message: response.ok ? 'Healthy' : `Status: ${response.status}`,
    });
  } catch (error) {
    checks.push({
      name: 'API Health',
      status: 'fail',
      message: 'Connection failed',
    });
  }

  // Output results
  const failed = checks.filter((c) => c.status === 'fail');
  if (failed.length > 0) {
    console.error('Validation failed:', failed);
    process.exit(1);
  }

  console.log('All checks passed:', checks);
}

validateConfig();
```