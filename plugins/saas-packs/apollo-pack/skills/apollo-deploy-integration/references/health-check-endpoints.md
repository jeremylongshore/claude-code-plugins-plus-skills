# Health Check Endpoints

## Health Check Endpoints

```typescript
// src/routes/health.ts
import { Router } from 'express';
import { apollo } from '../lib/apollo/client';

const router = Router();

// Basic health check
router.get('/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Apollo-specific health check
router.get('/health/apollo', async (req, res) => {
  try {
    const start = Date.now();
    await apollo.healthCheck();
    const latency = Date.now() - start;

    res.json({
      status: 'ok',
      apollo: {
        connected: true,
        latencyMs: latency,
      },
    });
  } catch (error: any) {
    res.status(503).json({
      status: 'degraded',
      apollo: {
        connected: false,
        error: error.message,
      },
    });
  }
});

// Readiness check (for Kubernetes)
router.get('/ready', async (req, res) => {
  try {
    await apollo.healthCheck();
    res.json({ ready: true });
  } catch {
    res.status(503).json({ ready: false });
  }
});

export default router;
```