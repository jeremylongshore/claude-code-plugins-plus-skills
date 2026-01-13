# Data Retention

## Data Retention

```typescript
// src/jobs/data-retention.job.ts
import { CronJob } from 'cron';

// Run daily at 2 AM
const retentionJob = new CronJob('0 2 * * *', async () => {
  console.log('Starting data retention cleanup...');

  const retentionPolicies = [
    { table: 'contacts', field: 'lastActivityAt', maxAgeDays: 730 },
    { table: 'engagements', field: 'occurredAt', maxAgeDays: 365 },
    { table: 'auditLogs', field: 'createdAt', maxAgeDays: 2555 }, // 7 years
  ];

  for (const policy of retentionPolicies) {
    const cutoffDate = new Date();
    cutoffDate.setDate(cutoffDate.getDate() - policy.maxAgeDays);

    const deleted = await prisma[policy.table].deleteMany({
      where: {
        [policy.field]: { lt: cutoffDate },
      },
    });

    console.log(`Deleted ${deleted.count} records from ${policy.table}`);
  }

  // Archive before deletion for compliance
  await archiveOldData();
});

async function archiveOldData(): Promise<void> {
  const archiveCutoff = new Date();
  archiveCutoff.setDate(archiveCutoff.getDate() - 365);

  // Export to cold storage before deletion
  const oldContacts = await prisma.contact.findMany({
    where: { lastActivityAt: { lt: archiveCutoff } },
  });

  if (oldContacts.length > 0) {
    await uploadToArchive('contacts', oldContacts);
  }
}
```