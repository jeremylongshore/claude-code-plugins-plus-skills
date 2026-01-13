# Implementation Guide

### Step 1: Set Up Project Structure
```bash
mkdir lindy-agents && cd lindy-agents
npm init -y
npm install @lindy-ai/sdk typescript ts-node dotenv
npm install -D @types/node nodemon
```

### Step 2: Configure TypeScript
```json
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "outDir": "./dist",
    "strict": true,
    "esModuleInterop": true
  },
  "include": ["src/**/*"]
}
```

### Step 3: Create Development Script
```json
// package.json scripts
{
  "scripts": {
    "dev": "nodemon --exec ts-node src/index.ts",
    "build": "tsc",
    "start": "node dist/index.js",
    "test:agent": "ts-node src/test-agent.ts"
  }
}
```

### Step 4: Create Agent Test Harness
```typescript
// src/test-agent.ts
import 'dotenv/config';
import { Lindy } from '@lindy-ai/sdk';

const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

async function testAgent(agentId: string, input: string) {
  console.log(`Testing agent ${agentId} with: "${input}"`);
  const start = Date.now();

  const result = await lindy.agents.run(agentId, { input });

  console.log(`Response (${Date.now() - start}ms): ${result.output}`);
  return result;
}

// Run test
testAgent(process.argv[2], process.argv[3] || 'Hello!');
```