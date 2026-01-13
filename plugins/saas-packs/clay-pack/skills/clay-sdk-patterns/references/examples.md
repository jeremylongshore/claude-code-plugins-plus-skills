# Examples

### Factory Pattern (Multi-tenant)
```typescript
const clients = new Map<string, ClayClient>();

export function getClientForTenant(tenantId: string): ClayClient {
  if (!clients.has(tenantId)) {
    const apiKey = getTenantApiKey(tenantId);
    clients.set(tenantId, new ClayClient({ apiKey }));
  }
  return clients.get(tenantId)!;
}
```

### Python Context Manager
```python
from contextlib import asynccontextmanager
from clay import ClayClient

@asynccontextmanager
async def get_clay_client():
    client = ClayClient()
    try:
        yield client
    finally:
        await client.close()
```

### Zod Validation
```typescript
import { z } from 'zod';

const clayResponseSchema = z.object({
  id: z.string(),
  status: z.enum(['active', 'inactive']),
  createdAt: z.string().datetime(),
});
```