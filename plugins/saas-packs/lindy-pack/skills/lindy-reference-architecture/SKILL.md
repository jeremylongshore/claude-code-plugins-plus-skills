---
name: lindy-reference-architecture
license: MIT
allowed-tools: Read, Write, Edit
description: Reference architectures for lindy ai integrations. use when designing
  systems, planning architecture, or implementing production patterns. trigger with
  phrases like "lindy architecture", "lindy design", "lindy system design", "lindy
  patterns".
---
# Lindy Reference Architecture

## Overview
Production-ready reference architectures for Lindy AI integrations.

## Prerequisites
- Understanding of system design principles
- Familiarity with cloud services
- Production requirements defined

## Architecture Patterns

### Pattern 1: Basic Integration
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │────▶│   Backend   │────▶│   Lindy AI  │
│   (React)   │◀────│   (Node.js) │◀────│   API       │
└─────────────┘     └─────────────┘     └─────────────┘
```

```typescript
// Simple backend integration
import express from 'express';
import { Lindy } from '@lindy-ai/sdk';

const app = express();
const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

app.post('/api/chat', async (req, res) => {
  const { message, agentId } = req.body;
  const result = await lindy.agents.run(agentId, { input: message });
  res.json({ response: result.output });
});
```

### Pattern 2: Event-Driven Architecture
```
┌──────────────────────────────────────────────────────────┐
│                     Event Bus (Redis/SQS)                │
└────┬─────────────────┬─────────────────┬────────────────┘
     │                 │                 │
     ▼                 ▼                 ▼
┌─────────┐      ┌─────────┐      ┌─────────┐
│ Worker  │      │ Worker  │      │ Worker  │
│ (Agent) │      │ (Agent) │      │ (Agent) │
└────┬────┘      └────┬────┘      └────┬────┘
     │                │                │
     └────────────────┼────────────────┘
                      ▼
              ┌─────────────┐
              │  Lindy AI   │
              │    API      │
              └─────────────┘
```

```typescript
// Event-driven worker
import { Queue } from 'bullmq';
import { Lindy } from '@lindy-ai/sdk';

const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });
const queue = new Queue('lindy-tasks');

// Producer
async function enqueueTask(agentId: string, input: string) {
  await queue.add('run-agent', { agentId, input });
}

// Consumer
const worker = new Worker('lindy-tasks', async (job) => {
  const { agentId, input } = job.data;
  const result = await lindy.agents.run(agentId, { input });

  // Emit result event
  await eventBus.publish('agent.completed', {
    jobId: job.id,
    result: result.output,
  });
});
```

### Pattern 3: Multi-Agent Orchestration
```
                    ┌─────────────────┐
                    │   Orchestrator  │
                    │     Agent       │
                    └────────┬────────┘
                             │
           ┌─────────────────┼─────────────────┐
           │                 │                 │
           ▼                 ▼                 ▼
    ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
    │  Research   │   │  Analysis   │   │  Writing    │
    │   Agent     │   │   Agent     │   │   Agent     │
    └─────────────┘   └─────────────┘   └─────────────┘
```

```typescript
// Multi-agent orchestrator
class AgentOrchestrator {
  private lindy: Lindy;
  private agents: Record<string, string> = {
    research: 'agt_research',
    analysis: 'agt_analysis',
    writing: 'agt_writing',
    orchestrator: 'agt_orchestrator',
  };

  async execute(task: string): Promise<string> {
    // Step 1: Orchestrator plans the work
    const plan = await this.lindy.agents.run(this.agents.orchestrator, {
      input: `Plan steps for: ${task}`,
    });

    // Step 2: Execute each step
    const steps = JSON.parse(plan.output);
    const results: string[] = [];

    for (const step of steps) {
      const result = await this.lindy.agents.run(
        this.agents[step.agent],
        { input: step.task }
      );
      results.push(result.output);
    }

    // Step 3: Synthesize results
    const synthesis = await this.lindy.agents.run(this.agents.orchestrator, {
      input: `Synthesize: ${results.join('\n')}`,
    });

    return synthesis.output;
  }
}
```

### Pattern 4: High-Availability Setup
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Load      │────▶│   App       │────▶│   Lindy     │
│   Balancer  │     │   Server 1  │     │   Primary   │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                    ┌─────────────┐     ┌──────▼──────┐
                    │   App       │────▶│   Lindy     │
                    │   Server 2  │     │   Fallback  │
                    └─────────────┘     └─────────────┘
                                               │
┌─────────────┐     ┌─────────────┐            │
│   Cache     │◀────│   Shared    │◀───────────┘
│   (Redis)   │     │   State     │
└─────────────┘     └─────────────┘
```

```typescript
// HA client with failover
class HALindyClient {
  private primary: Lindy;
  private fallback: Lindy;
  private cache: Redis;

  async run(agentId: string, input: string) {
    // Check cache first
    const cached = await this.cache.get(`${agentId}:${input}`);
    if (cached) return JSON.parse(cached);

    try {
      // Try primary
      const result = await this.primary.agents.run(agentId, { input });
      await this.cache.setex(`${agentId}:${input}`, 300, JSON.stringify(result));
      return result;
    } catch (error) {
      // Fallback
      console.warn('Primary failed, using fallback');
      return this.fallback.agents.run(agentId, { input });
    }
  }
}
```

## Output
- Architecture diagrams
- Implementation patterns
- HA/failover strategies
- Multi-agent orchestration

## Error Handling
| Pattern | Failure Mode | Recovery |
|---------|--------------|----------|
| Basic | API error | Retry with backoff |
| Event-driven | Worker crash | Queue retry |
| Multi-agent | Step failure | Skip or fallback |
| HA | Primary down | Automatic failover |

## Resources
- [Lindy Architecture Guide](https://docs.lindy.ai/architecture)
- [Best Practices](https://docs.lindy.ai/best-practices)
- [Case Studies](https://lindy.ai/case-studies)

## Next Steps
Proceed to Flagship tier skills for enterprise features.
