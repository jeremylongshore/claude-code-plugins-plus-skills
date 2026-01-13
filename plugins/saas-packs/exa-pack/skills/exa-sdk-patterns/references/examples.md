# Examples

### Factory Pattern (Multi-tenant)
```typescript
const clients = new Map<string, ExaClient>();

export function getClientForTenant(tenantId: string): ExaClient {
  if (!clients.has(tenantId)) {
    const apiKey = getTenantApiKey(tenantId);
    clients.set(tenantId, new ExaClient({ apiKey }));
  }
  return clients.get(tenantId)!;
}
```

### Python Context Manager
```python
from contextlib import asynccontextmanager
from exa import ExaClient

@asynccontextmanager
async def get_exa_client():
    client = ExaClient()
    try:
        yield client
    finally:
        await client.close()
```

### Zod Validation
```typescript
import { z } from 'zod';

const exaResponseSchema = z.object({
  id: z.string(),
  status: z.enum(['active', 'inactive']),
  createdAt: z.string().datetime(),
});
```