# Examples

### TypeScript Example
```typescript
import { Lindy } from '@lindy-ai/sdk';

const lindy = new Lindy({
  apiKey: process.env.LINDY_API_KEY,
});

async function main() {
  const agent = await lindy.agents.create({
    name: 'Greeting Agent',
    instructions: 'Greet users warmly and helpfully.',
  });

  const result = await lindy.agents.run(agent.id, {
    input: 'Hello!',
  });

  console.log(result.output);
}

main().catch(console.error);
```

### Python Example
```python
from lindy import Lindy

client = Lindy()

agent = client.agents.create(
    name="Greeting Agent",
    instructions="Greet users warmly and helpfully."
)

result = client.agents.run(agent.id, input="Hello!")
print(result.output)
```