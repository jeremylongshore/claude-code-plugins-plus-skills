# Rollback Strategy

## Rollback Strategy

```typescript
// src/migration/rollback.ts
interface RollbackPlan {
  phase: string;
  recordIds: string[];
  timestamp: Date;
}

async function createRollbackPlan(phase: string): Promise<RollbackPlan> {
  const mappings = await prisma.migrationMapping.findMany({
    where: { phase },
  });

  return {
    phase,
    recordIds: mappings.map(m => m.apolloId),
    timestamp: new Date(),
  };
}

async function executeRollback(plan: RollbackPlan): Promise<void> {
  console.log(`Rolling back ${plan.recordIds.length} records from phase: ${plan.phase}`);

  // Delete from Apollo in batches
  const batchSize = 50;
  for (let i = 0; i < plan.recordIds.length; i += batchSize) {
    const batch = plan.recordIds.slice(i, i + batchSize);

    await Promise.all(
      batch.map(async (id) => {
        try {
          // Apollo may not have delete API - mark as inactive instead
          await apollo.updateContact(id, { status: 'inactive' });
        } catch (error) {
          console.error(`Failed to rollback contact ${id}:`, error);
        }
      })
    );

    console.log(`Rollback progress: ${i + batch.length}/${plan.recordIds.length}`);
    await sleep(1000);
  }

  // Update migration mappings
  await prisma.migrationMapping.updateMany({
    where: { phase: plan.phase },
    data: { rolledBack: true, rolledBackAt: new Date() },
  });

  console.log(`Rollback complete for phase: ${plan.phase}`);
}
```