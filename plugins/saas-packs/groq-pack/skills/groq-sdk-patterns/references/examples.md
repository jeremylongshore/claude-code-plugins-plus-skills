# Examples

### Factory Pattern (Multi-tenant)
```typescript
const clients = new Map<string, GroqClient>();

export function getClientForTenant(tenantId: string): GroqClient {
  if (!clients.has(tenantId)) {
    const apiKey = getTenantApiKey(tenantId);
    clients.set(tenantId, new GroqClient({ apiKey }));
  }
  return clients.get(tenantId)!;
}
```

### Python Context Manager
```python
from contextlib import asynccontextmanager
from groq import GroqClient

@asynccontextmanager
async def get_groq_client():
    client = GroqClient()
    try:
        yield client
    finally:
        await client.close()
```

### Zod Validation
```typescript
import { z } from 'zod';

const groqResponseSchema = z.object({
  id: z.string(),
  status: z.enum(['active', 'inactive']),
  createdAt: z.string().datetime(),
});
```