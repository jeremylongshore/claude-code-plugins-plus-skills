# Examples

### Python Example
```python
from juicebox import JuiceboxClient
import os

client = JuiceboxClient(api_key=os.environ.get('JUICEBOX_API_KEY'))

results = client.search.people(
    query='product manager in San Francisco',
    limit=10
)

for profile in results.profiles:
    print(f"- {profile.name} | {profile.title}")
```

### Advanced Search
```typescript
const results = await client.search.people({
  query: 'senior engineer',
  filters: {
    location: 'New York',
    company_size: '1000+',
    experience_years: { min: 5 }
  },
  limit: 20
});
```