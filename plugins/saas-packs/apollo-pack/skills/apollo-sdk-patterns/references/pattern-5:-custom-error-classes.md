# Pattern 5: Custom Error Classes

## Pattern 5: Custom Error Classes

```typescript
// src/lib/apollo/errors.ts
export class ApolloError extends Error {
  constructor(message: string, public readonly code?: string) {
    super(message);
    this.name = 'ApolloError';
  }
}

export class ApolloRateLimitError extends ApolloError {
  constructor(message: string = 'Rate limit exceeded') {
    super(message, 'RATE_LIMIT');
    this.name = 'ApolloRateLimitError';
  }
}

export class ApolloAuthError extends ApolloError {
  constructor(message: string = 'Authentication failed') {
    super(message, 'AUTH_ERROR');
    this.name = 'ApolloAuthError';
  }
}

export class ApolloValidationError extends ApolloError {
  constructor(message: string, public readonly details?: unknown) {
    super(message, 'VALIDATION_ERROR');
    this.name = 'ApolloValidationError';
  }
}
```