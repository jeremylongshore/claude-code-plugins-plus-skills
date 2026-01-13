# Implementation Guide

### Step 1: Environment Setup
```bash
# Create environment files
touch .env .env.example .env.test

# Add to .gitignore
echo '.env' >> .gitignore
echo '.env.local' >> .gitignore
```

```bash
# .env.example (commit this)
APOLLO_API_KEY=your-api-key-here
APOLLO_RATE_LIMIT=100
APOLLO_ENV=development
```

### Step 2: Create Development Client
```typescript
// src/lib/apollo-dev.ts
import axios from 'axios';

const isDev = process.env.NODE_ENV !== 'production';

export const apolloClient = axios.create({
  baseURL: 'https://api.apollo.io/v1',
  params: { api_key: process.env.APOLLO_API_KEY },
});

// Add request logging in development
if (isDev) {
  apolloClient.interceptors.request.use((config) => {
    console.log(`[Apollo] ${config.method?.toUpperCase()} ${config.url}`);
    return config;
  });

  apolloClient.interceptors.response.use(
    (response) => {
      console.log(`[Apollo] Response: ${response.status}`);
      return response;
    },
    (error) => {
      console.error(`[Apollo] Error: ${error.response?.status}`, error.message);
      return Promise.reject(error);
    }
  );
}
```

### Step 3: Create Mock Server for Testing
```typescript
// src/mocks/apollo-mock.ts
import { rest } from 'msw';

export const apolloHandlers = [
  rest.post('https://api.apollo.io/v1/people/search', (req, res, ctx) => {
    return res(
      ctx.json({
        people: [
          { id: '1', name: 'Test User', title: 'Engineer', email: 'test@example.com' },
        ],
        pagination: { page: 1, per_page: 10, total_entries: 1 },
      })
    );
  }),

  rest.get('https://api.apollo.io/v1/organizations/enrich', (req, res, ctx) => {
    return res(
      ctx.json({
        organization: {
          name: 'Test Company',
          domain: 'test.com',
          industry: 'Technology',
        },
      })
    );
  }),
];
```

### Step 4: Development Scripts
```json
{
  "scripts": {
    "dev": "NODE_ENV=development tsx watch src/index.ts",
    "dev:mock": "MOCK_APOLLO=true npm run dev",
    "test:apollo": "vitest run src/**/*.apollo.test.ts",
    "apollo:quota": "tsx scripts/check-apollo-quota.ts"
  }
}
```

### Step 5: Quota Monitoring Script
```typescript
// scripts/check-apollo-quota.ts
import { apolloClient } from '../src/lib/apollo-dev';

async function checkQuota() {
  try {
    const { data } = await apolloClient.get('/auth/health');
    console.log('API Status:', data);
    // Note: Apollo doesn't expose quota directly, track usage manually
  } catch (error: any) {
    if (error.response?.status === 429) {
      console.error('Rate limited! Wait before making more requests.');
    }
  }
}

checkQuota();
```