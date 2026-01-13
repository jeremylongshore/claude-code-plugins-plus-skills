# Examples

### Factory Pattern (Multi-tenant)
```typescript
const clients = new Map<string, WindsurfClient>();

export function getClientForTenant(tenantId: string): WindsurfClient {
  if (!clients.has(tenantId)) {
    const apiKey = getTenantApiKey(tenantId);
    clients.set(tenantId, new WindsurfClient({ apiKey }));
  }
  return clients.get(tenantId)!;
}
```

### Python Context Manager
```python
from contextlib import asynccontextmanager
from windsurf import WindsurfClient

@asynccontextmanager
async def get_windsurf_client():
    client = WindsurfClient()
    try:
        yield client
    finally:
        await client.close()
```

### Zod Validation
```typescript
import { z } from 'zod';

const windsurfResponseSchema = z.object({
  id: z.string(),
  status: z.enum(['active', 'inactive']),
  createdAt: z.string().datetime(),
});
```