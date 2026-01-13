# Examples

### Factory Pattern (Multi-tenant)
```typescript
const clients = new Map<string, Vast.aiClient>();

export function getClientForTenant(tenantId: string): Vast.aiClient {
  if (!clients.has(tenantId)) {
    const apiKey = getTenantApiKey(tenantId);
    clients.set(tenantId, new Vast.aiClient({ apiKey }));
  }
  return clients.get(tenantId)!;
}
```

### Python Context Manager
```python
from contextlib import asynccontextmanager
from vastai import Vast.aiClient

@asynccontextmanager
async def get_vastai_client():
    client = Vast.aiClient()
    try:
        yield client
    finally:
        await client.close()
```

### Zod Validation
```typescript
import { z } from 'zod';

const vastaiResponseSchema = z.object({
  id: z.string(),
  status: z.enum(['active', 'inactive']),
  createdAt: z.string().datetime(),
});
```