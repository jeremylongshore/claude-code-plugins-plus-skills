# Examples

### Factory Pattern (Multi-tenant)
```typescript
const clients = new Map<string, CodeRabbitClient>();

export function getClientForTenant(tenantId: string): CodeRabbitClient {
  if (!clients.has(tenantId)) {
    const apiKey = getTenantApiKey(tenantId);
    clients.set(tenantId, new CodeRabbitClient({ apiKey }));
  }
  return clients.get(tenantId)!;
}
```

### Python Context Manager
```python
from contextlib import asynccontextmanager
from coderabbit import CodeRabbitClient

@asynccontextmanager
async def get_coderabbit_client():
    client = CodeRabbitClient()
    try:
        yield client
    finally:
        await client.close()
```

### Zod Validation
```typescript
import { z } from 'zod';

const coderabbitResponseSchema = z.object({
  id: z.string(),
  status: z.enum(['active', 'inactive']),
  createdAt: z.string().datetime(),
});
```