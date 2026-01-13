# Implementation Guide

### Step 1: Install Dev Dependencies
```bash
npm install -D nodemon tsx dotenv @types/node
```

### Step 2: Configure Development Script
Add to package.json:
```json
{
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "dev:mock": "GAMMA_MOCK=true tsx watch src/index.ts"
  }
}
```

### Step 3: Create Mock Client
```typescript
// src/gamma-client.ts
import { GammaClient } from '@gamma/sdk';

const isMock = process.env.GAMMA_MOCK === 'true';

export const gamma = isMock
  ? createMockClient()
  : new GammaClient({ apiKey: process.env.GAMMA_API_KEY });

function createMockClient() {
  return {
    presentations: {
      create: async (opts) => ({
        id: 'mock-123',
        url: 'https://gamma.app/mock/preview',
        title: opts.title,
      }),
    },
  };
}
```

### Step 4: Set Up Environment Files
```bash
# .env.development
GAMMA_API_KEY=your-dev-key
GAMMA_MOCK=false

# .env.test
GAMMA_MOCK=true
```