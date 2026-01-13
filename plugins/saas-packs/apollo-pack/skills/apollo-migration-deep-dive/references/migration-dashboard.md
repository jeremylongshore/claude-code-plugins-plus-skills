# Migration Dashboard

## Migration Dashboard

```typescript
// src/routes/admin/migration.ts
router.get('/migration/status', async (req, res) => {
  const status = {
    phases: await getMigrationPhaseStatus(),
    progress: await getOverallProgress(),
    errors: await getRecentErrors(50),
    queue: await getQueueStatus(),
  };

  res.json(status);
});

router.post('/migration/pause', async (req, res) => {
  await migrationQueue.pause();
  res.json({ status: 'paused' });
});

router.post('/migration/resume', async (req, res) => {
  await migrationQueue.resume();
  res.json({ status: 'resumed' });
});

router.post('/migration/rollback/:phase', async (req, res) => {
  const plan = await createRollbackPlan(req.params.phase);
  await executeRollback(plan);
  res.json({ status: 'rolled back', plan });
});
```