# Implementation Guide

### Step 1: Create GitHub Actions Workflow
Create `.github/workflows/coderabbit-integration.yml`:

```yaml
name: CodeRabbit Integration Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  CODERABBIT_API_KEY: ${{ secrets.CODERABBIT_API_KEY }}

jobs:
  test:
    runs-on: ubuntu-latest
    env:
      CODERABBIT_API_KEY: ${{ secrets.CODERABBIT_API_KEY }}
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
gh secret set CODERABBIT_API_KEY --body "sk_test_***"
```

### Step 3: Add Integration Tests
```typescript
describe('CodeRabbit Integration', () => {
  it.skipIf(!process.env.CODERABBIT_API_KEY)('should connect', async () => {
    const client = getCodeRabbitClient();
    const result = await client.healthCheck();
    expect(result.status).toBe('ok');
  });
});
```