# Implementation Guide

### Step 1: Create Search Script
```typescript
// search.ts
import { JuiceboxClient } from '@juicebox/sdk';

const client = new JuiceboxClient({
  apiKey: process.env.JUICEBOX_API_KEY
});

async function searchPeople() {
  const results = await client.search.people({
    query: 'software engineer at Google',
    limit: 5
  });

  console.log(`Found ${results.total} people`);
  results.profiles.forEach(profile => {
    console.log(`- ${profile.name} | ${profile.title} at ${profile.company}`);
  });
}

searchPeople();
```

### Step 2: Run the Search
```bash
npx ts-node search.ts
```

### Step 3: Verify Output
Expected output:
```
Found 150 people
- Jane Smith | Senior Software Engineer at Google
- John Doe | Staff Engineer at Google
- ...
```