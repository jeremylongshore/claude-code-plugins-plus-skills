# Implementation Guide

### Step 1: Create GitHub Actions Workflow
Create `.github/workflows/instantly-integration.yml`:

```yaml
name: Instantly Integration Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  INSTANTLY_API_KEY: ${{ secrets.INSTANTLY_API_KEY }}

jobs:
  test:
    runs-on: ubuntu-latest
    env:
      INSTANTLY_API_KEY: ${{ secrets.INSTANTLY_API_KEY }}
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
gh secret set INSTANTLY_API_KEY --body "sk_test_***"
```

### Step 3: Add Integration Tests
```typescript
describe('Instantly Integration', () => {
  it.skipIf(!process.env.INSTANTLY_API_KEY)('should connect', async () => {
    const client = getInstantlyClient();
    const result = await client.healthCheck();
    expect(result.status).toBe('ok');
  });
});
```