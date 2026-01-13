# Implementation Guide

### Step 1: Create Entry File
Create a new file for your hello world example.

### Step 2: Import and Initialize Client
```typescript
import { Lindy } from '@lindy-ai/sdk';

const lindy = new Lindy({
  apiKey: process.env.LINDY_API_KEY,
});
```

### Step 3: Create Your First Agent
```typescript
async function main() {
  // Create a simple AI agent
  const agent = await lindy.agents.create({
    name: 'Hello World Agent',
    description: 'My first Lindy agent',
    instructions: 'You are a helpful assistant that greets users.',
  });

  console.log(`Created agent: ${agent.id}`);

  // Run the agent with a simple task
  const result = await lindy.agents.run(agent.id, {
    input: 'Say hello to the world!',
  });

  console.log(`Agent response: ${result.output}`);
}

main().catch(console.error);
```