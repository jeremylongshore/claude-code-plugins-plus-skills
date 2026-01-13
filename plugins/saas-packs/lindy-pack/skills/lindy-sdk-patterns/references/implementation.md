# Implementation Guide

### Pattern 1: Client Singleton
```typescript
// lib/lindy.ts
import { Lindy } from '@lindy-ai/sdk';

let client: Lindy | null = null;

export function getLindyClient(): Lindy {
  if (!client) {
    client = new Lindy({
      apiKey: process.env.LINDY_API_KEY!,
      timeout: 30000,
    });
  }
  return client;
}
```

### Pattern 2: Agent Factory
```typescript
// agents/factory.ts
import { getLindyClient } from '../lib/lindy';

interface AgentConfig {
  name: string;
  instructions: string;
  tools?: string[];
}

export async function createAgent(config: AgentConfig) {
  const lindy = getLindyClient();

  const agent = await lindy.agents.create({
    name: config.name,
    instructions: config.instructions,
    tools: config.tools || [],
  });

  return agent;
}
```

### Pattern 3: Retry with Backoff
```typescript
async function runWithRetry<T>(
  fn: () => Promise<T>,
  maxRetries = 3
): Promise<T> {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await fn();
    } catch (error: any) {
      if (error.status === 429 && i < maxRetries - 1) {
        await new Promise(r => setTimeout(r, Math.pow(2, i) * 1000));
        continue;
      }
      throw error;
    }
  }
  throw new Error('Max retries exceeded');
}
```

### Pattern 4: Streaming Responses
```typescript
async function streamAgentResponse(agentId: string, input: string) {
  const lindy = getLindyClient();

  const stream = await lindy.agents.runStream(agentId, { input });

  for await (const chunk of stream) {
    process.stdout.write(chunk.delta);
  }
  console.log(); // newline
}
```