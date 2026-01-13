# Examples

### Complete Agent Service
```typescript
// services/agent-service.ts
import { getLindyClient } from '../lib/lindy';

export class AgentService {
  private lindy = getLindyClient();

  async createAndRun(name: string, instructions: string, input: string) {
    const agent = await this.lindy.agents.create({ name, instructions });
    const result = await this.lindy.agents.run(agent.id, { input });
    return { agent, result };
  }

  async listAgents() {
    return this.lindy.agents.list();
  }

  async deleteAgent(id: string) {
    return this.lindy.agents.delete(id);
  }
}
```