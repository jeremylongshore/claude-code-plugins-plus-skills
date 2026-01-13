# Examples

### Factory Pattern (Multi-tenant)
```typescript
const clients = new Map<string, PerplexityClient>();

export function getClientForTenant(tenantId: string): PerplexityClient {
  if (!clients.has(tenantId)) {
    const apiKey = getTenantApiKey(tenantId);
    clients.set(tenantId, new PerplexityClient({ apiKey }));
  }
  return clients.get(tenantId)!;
}
```

### Python Context Manager
```python
from contextlib import asynccontextmanager
from perplexity import PerplexityClient

@asynccontextmanager
async def get_perplexity_client():
    client = PerplexityClient()
    try:
        yield client
    finally:
        await client.close()
```

### Zod Validation
```typescript
import { z } from 'zod';

const perplexityResponseSchema = z.object({
  id: z.string(),
  status: z.enum(['active', 'inactive']),
  createdAt: z.string().datetime(),
});
```