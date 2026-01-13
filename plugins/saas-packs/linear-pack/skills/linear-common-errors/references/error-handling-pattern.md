# Error Handling Pattern

## Error Handling Pattern
```typescript
import { LinearClient, LinearError } from "@linear/sdk";

async function safeLinearCall<T>(
  operation: () => Promise<T>,
  context: string
): Promise<T> {
  try {
    return await operation();
  } catch (error) {
    if (error instanceof LinearError) {
      console.error(`Linear API Error in ${context}:`, {
        message: error.message,
        type: error.type,
        errors: error.errors,
      });

      // Handle specific error types
      switch (error.type) {
        case "AuthenticationError":
          throw new Error("Please check your Linear API key");
        case "RateLimitedError":
          throw new Error("Too many requests, please retry later");
        default:
          throw error;
      }
    }
    throw error;
  }
}
```