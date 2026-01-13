# Examples

### Factory Pattern (Multi-tenant)
```typescript
const clients = new Map<string, RetellAIClient>();

export function getClientForTenant(tenantId: string): RetellAIClient {
  if (!clients.has(tenantId)) {
    const apiKey = getTenantApiKey(tenantId);
    clients.set(tenantId, new RetellAIClient({ apiKey }));
  }
  return clients.get(tenantId)!;
}
```

### Python Context Manager
```python
from contextlib import asynccontextmanager
from retellai import RetellAIClient

@asynccontextmanager
async def get_retellai_client():
    client = RetellAIClient()
    try:
        yield client
    finally:
        await client.close()
```

### Zod Validation
```typescript
import { z } from 'zod';

const retellaiResponseSchema = z.object({
  id: z.string(),
  status: z.enum(['active', 'inactive']),
  createdAt: z.string().datetime(),
});
```