# Examples

### Complete Environment Setup
```typescript
// index.ts
import { getLindyClient } from './lib/lindy-client';
import { getAgentId } from './agents/config';

async function main() {
  const lindy = getLindyClient();
  const agentId = getAgentId('support');

  console.log(`Environment: ${process.env.NODE_ENV}`);
  console.log(`Agent: ${agentId}`);

  const result = await lindy.agents.run(agentId, {
    input: 'Test message',
  });

  console.log('Response:', result.output);
}

main().catch(console.error);
```