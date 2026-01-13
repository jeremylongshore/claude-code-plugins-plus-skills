# Examples

### Factory Pattern (Multi-tenant)
```typescript
const clients = new Map<string, InstantlyClient>();

export function getClientForTenant(tenantId: string): InstantlyClient {
  if (!clients.has(tenantId)) {
    const apiKey = getTenantApiKey(tenantId);
    clients.set(tenantId, new InstantlyClient({ apiKey }));
  }
  return clients.get(tenantId)!;
}
```

### Python Context Manager
```python
from contextlib import asynccontextmanager
from instantly import InstantlyClient

@asynccontextmanager
async def get_instantly_client():
    client = InstantlyClient()
    try:
        yield client
    finally:
        await client.close()
```

### Zod Validation
```typescript
import { z } from 'zod';

const instantlyResponseSchema = z.object({
  id: z.string(),
  status: z.enum(['active', 'inactive']),
  createdAt: z.string().datetime(),
});
```