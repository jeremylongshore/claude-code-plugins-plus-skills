# Examples

### TypeScript Setup
```typescript
import axios, { AxiosInstance } from 'axios';

interface ApolloClientConfig {
  apiKey: string;
  baseURL?: string;
}

export function createApolloClient(config: ApolloClientConfig): AxiosInstance {
  return axios.create({
    baseURL: config.baseURL || 'https://api.apollo.io/v1',
    headers: {
      'Content-Type': 'application/json',
    },
    params: {
      api_key: config.apiKey,
    },
  });
}

const client = createApolloClient({
  apiKey: process.env.APOLLO_API_KEY!,
});
```

### Python Setup
```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class ApolloClient:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get('APOLLO_API_KEY')
        self.base_url = 'https://api.apollo.io/v1'

    def _request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        params = kwargs.pop('params', {})
        params['api_key'] = self.api_key
        return requests.request(method, url, params=params, **kwargs)

client = ApolloClient()
```