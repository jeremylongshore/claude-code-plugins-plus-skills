# Implementation

## Implementation

### Health Check Endpoint
```typescript
// health/lindy.ts
import { Lindy } from '@lindy-ai/sdk';

export async function checkLindyHealth(): Promise<HealthStatus> {
  const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });
  const start = Date.now();

  try {
    await lindy.users.me();
    const latency = Date.now() - start;

    return {
      status: latency < 1000 ? 'healthy' : 'degraded',
      latency,
      timestamp: new Date().toISOString(),
    };
  } catch (error: any) {
    return {
      status: 'unhealthy',
      error: error.message,
      timestamp: new Date().toISOString(),
    };
  }
}
```

### Pre-Deployment Validation
```typescript
async function preDeploymentCheck(): Promise<boolean> {
  const checks = {
    apiKey: !!process.env.LINDY_API_KEY,
    environment: process.env.LINDY_ENVIRONMENT === 'production',
    connectivity: false,
    agents: false,
  };

  const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

  try {
    await lindy.users.me();
    checks.connectivity = true;

    const agents = await lindy.agents.list();
    checks.agents = agents.length > 0;
  } catch (e) {
    // Failed checks
  }

  const passed = Object.values(checks).every(Boolean);
  console.log('Pre-deployment checks:', checks);
  console.log(`Status: ${passed ? 'PASSED' : 'FAILED'}`);

  return passed;
}
```