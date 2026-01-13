# Implementation Guide

### Step 1: Create GitHub Actions Workflow
Create `.github/workflows/fireflies-integration.yml`:

```yaml
name: Fireflies.ai Integration Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  FIREFLIES_API_KEY: ${{ secrets.FIREFLIES_API_KEY }}

jobs:
  test:
    runs-on: ubuntu-latest
    env:
      FIREFLIES_API_KEY: ${{ secrets.FIREFLIES_API_KEY }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      - run: npm ci
      - run: npm test -- --coverage
      - run: npm run test:integration
```

### Step 2: Configure Secrets
```bash
gh secret set FIREFLIES_API_KEY --body "sk_test_***"
```

### Step 3: Add Integration Tests
```typescript
describe('Fireflies.ai Integration', () => {
  it.skipIf(!process.env.FIREFLIES_API_KEY)('should connect', async () => {
    const client = getFireflies.aiClient();
    const result = await client.healthCheck();
    expect(result.status).toBe('ok');
  });
});
```