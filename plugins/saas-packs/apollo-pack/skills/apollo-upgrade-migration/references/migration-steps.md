# Migration Steps

## Migration Steps

### Step 1: Create Compatibility Layer
```typescript
// src/lib/apollo/compat.ts
import { apollo } from './client';

/**
 * Compatibility layer for deprecated API patterns.
 * Remove after all code is updated.
 * @deprecated Use new API directly
 */
export const apolloCompat = {
  /**
   * @deprecated Use apollo.searchPeople()
   */
  async searchContacts(params: any) {
    console.warn('searchContacts is deprecated, use searchPeople');
    return apollo.searchPeople(params);
  },

  /**
   * @deprecated Use q_organization_domains parameter
   */
  async searchByCompanyName(companyName: string) {
    console.warn('searchByCompanyName is deprecated');
    // Try to find domain from company name
    const orgSearch = await apollo.searchOrganizations({
      q_organization_name: companyName,
      per_page: 1,
    });

    if (orgSearch.organizations.length === 0) {
      throw new Error(`Company not found: ${companyName}`);
    }

    const domain = orgSearch.organizations[0].primary_domain;
    return apollo.searchPeople({
      q_organization_domains: [domain],
    });
  },
};
```

### Step 2: Update Imports Gradually
```typescript
// Before migration
import { searchContacts } from '../lib/apollo/legacy';

// During migration (use compat layer)
import { apolloCompat } from '../lib/apollo/compat';
const results = await apolloCompat.searchContacts(params);

// After migration (use new API)
import { apollo } from '../lib/apollo/client';
const results = await apollo.searchPeople(params);
```

### Step 3: Feature Flag for New API
```typescript
// src/lib/apollo/feature-flags.ts
export const USE_NEW_APOLLO_API = process.env.APOLLO_USE_NEW_API === 'true';

// src/services/leads.ts
import { apollo } from '../lib/apollo/client';
import { apolloCompat } from '../lib/apollo/compat';
import { USE_NEW_APOLLO_API } from '../lib/apollo/feature-flags';

export async function searchLeads(criteria: SearchCriteria) {
  if (USE_NEW_APOLLO_API) {
    return apollo.searchPeople({
      q_organization_domains: criteria.domains,
      person_titles: criteria.titles,
    });
  } else {
    // Legacy path
    return apolloCompat.searchContacts({
      organization_domains: criteria.domains,
      titles: criteria.titles,
    });
  }
}
```

### Step 4: Parallel Testing
```typescript
// scripts/compare-api-results.ts
import { apollo } from '../src/lib/apollo/client';
import { apolloCompat } from '../src/lib/apollo/compat';

async function compareResults() {
  const testCases = [
    { domains: ['stripe.com'], titles: ['Engineer'] },
    { domains: ['apollo.io'], titles: ['Sales'] },
  ];

  for (const testCase of testCases) {
    console.log(`\nTesting: ${JSON.stringify(testCase)}`);

    // New API
    const newResult = await apollo.searchPeople({
      q_organization_domains: testCase.domains,
      person_titles: testCase.titles,
      per_page: 10,
    });

    // Legacy API (through compat)
    const legacyResult = await apolloCompat.searchContacts({
      organization_domains: testCase.domains,
      titles: testCase.titles,
      per_page: 10,
    });

    // Compare
    const newCount = newResult.people.length;
    const legacyCount = legacyResult.people.length;

    console.log(`  New API: ${newCount} results`);
    console.log(`  Legacy:  ${legacyCount} results`);
    console.log(`  Match:   ${newCount === legacyCount ? 'YES' : 'NO'}`);
  }
}

compareResults().catch(console.error);
```