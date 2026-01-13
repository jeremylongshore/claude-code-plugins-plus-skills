# Examples

### TypeScript Setup
```typescript
import { LinearClient } from "@linear/sdk";

const linearClient = new LinearClient({
  apiKey: process.env.LINEAR_API_KEY,
});

// Verify connection
async function verifyConnection() {
  try {
    const viewer = await linearClient.viewer;
    console.log(`Connected as ${viewer.name}`);
    return true;
  } catch (error) {
    console.error("Linear connection failed:", error);
    return false;
  }
}
```

### OAuth Setup (for user-facing apps)
```typescript
import { LinearClient } from "@linear/sdk";

// OAuth tokens from your OAuth flow
const client = new LinearClient({
  accessToken: userAccessToken,
});
```