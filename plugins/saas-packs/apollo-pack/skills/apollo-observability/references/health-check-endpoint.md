# Health Check Endpoint

## Health Check Endpoint

```typescript
// src/routes/health/apollo.ts
import { Router } from 'express';
import { register } from '../../lib/apollo/metrics';

const router = Router();

router.get('/health/apollo', async (req, res) => {
  const checks = {
    api: false,
    rateLimit: false,
    cache: false,
  };

  try {
    // Check API connectivity
    await apollo.healthCheck();
    checks.api = true;

    // Check rate limit status
    const remaining = apolloRateLimitRemaining.get();
    checks.rateLimit = remaining > 10;

    // Check cache health
    const cacheStats = apolloCache.getStats();
    checks.cache = cacheStats.size > 0;

    const healthy = Object.values(checks).every(Boolean);

    res.status(healthy ? 200 : 503).json({
      status: healthy ? 'healthy' : 'degraded',
      checks,
      timestamp: new Date().toISOString(),
    });
  } catch (error: any) {
    res.status(503).json({
      status: 'unhealthy',
      error: error.message,
      checks,
    });
  }
});

router.get('/metrics', async (req, res) => {
  res.set('Content-Type', register.contentType);
  res.end(await register.metrics());
});

export default router;
```