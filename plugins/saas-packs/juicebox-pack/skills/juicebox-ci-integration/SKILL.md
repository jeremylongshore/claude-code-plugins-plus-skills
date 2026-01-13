---
name: juicebox-ci-integration
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Configure Juicebox CI/CD integration with GitHub Actions and testing.
  Use when setting up automated testing, configuring CI pipelines, or integrating
  Juicebox tests into your build process. Trigger with phrases like "juicebox CI",
  "juicebox GitHub...
---
# Juicebox CI Integration

## Overview
Configure CI/CD pipelines for Juicebox integration testing and deployment.

## Prerequisites
- GitHub repository with Actions enabled
- Juicebox test API key
- npm/pnpm project configured

## Instructions

### Step 1: Configure GitHub Secrets
```bash
# Add secrets via GitHub CLI
gh secret set JUICEBOX_API_KEY --body "jb_test_xxxx"
gh secret set JUICEBOX_API_KEY_PROD --body "jb_prod_xxxx"
```

### Step 2: Create Test Workflow
```yaml
# .github/workflows/juicebox-tests.yml
name: Juicebox Integration Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  JUICEBOX_API_KEY: ${{ secrets.JUICEBOX_API_KEY }}

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run Juicebox tests
        run: npm run test:juicebox

      - name: Upload test results
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: test-results
          path: coverage/
```

### Step 3: Add Integration Tests
```typescript
// tests/juicebox.integration.test.ts
import { describe, it, expect, beforeAll } from 'vitest';
import { JuiceboxClient } from '@juicebox/sdk';

describe('Juicebox Integration', () => {
  let client: JuiceboxClient;

  beforeAll(() => {
    if (!process.env.JUICEBOX_API_KEY) {
      throw new Error('JUICEBOX_API_KEY required for integration tests');
    }
    client = new JuiceboxClient({
      apiKey: process.env.JUICEBOX_API_KEY
    });
  });

  it('authenticates with valid API key', async () => {
    const user = await client.auth.me();
    expect(user.id).toBeDefined();
  });

  it('performs basic search', async () => {
    const results = await client.search.people({
      query: 'engineer',
      limit: 5
    });
    expect(results.profiles).toBeDefined();
  });

  it('handles invalid queries gracefully', async () => {
    await expect(
      client.search.people({ query: '', limit: 5 })
    ).rejects.toThrow();
  });
});
```

### Step 4: Configure Branch Protection
```yaml
# .github/workflows/required-checks.yml
name: Required Checks

on:
  pull_request:
    branches: [main]

jobs:
  juicebox-smoke-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npm run test:juicebox:smoke
        env:
          JUICEBOX_API_KEY: ${{ secrets.JUICEBOX_API_KEY }}
```

### Step 5: Add Deployment Pipeline
```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: production

    steps:
      - uses: actions/checkout@v4

      - name: Validate Juicebox config
        run: |
          curl -f -H "Authorization: Bearer ${{ secrets.JUICEBOX_API_KEY_PROD }}" \
            https://api.juicebox.ai/v1/auth/me

      - name: Deploy application
        run: npm run deploy
        env:
          JUICEBOX_API_KEY: ${{ secrets.JUICEBOX_API_KEY_PROD }}
```

## Output
- GitHub Actions workflow files
- Integration test suite
- Branch protection rules
- Deployment pipeline

## Error Handling
| CI Issue | Cause | Solution |
|----------|-------|----------|
| Secret not found | Not configured | Run `gh secret set` |
| Rate limited | Too many test runs | Use sandbox mode |
| Flaky tests | Network issues | Add retry logic |

## Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Juicebox CI Guide](https://juicebox.ai/docs/ci)

## Next Steps
After CI setup, see `juicebox-deploy-integration` for deployment configuration.
