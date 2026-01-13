# Pattern 1: Type-Safe Client Singleton

## Pattern 1: Type-Safe Client Singleton

```typescript
// src/lib/apollo/client.ts
import axios, { AxiosInstance, AxiosError } from 'axios';
import { z } from 'zod';

// Response schemas
const PersonSchema = z.object({
  id: z.string(),
  name: z.string(),
  first_name: z.string().optional(),
  last_name: z.string().optional(),
  title: z.string().optional(),
  email: z.string().email().optional(),
  linkedin_url: z.string().url().optional(),
  organization: z.object({
    id: z.string(),
    name: z.string(),
    domain: z.string().optional(),
  }).optional(),
});

const PeopleSearchResponseSchema = z.object({
  people: z.array(PersonSchema),
  pagination: z.object({
    page: z.number(),
    per_page: z.number(),
    total_entries: z.number(),
    total_pages: z.number(),
  }),
});

export type Person = z.infer<typeof PersonSchema>;
export type PeopleSearchResponse = z.infer<typeof PeopleSearchResponseSchema>;

class ApolloClient {
  private static instance: ApolloClient;
  private client: AxiosInstance;

  private constructor() {
    this.client = axios.create({
      baseURL: 'https://api.apollo.io/v1',
      timeout: 30000,
      headers: { 'Content-Type': 'application/json' },
      params: { api_key: process.env.APOLLO_API_KEY },
    });

    this.setupInterceptors();
  }

  static getInstance(): ApolloClient {
    if (!ApolloClient.instance) {
      ApolloClient.instance = new ApolloClient();
    }
    return ApolloClient.instance;
  }

  private setupInterceptors() {
    this.client.interceptors.response.use(
      (response) => response,
      this.handleError.bind(this)
    );
  }

  private handleError(error: AxiosError) {
    if (error.response?.status === 429) {
      throw new ApolloRateLimitError('Rate limit exceeded');
    }
    if (error.response?.status === 401) {
      throw new ApolloAuthError('Invalid API key');
    }
    throw error;
  }

  async searchPeople(params: PeopleSearchParams): Promise<PeopleSearchResponse> {
    const { data } = await this.client.post('/people/search', params);
    return PeopleSearchResponseSchema.parse(data);
  }
}

export const apollo = ApolloClient.getInstance();
```