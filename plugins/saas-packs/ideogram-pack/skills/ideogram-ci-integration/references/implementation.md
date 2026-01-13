# Implementation Guide

### Step 1: Create GitHub Actions Workflow
Create `.github/workflows/ideogram-integration.yml`:

```yaml
name: Ideogram Integration Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  IDEOGRAM_API_KEY: ${{ secrets.IDEOGRAM_API_KEY }}

jobs:
  test:
    runs-on: ubuntu-latest
    env:
      IDEOGRAM_API_KEY: ${{ secrets.IDEOGRAM_API_KEY }}
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
gh secret set IDEOGRAM_API_KEY --body "sk_test_***"
```

### Step 3: Add Integration Tests
```typescript
describe('Ideogram Integration', () => {
  it.skipIf(!process.env.IDEOGRAM_API_KEY)('should connect', async () => {
    const client = getIdeogramClient();
    const result = await client.healthCheck();
    expect(result.status).toBe('ok');
  });
});
```