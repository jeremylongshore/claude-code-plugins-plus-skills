# Implementation Guide

### Step 1: Create Project Structure
```
my-vastai-project/
├── src/
│   ├── vastai/
│   │   ├── client.ts       # Vast.ai client wrapper
│   │   ├── config.ts       # Configuration management
│   │   └── utils.ts        # Helper functions
│   └── index.ts
├── tests/
│   └── vastai.test.ts
├── .env.local              # Local secrets (git-ignored)
├── .env.example            # Template for team
└── package.json
```

### Step 2: Configure Environment
```bash
# Copy environment template
cp .env.example .env.local

# Install dependencies
npm install

# Start development server
npm run dev
```

### Step 3: Setup Hot Reload
```json
{
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "test": "vitest",
    "test:watch": "vitest --watch"
  }
}
```

### Step 4: Configure Testing
```typescript
import { describe, it, expect, vi } from 'vitest';
import { Vast.aiClient } from '../src/vastai/client';

describe('Vast.ai Client', () => {
  it('should initialize with API key', () => {
    const client = new Vast.aiClient({ apiKey: 'test-key' });
    expect(client).toBeDefined();
  });
});
```