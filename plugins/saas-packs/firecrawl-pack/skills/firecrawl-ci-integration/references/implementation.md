# Implementation Guide

### Step 1: Create GitHub Actions Workflow
Create `.github/workflows/firecrawl-integration.yml`:

```yaml
name: FireCrawl Integration Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  FIRECRAWL_API_KEY: ${{ secrets.FIRECRAWL_API_KEY }}

jobs:
  test:
    runs-on: ubuntu-latest
    env:
      FIRECRAWL_API_KEY: ${{ secrets.FIRECRAWL_API_KEY }}
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
gh secret set FIRECRAWL_API_KEY --body "sk_test_***"
```

### Step 3: Add Integration Tests
```typescript
describe('FireCrawl Integration', () => {
  it.skipIf(!process.env.FIRECRAWL_API_KEY)('should connect', async () => {
    const client = getFireCrawlClient();
    const result = await client.healthCheck();
    expect(result.status).toBe('ok');
  });
});
```