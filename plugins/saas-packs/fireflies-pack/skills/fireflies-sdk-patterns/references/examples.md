# Examples

### Factory Pattern (Multi-tenant)
```typescript
const clients = new Map<string, Fireflies.aiClient>();

export function getClientForTenant(tenantId: string): Fireflies.aiClient {
  if (!clients.has(tenantId)) {
    const apiKey = getTenantApiKey(tenantId);
    clients.set(tenantId, new Fireflies.aiClient({ apiKey }));
  }
  return clients.get(tenantId)!;
}
```

### Python Context Manager
```python
from contextlib import asynccontextmanager
from fireflies import Fireflies.aiClient

@asynccontextmanager
async def get_fireflies_client():
    client = Fireflies.aiClient()
    try:
        yield client
    finally:
        await client.close()
```

### Zod Validation
```typescript
import { z } from 'zod';

const firefliesResponseSchema = z.object({
  id: z.string(),
  status: z.enum(['active', 'inactive']),
  createdAt: z.string().datetime(),
});
```