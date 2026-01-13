# Migration Execution

## Migration Execution

### Phased Migration Strategy

```typescript
// src/migration/phased-migration.ts
interface MigrationPhase {
  name: string;
  percentage: number;
  criteria: any;
  validation: () => Promise<boolean>;
  rollbackPlan: () => Promise<void>;
}

const MIGRATION_PHASES: MigrationPhase[] = [
  {
    name: 'Pilot',
    percentage: 1,
    criteria: { createdAt: { gt: '2024-01-01' }, hasEmail: true },
    validation: async () => {
      const migrated = await getMigratedCount('pilot');
      const errors = await getErrorCount('pilot');
      return errors / migrated < 0.01; // Less than 1% error rate
    },
    rollbackPlan: async () => {
      await deleteApolloContacts({ tag: 'migration-pilot' });
    },
  },
  {
    name: 'Early Adopters',
    percentage: 10,
    criteria: { hasEmail: true, engagementScore: { gt: 50 } },
    validation: async () => {
      // Validate data integrity
      const sample = await sampleMigratedRecords(100);
      const integrity = await validateDataIntegrity(sample);
      return integrity.score > 0.95;
    },
    rollbackPlan: async () => {
      await deleteApolloContacts({ tag: 'migration-early' });
    },
  },
  {
    name: 'Main Migration',
    percentage: 75,
    criteria: { hasEmail: true },
    validation: async () => {
      // Full validation suite
      return await runFullValidation();
    },
    rollbackPlan: async () => {
      // This is risky - need careful planning
      console.warn('Full rollback required - contact support');
    },
  },
  {
    name: 'Cleanup',
    percentage: 14,
    criteria: {}, // Remaining records
    validation: async () => true,
    rollbackPlan: async () => {},
  },
];

async function executePhasedMigration(): Promise<void> {
  for (const phase of MIGRATION_PHASES) {
    console.log(`Starting phase: ${phase.name} (${phase.percentage}%)`);

    // Get records for this phase
    const records = await getRecordsForPhase(phase);
    console.log(`Found ${records.length} records for ${phase.name}`);

    // Migrate in batches
    const batchSize = 100;
    for (let i = 0; i < records.length; i += batchSize) {
      const batch = records.slice(i, i + batchSize);
      await migrateBatch(batch, phase.name);

      // Progress update
      console.log(`Progress: ${i + batch.length}/${records.length}`);

      // Rate limit
      await sleep(1000);
    }

    // Validate phase
    const isValid = await phase.validation();
    if (!isValid) {
      console.error(`Phase ${phase.name} validation failed!`);
      await phase.rollbackPlan();
      throw new Error(`Migration failed at phase: ${phase.name}`);
    }

    console.log(`Phase ${phase.name} completed successfully`);
  }
}
```

### Batch Migration Worker

```typescript
// src/migration/batch-worker.ts
import { Queue, Worker, Job } from 'bullmq';

interface MigrationJob {
  records: any[];
  phase: string;
  batchNumber: number;
}

const migrationQueue = new Queue('apollo-migration');

// Producer
async function enqueueMigrationBatch(
  records: any[],
  phase: string,
  batchNumber: number
): Promise<void> {
  await migrationQueue.add('migrate', {
    records,
    phase,
    batchNumber,
  }, {
    attempts: 3,
    backoff: {
      type: 'exponential',
      delay: 5000,
    },
    removeOnComplete: 100,
    removeOnFail: false,
  });
}

// Consumer
const worker = new Worker('apollo-migration', async (job: Job<MigrationJob>) => {
  const { records, phase, batchNumber } = job.data;

  const results = {
    success: 0,
    failed: 0,
    errors: [] as any[],
  };

  for (const record of records) {
    try {
      // Transform record
      const transformed = transformRecord(record, getMapping(record.source));

      if (transformed.errors.length > 0) {
        results.failed++;
        results.errors.push({ record, errors: transformed.errors });
        continue;
      }

      // Create in Apollo
      await apollo.createContact(transformed.data);

      // Store mapping for rollback
      await storeMigrationMapping(record.id, transformed.data.id, phase);

      results.success++;
    } catch (error: any) {
      results.failed++;
      results.errors.push({ record, error: error.message });
    }

    // Update job progress
    await job.updateProgress((results.success + results.failed) / records.length * 100);
  }

  // Log results
  console.log(`Batch ${batchNumber}: ${results.success} success, ${results.failed} failed`);

  if (results.errors.length > 0) {
    await storeFailedRecords(results.errors, phase, batchNumber);
  }

  return results;
});
```