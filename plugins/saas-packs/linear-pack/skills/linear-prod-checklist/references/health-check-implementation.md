# Health Check Implementation

## Health Check Implementation

```typescript
// health/linear.ts
import { LinearClient } from "@linear/sdk";

interface HealthStatus {
  status: "healthy" | "degraded" | "unhealthy";
  latencyMs: number;
  details: {
    authentication: boolean;
    apiReachable: boolean;
    rateLimitOk: boolean;
  };
  timestamp: string;
}

export async function checkHealth(client: LinearClient): Promise<HealthStatus> {
  const start = Date.now();
  const details = {
    authentication: false,
    apiReachable: false,
    rateLimitOk: true,
  };

  try {
    // Test authentication
    const viewer = await client.viewer;
    details.authentication = true;
    details.apiReachable = true;

    // Check if we're close to rate limits
    // (Would need to track this from headers)

    return {
      status: "healthy",
      latencyMs: Date.now() - start,
      details,
      timestamp: new Date().toISOString(),
    };
  } catch (error: any) {
    details.apiReachable = error.type !== "NetworkError";

    return {
      status: "unhealthy",
      latencyMs: Date.now() - start,
      details,
      timestamp: new Date().toISOString(),
    };
  }
}
```