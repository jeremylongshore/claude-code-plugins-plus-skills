# Implementation Guide

### Step 1: Create GitHub Actions Workflow
```yaml
# .github/workflows/gamma-ci.yml
name: Gamma CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  GAMMA_API_KEY: ${{ secrets.GAMMA_API_KEY }}

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

      - name: Run unit tests
        run: npm test

      - name: Run Gamma integration tests
        run: npm run test:gamma
        env:
          GAMMA_MOCK: ${{ github.event_name == 'pull_request' }}

      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          files: ./coverage/lcov.info
```

### Step 2: Create Test Scripts
```json
// package.json
{
  "scripts": {
    "test": "vitest run",
    "test:gamma": "vitest run --config vitest.gamma.config.ts",
    "test:gamma:live": "GAMMA_MOCK=false vitest run --config vitest.gamma.config.ts"
  }
}
```

### Step 3: Gamma Test Configuration
```typescript
// vitest.gamma.config.ts
import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    include: ['tests/gamma/**/*.test.ts'],
    testTimeout: 60000, // Gamma API can be slow
    hookTimeout: 30000,
    setupFiles: ['./tests/gamma/setup.ts'],
  },
});
```

### Step 4: Test Setup with Mocking
```typescript
// tests/gamma/setup.ts
import { beforeAll, afterAll } from 'vitest';
import { GammaClient } from '@gamma/sdk';

const useMock = process.env.GAMMA_MOCK === 'true';

export let gamma: GammaClient;

beforeAll(() => {
  if (useMock) {
    gamma = createMockGammaClient();
  } else {
    gamma = new GammaClient({
      apiKey: process.env.GAMMA_API_KEY,
    });
  }
});

function createMockGammaClient() {
  return {
    presentations: {
      create: vi.fn().mockResolvedValue({
        id: 'mock-id',
        url: 'https://gamma.app/mock/test',
        title: 'Mock Presentation',
      }),
      list: vi.fn().mockResolvedValue([]),
      get: vi.fn().mockResolvedValue({ id: 'mock-id' }),
    },
    ping: vi.fn().mockResolvedValue({ ok: true }),
  } as unknown as GammaClient;
}
```

### Step 5: Integration Test Example
```typescript
// tests/gamma/presentation.test.ts
import { describe, it, expect } from 'vitest';
import { gamma } from './setup';

describe('Gamma Presentations', () => {
  it('should create a presentation', async () => {
    const result = await gamma.presentations.create({
      title: 'CI Test Presentation',
      prompt: 'Test slide for CI',
      slideCount: 1,
    });

    expect(result.id).toBeDefined();
    expect(result.url).toContain('gamma.app');
  });

  it('should list presentations', async () => {
    const presentations = await gamma.presentations.list({ limit: 5 });

    expect(Array.isArray(presentations)).toBe(true);
  });
});
```

### Step 6: Add Secrets to GitHub
```bash
# Using GitHub CLI
gh secret set GAMMA_API_KEY --body "your-test-api-key"

# Verify secrets
gh secret list
```