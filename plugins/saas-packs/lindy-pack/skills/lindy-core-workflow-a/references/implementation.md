# Implementation Guide

### Step 1: Define Agent Specification
```typescript
interface AgentSpec {
  name: string;
  description: string;
  instructions: string;
  tools: string[];
  model?: string;
  temperature?: number;
}

const agentSpec: AgentSpec = {
  name: 'Customer Support Agent',
  description: 'Handles customer inquiries and support tickets',
  instructions: `
    You are a helpful customer support agent.
    - Be polite and professional
    - Ask clarifying questions when needed
    - Escalate complex issues to human support
    - Always confirm resolution with the customer
  `,
  tools: ['email', 'calendar', 'knowledge-base'],
  model: 'gpt-4',
  temperature: 0.7,
};
```

### Step 2: Create the Agent
```typescript
import { Lindy } from '@lindy-ai/sdk';

const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

async function createAgent(spec: AgentSpec) {
  const agent = await lindy.agents.create({
    name: spec.name,
    description: spec.description,
    instructions: spec.instructions,
    tools: spec.tools,
    config: {
      model: spec.model || 'gpt-4',
      temperature: spec.temperature || 0.7,
    },
  });

  console.log(`Created agent: ${agent.id}`);
  return agent;
}
```

### Step 3: Configure Agent Tools
```typescript
async function configureTools(agentId: string, tools: string[]) {
  for (const tool of tools) {
    await lindy.agents.addTool(agentId, {
      name: tool,
      enabled: true,
    });
  }
  console.log(`Configured ${tools.length} tools`);
}
```

### Step 4: Test the Agent
```typescript
async function testAgent(agentId: string) {
  const testCases = [
    'Hello, I need help with my order',
    'Can you check my subscription status?',
    'I want to cancel my account',
  ];

  for (const input of testCases) {
    const result = await lindy.agents.run(agentId, { input });
    console.log(`Input: ${input}`);
    console.log(`Output: ${result.output}\n`);
  }
}
```