# Examples

### Factory Pattern (Multi-tenant)
```typescript
const clients = new Map<string, IdeogramClient>();

export function getClientForTenant(tenantId: string): IdeogramClient {
  if (!clients.has(tenantId)) {
    const apiKey = getTenantApiKey(tenantId);
    clients.set(tenantId, new IdeogramClient({ apiKey }));
  }
  return clients.get(tenantId)!;
}
```

### Python Context Manager
```python
from contextlib import asynccontextmanager
from ideogram import IdeogramClient

@asynccontextmanager
async def get_ideogram_client():
    client = IdeogramClient()
    try:
        yield client
    finally:
        await client.close()
```

### Zod Validation
```typescript
import { z } from 'zod';

const ideogramResponseSchema = z.object({
  id: z.string(),
  status: z.enum(['active', 'inactive']),
  createdAt: z.string().datetime(),
});
```