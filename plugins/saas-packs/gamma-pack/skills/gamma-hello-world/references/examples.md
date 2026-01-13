# Examples

### TypeScript Example
```typescript
import { GammaClient } from '@gamma/sdk';

const gamma = new GammaClient({
  apiKey: process.env.GAMMA_API_KEY,
});

async function main() {
  const result = await gamma.presentations.create({
    title: 'My First Presentation',
    prompt: 'Explain the benefits of AI-powered presentations',
  });

  console.log('View at:', result.url);
}

main().catch(console.error);
```

### Python Example
```python
from gamma import GammaClient

client = GammaClient()

response = client.presentations.create(
    title='My First Presentation',
    prompt='Explain the benefits of AI-powered presentations'
)

print(f'View at: {response.url}')
```