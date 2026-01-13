# Examples

### Factory Pattern (Multi-tenant)
```typescript
const clients = new Map<string, PostHogClient>();

export function getClientForTenant(tenantId: string): PostHogClient {
  if (!clients.has(tenantId)) {
    const apiKey = getTenantApiKey(tenantId);
    clients.set(tenantId, new PostHogClient({ apiKey }));
  }
  return clients.get(tenantId)!;
}
```

### Python Context Manager
```python
from contextlib import asynccontextmanager
from posthog import PostHogClient

@asynccontextmanager
async def get_posthog_client():
    client = PostHogClient()
    try:
        yield client
    finally:
        await client.close()
```

### Zod Validation
```typescript
import { z } from 'zod';

const posthogResponseSchema = z.object({
  id: z.string(),
  status: z.enum(['active', 'inactive']),
  createdAt: z.string().datetime(),
});
```