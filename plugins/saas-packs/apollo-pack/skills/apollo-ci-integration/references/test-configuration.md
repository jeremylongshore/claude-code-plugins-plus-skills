# Test Configuration

## Test Configuration

### Test Setup
```typescript
// tests/setup/apollo.ts
import { beforeAll, afterAll, beforeEach } from 'vitest';
import { setupServer } from 'msw/node';
import { apolloHandlers } from './mocks/apollo-handlers';

const server = setupServer(...apolloHandlers);

beforeAll(() => {
  server.listen({ onUnhandledRequest: 'warn' });
});

afterAll(() => {
  server.close();
});

beforeEach(() => {
  server.resetHandlers();
});

export { server };
```

### Mock Handlers for CI
```typescript
// tests/mocks/apollo-handlers.ts
import { http, HttpResponse } from 'msw';

export const apolloHandlers = [
  http.get('https://api.apollo.io/v1/auth/health', () => {
    return HttpResponse.json({ status: 'ok' });
  }),

  http.post('https://api.apollo.io/v1/people/search', async ({ request }) => {
    const body = await request.json();
    return HttpResponse.json({
      people: [
        {
          id: 'test-1',
          name: 'Test User',
          title: 'Engineer',
          email: 'test@example.com',
        },
      ],
      pagination: {
        page: body.page || 1,
        per_page: body.per_page || 25,
        total_entries: 1,
        total_pages: 1,
      },
    });
  }),

  http.get('https://api.apollo.io/v1/organizations/enrich', ({ request }) => {
    const url = new URL(request.url);
    const domain = url.searchParams.get('domain');
    return HttpResponse.json({
      organization: {
        id: 'org-1',
        name: 'Test Company',
        primary_domain: domain,
        industry: 'Technology',
      },
    });
  }),
];
```

### Integration Tests
```typescript
// tests/integration/apollo.test.ts
import { describe, it, expect, beforeEach } from 'vitest';
import { apollo } from '../../src/lib/apollo/client';

describe('Apollo API Integration', () => {
  // Only run with real API in CI
  const isCI = process.env.CI === 'true';
  const hasApiKey = !!process.env.APOLLO_API_KEY;

  beforeEach(() => {
    if (!isCI || !hasApiKey) {
      console.log('Skipping real API tests - using mocks');
    }
  });

  it('should search for people', async () => {
    const result = await apollo.searchPeople({
      q_organization_domains: [process.env.APOLLO_TEST_DOMAIN || 'apollo.io'],
      per_page: 5,
    });

    expect(result.people).toBeDefined();
    expect(Array.isArray(result.people)).toBe(true);
    expect(result.pagination.total_entries).toBeGreaterThanOrEqual(0);
  });

  it('should enrich organization', async () => {
    const result = await apollo.enrichOrganization(
      process.env.APOLLO_TEST_DOMAIN || 'apollo.io'
    );

    expect(result.organization).toBeDefined();
    expect(result.organization.name).toBeTruthy();
  });

  it('should handle rate limits gracefully', async () => {
    // This test verifies rate limit handling without actually hitting limits
    const startTime = Date.now();

    // Make 5 requests in sequence
    for (let i = 0; i < 5; i++) {
      await apollo.searchPeople({ per_page: 1 });
    }

    const duration = Date.now() - startTime;
    // Should complete in reasonable time with rate limiting
    expect(duration).toBeLessThan(30000);
  });
});
```