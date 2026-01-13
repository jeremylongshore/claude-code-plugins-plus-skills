# Examples

### TypeScript Example - People Search
```typescript
import axios from 'axios';

const client = axios.create({
  baseURL: 'https://api.apollo.io/v1',
  params: { api_key: process.env.APOLLO_API_KEY },
});

interface Person {
  id: string;
  name: string;
  title: string;
  email: string;
  organization: { name: string };
}

async function main() {
  // Search for people at a company
  const { data } = await client.post('/people/search', {
    q_organization_domains: ['stripe.com'],
    person_titles: ['engineer', 'developer'],
    page: 1,
    per_page: 5,
  });

  console.log('People Search Results:');
  data.people.forEach((person: Person) => {
    console.log(`  ${person.name} - ${person.title} at ${person.organization?.name}`);
  });
}

main().catch(console.error);
```

### Python Example - Company Enrichment
```python
import os
import requests

APOLLO_API_KEY = os.environ.get('APOLLO_API_KEY')
BASE_URL = 'https://api.apollo.io/v1'

def enrich_company(domain: str):
    response = requests.get(
        f'{BASE_URL}/organizations/enrich',
        params={
            'api_key': APOLLO_API_KEY,
            'domain': domain,
        }
    )
    return response.json()

if __name__ == '__main__':
    company = enrich_company('apollo.io')
    org = company.get('organization', {})
    print(f"Company: {org.get('name')}")
    print(f"Industry: {org.get('industry')}")
    print(f"Employees: {org.get('estimated_num_employees')}")
```