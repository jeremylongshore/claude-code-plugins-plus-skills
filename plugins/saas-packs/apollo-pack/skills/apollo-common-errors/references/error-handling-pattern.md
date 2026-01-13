# Error Handling Pattern

## Error Handling Pattern

```typescript
// src/lib/apollo/error-handler.ts
import { AxiosError } from 'axios';

export class ApolloErrorHandler {
  handle(error: AxiosError): never {
    const status = error.response?.status;
    const data = error.response?.data as any;

    switch (status) {
      case 401:
        throw new ApolloAuthError(
          'Invalid API key. Verify APOLLO_API_KEY is set correctly.'
        );
      case 403:
        throw new ApolloPermissionError(
          `Permission denied: ${data?.message || 'Check your plan features'}`
        );
      case 422:
        throw new ApolloValidationError(
          `Invalid request: ${data?.message}`,
          data?.errors
        );
      case 429:
        throw new ApolloRateLimitError(
          'Rate limit exceeded',
          this.parseRetryAfter(error)
        );
      case 500:
        throw new ApolloServerError(
          'Apollo server error. Check status.apollo.io'
        );
      default:
        throw new ApolloError(
          `Apollo API error: ${status} - ${data?.message || error.message}`
        );
    }
  }

  private parseRetryAfter(error: AxiosError): number {
    return parseInt(error.response?.headers['retry-after'] || '60');
  }
}
```