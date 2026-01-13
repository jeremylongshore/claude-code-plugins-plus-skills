# Examples

### Factory Pattern (Multi-tenant)
```typescript
const clients = new Map<string, FireCrawlClient>();

export function getClientForTenant(tenantId: string): FireCrawlClient {
  if (!clients.has(tenantId)) {
    const apiKey = getTenantApiKey(tenantId);
    clients.set(tenantId, new FireCrawlClient({ apiKey }));
  }
  return clients.get(tenantId)!;
}
```

### Python Context Manager
```python
from contextlib import asynccontextmanager
from firecrawl import FireCrawlClient

@asynccontextmanager
async def get_firecrawl_client():
    client = FireCrawlClient()
    try:
        yield client
    finally:
        await client.close()
```

### Zod Validation
```typescript
import { z } from 'zod';

const firecrawlResponseSchema = z.object({
  id: z.string(),
  status: z.enum(['active', 'inactive']),
  createdAt: z.string().datetime(),
});
```