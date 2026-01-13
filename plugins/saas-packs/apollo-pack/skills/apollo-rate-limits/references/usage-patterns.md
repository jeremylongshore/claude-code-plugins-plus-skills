# Usage Patterns

## Usage Patterns

### Pattern 1: Simple Rate-Limited Request
```typescript
import { withBackoff } from './backoff';

const people = await withBackoff(() =>
  apollo.searchPeople({
    q_organization_domains: ['stripe.com'],
    per_page: 100,
  })
);
```

### Pattern 2: Batch Processing with Queue
```typescript
import { apolloQueue } from './request-queue';

async function enrichCompanies(domains: string[]) {
  const results = [];

  for (const domain of domains) {
    const result = await apolloQueue.add(
      () => withBackoff(() => apollo.enrichOrganization(domain)),
      { priority: 1 } // Lower priority
    );
    results.push(result);
  }

  return results;
}
```

### Pattern 3: Priority Queue for Interactive vs Background
```typescript
// High priority for user-facing requests
async function interactiveSearch(query: string) {
  return apolloQueue.add(
    () => withBackoff(() => apollo.searchPeople({ q_keywords: query })),
    { priority: 0 } // Highest priority
  );
}

// Low priority for background sync
async function backgroundSync(contacts: string[]) {
  return Promise.all(
    contacts.map((id) =>
      apolloQueue.add(
        () => withBackoff(() => apollo.getContact(id)),
        { priority: 10 } // Low priority
      )
    )
  );
}
```