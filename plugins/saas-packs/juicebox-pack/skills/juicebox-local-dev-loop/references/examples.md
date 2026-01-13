# Examples

### Integration Test
```typescript
import { describe, it, expect } from 'vitest';
import { createTestClient } from './test-utils/juicebox';

describe('Juicebox Search', () => {
  it('returns profiles for valid query', async () => {
    const client = createTestClient();
    const results = await client.search.people({
      query: 'engineer',
      limit: 5
    });

    expect(results.profiles.length).toBeGreaterThan(0);
  });
});
```