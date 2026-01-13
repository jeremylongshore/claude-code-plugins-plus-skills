# Data Export

## Data Export

```typescript
// src/services/export/export.service.ts
import { stringify } from 'csv-stringify/sync';
import { createWriteStream } from 'fs';
import archiver from 'archiver';

interface ExportOptions {
  format: 'csv' | 'json';
  includeEngagements: boolean;
  dateRange?: { start: Date; end: Date };
}

export async function exportContactData(
  criteria: any,
  options: ExportOptions
): Promise<string> {
  const contacts = await prisma.contact.findMany({
    where: {
      ...criteria,
      ...(options.dateRange && {
        createdAt: {
          gte: options.dateRange.start,
          lte: options.dateRange.end,
        },
      }),
    },
    include: options.includeEngagements ? { engagements: true } : undefined,
  });

  const filename = `apollo-export-${Date.now()}`;

  if (options.format === 'csv') {
    const csv = stringify(contacts, {
      header: true,
      columns: ['id', 'email', 'name', 'title', 'company', 'createdAt'],
    });
    await writeFile(`exports/${filename}.csv`, csv);
    return `${filename}.csv`;
  } else {
    await writeFile(`exports/${filename}.json`, JSON.stringify(contacts, null, 2));
    return `${filename}.json`;
  }
}

export async function createSecureExport(
  contacts: any[],
  encryptionKey: string
): Promise<Buffer> {
  const data = JSON.stringify(contacts);
  const encrypted = await encrypt(data, encryptionKey);
  return encrypted;
}
```