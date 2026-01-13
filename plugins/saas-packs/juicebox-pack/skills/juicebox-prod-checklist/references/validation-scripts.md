# Validation Scripts

## Validation Scripts

### API Connectivity Check
```bash
#!/bin/bash
# validate-juicebox-prod.sh

echo "=== Juicebox Production Validation ==="

# Check API key is set
if [ -z "$JUICEBOX_API_KEY" ]; then
  echo "FAIL: JUICEBOX_API_KEY not set"
  exit 1
fi

# Test health endpoint
HEALTH=$(curl -s -w "%{http_code}" -o /dev/null https://api.juicebox.ai/v1/health)
if [ "$HEALTH" != "200" ]; then
  echo "FAIL: Health check returned $HEALTH"
  exit 1
fi
echo "PASS: Health check"

# Test authentication
AUTH=$(curl -s -w "%{http_code}" -o /dev/null \
  -H "Authorization: Bearer $JUICEBOX_API_KEY" \
  https://api.juicebox.ai/v1/auth/me)
if [ "$AUTH" != "200" ]; then
  echo "FAIL: Auth check returned $AUTH"
  exit 1
fi
echo "PASS: Authentication"

# Test sample search
SEARCH=$(curl -s -w "%{http_code}" -o /dev/null \
  -H "Authorization: Bearer $JUICEBOX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query":"test","limit":1}' \
  https://api.juicebox.ai/v1/search)
if [ "$SEARCH" != "200" ]; then
  echo "FAIL: Search test returned $SEARCH"
  exit 1
fi
echo "PASS: Search functionality"

echo "=== All production checks passed ==="
```

### Integration Test Suite
```typescript
// tests/production-readiness.test.ts
import { describe, it, expect } from 'vitest';
import { JuiceboxClient } from '@juicebox/sdk';

describe('Production Readiness', () => {
  const client = new JuiceboxClient({
    apiKey: process.env.JUICEBOX_API_KEY!
  });

  it('authenticates successfully', async () => {
    const user = await client.auth.me();
    expect(user.id).toBeDefined();
  });

  it('performs search within SLA', async () => {
    const start = Date.now();
    const results = await client.search.people({
      query: 'software engineer',
      limit: 10
    });
    const duration = Date.now() - start;

    expect(results.profiles.length).toBeGreaterThan(0);
    expect(duration).toBeLessThan(5000); // 5s SLA
  });

  it('handles rate limiting gracefully', async () => {
    // Implementation depends on your retry logic
  });
});
```