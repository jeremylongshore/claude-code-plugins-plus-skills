# Implementation Guide

### Step 1: Create Entry File
Create a new file for your hello world example.

### Step 2: Import and Initialize Client
```typescript
import axios from 'axios';

const apolloClient = axios.create({
  baseURL: 'https://api.apollo.io/v1',
  headers: { 'Content-Type': 'application/json' },
  params: { api_key: process.env.APOLLO_API_KEY },
});
```

### Step 3: Search for People
```typescript
async function searchPeople() {
  const response = await apolloClient.post('/people/search', {
    q_organization_domains: ['apollo.io'],
    page: 1,
    per_page: 10,
  });

  console.log('Found contacts:', response.data.people.length);
  response.data.people.forEach((person: any) => {
    console.log(`- ${person.name} (${person.title})`);
  });
}

searchPeople().catch(console.error);
```