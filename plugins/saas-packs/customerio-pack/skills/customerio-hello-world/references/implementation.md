# Implementation Guide

### Step 1: Create Basic Integration
```typescript
// hello-customerio.ts
import { TrackClient, RegionUS } from '@customerio/track';

const client = new TrackClient(
  process.env.CUSTOMERIO_SITE_ID!,
  process.env.CUSTOMERIO_API_KEY!,
  { region: RegionUS }
);

async function main() {
  // Step 1: Identify a user
  await client.identify('user-123', {
    email: 'hello@example.com',
    first_name: 'Hello',
    created_at: Math.floor(Date.now() / 1000)
  });
  console.log('User identified');

  // Step 2: Track an event
  await client.track('user-123', {
    name: 'hello_world',
    data: {
      source: 'sdk-test',
      timestamp: new Date().toISOString()
    }
  });
  console.log('Event tracked');
}

main().catch(console.error);
```

### Step 2: Run the Example
```bash
npx ts-node hello-customerio.ts
```

### Step 3: Verify in Dashboard
1. Go to Customer.io dashboard
2. Navigate to People section
3. Search for "user-123" or "hello@example.com"
4. Verify user profile shows attributes
5. Check Activity tab for "hello_world" event