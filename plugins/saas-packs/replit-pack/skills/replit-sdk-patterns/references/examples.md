# Examples

### Factory Pattern (Multi-tenant)
```typescript
const clients = new Map<string, ReplitClient>();

export function getClientForTenant(tenantId: string): ReplitClient {
  if (!clients.has(tenantId)) {
    const apiKey = getTenantApiKey(tenantId);
    clients.set(tenantId, new ReplitClient({ apiKey }));
  }
  return clients.get(tenantId)!;
}
```

### Python Context Manager
```python
from contextlib import asynccontextmanager
from replit import ReplitClient

@asynccontextmanager
async def get_replit_client():
    client = ReplitClient()
    try:
        yield client
    finally:
        await client.close()
```

### Zod Validation
```typescript
import { z } from 'zod';

const replitResponseSchema = z.object({
  id: z.string(),
  status: z.enum(['active', 'inactive']),
  createdAt: z.string().datetime(),
});
```