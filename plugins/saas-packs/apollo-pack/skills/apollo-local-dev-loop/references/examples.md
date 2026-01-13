# Examples

### Watch Mode Development
```bash
# Terminal 1: Run dev server with watch
npm run dev

# Terminal 2: Test API calls
curl -X POST http://localhost:3000/api/apollo/search \
  -H "Content-Type: application/json" \
  -d '{"domain": "stripe.com"}'
```

### Testing with Mocks
```typescript
// src/services/apollo.apollo.test.ts
import { describe, it, expect, beforeAll, afterAll } from 'vitest';
import { setupServer } from 'msw/node';
import { apolloHandlers } from '../mocks/apollo-mock';
import { searchPeople } from './apollo';

const server = setupServer(...apolloHandlers);

beforeAll(() => server.listen());
afterAll(() => server.close());

describe('Apollo Service', () => {
  it('searches for people', async () => {
    const results = await searchPeople({ domain: 'test.com' });
    expect(results.people).toHaveLength(1);
    expect(results.people[0].name).toBe('Test User');
  });
});
```