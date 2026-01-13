# Implementation Guide

### Step 1: Check Current Version
```bash
# Node.js
npm list @gamma/sdk

# Python
pip show gamma-sdk

# Check for available updates
npm outdated @gamma/sdk
```

### Step 2: Review Changelog
```bash
# View changelog
npm info @gamma/sdk changelog

# Or visit
# https://gamma.app/docs/changelog
```

### Step 3: Upgrade SDK
```bash
# Create upgrade branch
git checkout -b feat/gamma-sdk-upgrade

# Node.js - upgrade to latest
npm install @gamma/sdk@latest

# Python - upgrade to latest
pip install --upgrade gamma-sdk

# Or specific version
npm install @gamma/sdk@2.0.0
```

### Step 4: Handle Breaking Changes

**Common Migration Patterns:**

```typescript
// v1.x -> v2.x: Client initialization change
// Before (v1)
import Gamma from '@gamma/sdk';
const gamma = new Gamma(apiKey);

// After (v2)
import { GammaClient } from '@gamma/sdk';
const gamma = new GammaClient({ apiKey });
```

```typescript
// v1.x -> v2.x: Response format change
// Before (v1)
const result = await gamma.createPresentation({ title: 'Test' });
console.log(result.id);

// After (v2)
const result = await gamma.presentations.create({ title: 'Test' });
console.log(result.data.id);
```

```typescript
// v1.x -> v2.x: Error handling change
// Before (v1)
try {
  await gamma.create({ ... });
} catch (e) {
  if (e.code === 'RATE_LIMIT') { ... }
}

// After (v2)
import { RateLimitError } from '@gamma/sdk';
try {
  await gamma.presentations.create({ ... });
} catch (e) {
  if (e instanceof RateLimitError) { ... }
}
```

### Step 5: Update Type Definitions
```typescript
// Check for type changes
// tsconfig.json - ensure strict mode catches issues
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true
  }
}

// Run type check
npx tsc --noEmit
```

### Step 6: Test Thoroughly
```bash
# Run unit tests
npm test

# Run integration tests
npm run test:integration

# Manual smoke test
node -e "
const { GammaClient } = require('@gamma/sdk');
const g = new GammaClient({ apiKey: process.env.GAMMA_API_KEY });
g.ping().then(() => console.log('OK')).catch(console.error);
"
```

### Step 7: Deprecation Handling
```typescript
// Enable deprecation warnings
const gamma = new GammaClient({
  apiKey: process.env.GAMMA_API_KEY,
  showDeprecationWarnings: true,
});

// Migrate deprecated methods
// Deprecated
await gamma.getPresentations();

// New
await gamma.presentations.list();
```