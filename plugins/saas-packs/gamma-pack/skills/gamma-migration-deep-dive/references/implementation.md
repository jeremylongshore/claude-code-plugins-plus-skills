# Implementation Guide

### Step 1: Inventory Source Presentations
```typescript
// scripts/migration-inventory.ts
interface SourcePresentation {
  id: string;
  title: string;
  source: 'powerpoint' | 'google' | 'canva' | 'other';
  path: string;
  size: number;
  lastModified: Date;
  slideCount?: number;
}

async function inventoryPresentations(sourceDir: string): Promise<SourcePresentation[]> {
  const files = await glob('**/*.{pptx,pdf,key}', { cwd: sourceDir });

  const inventory: SourcePresentation[] = [];

  for (const file of files) {
    const stats = await fs.stat(path.join(sourceDir, file));
    const ext = path.extname(file).toLowerCase();

    inventory.push({
      id: crypto.randomUUID(),
      title: path.basename(file, ext),
      source: detectSource(file),
      path: file,
      size: stats.size,
      lastModified: stats.mtime,
    });
  }

  // Save inventory
  await fs.writeFile(
    'migration-inventory.json',
    JSON.stringify(inventory, null, 2)
  );

  console.log(`Found ${inventory.length} presentations to migrate`);
  return inventory;
}
```

### Step 2: Migration Engine
```typescript
// lib/migration-engine.ts
import { GammaClient } from '@gamma/sdk';

interface MigrationResult {
  sourceId: string;
  gammaId?: string;
  success: boolean;
  error?: string;
  duration: number;
}

class MigrationEngine {
  private gamma: GammaClient;
  private results: MigrationResult[] = [];

  constructor() {
    this.gamma = new GammaClient({
      apiKey: process.env.GAMMA_API_KEY,
      timeout: 120000, // Long timeout for imports
    });
  }

  async migrateFile(source: SourcePresentation): Promise<MigrationResult> {
    const start = Date.now();

    try {
      // Read file
      const fileBuffer = await fs.readFile(source.path);

      // Upload to Gamma
      const presentation = await this.gamma.presentations.import({
        file: fileBuffer,
        filename: path.basename(source.path),
        title: source.title,
        preserveFormatting: true,
        convertToGammaStyle: false,
      });

      const result: MigrationResult = {
        sourceId: source.id,
        gammaId: presentation.id,
        success: true,
        duration: Date.now() - start,
      };

      this.results.push(result);
      return result;
    } catch (error) {
      const result: MigrationResult = {
        sourceId: source.id,
        success: false,
        error: error.message,
        duration: Date.now() - start,
      };

      this.results.push(result);
      return result;
    }
  }

  async migrateAll(
    sources: SourcePresentation[],
    options = { concurrency: 3, retries: 2 }
  ) {
    const queue = new PQueue({ concurrency: options.concurrency });

    const tasks = sources.map(source =>
      queue.add(async () => {
        for (let attempt = 0; attempt < options.retries; attempt++) {
          const result = await this.migrateFile(source);
          if (result.success) return result;

          console.log(`Retry ${attempt + 1} for ${source.title}`);
          await delay(5000 * (attempt + 1));
        }
      })
    );

    await Promise.all(tasks);
    return this.getReport();
  }

  getReport() {
    const successful = this.results.filter(r => r.success);
    const failed = this.results.filter(r => !r.success);

    return {
      total: this.results.length,
      successful: successful.length,
      failed: failed.length,
      successRate: (successful.length / this.results.length * 100).toFixed(1),
      averageDuration: successful.reduce((a, b) => a + b.duration, 0) / successful.length,
      failures: failed.map(f => ({ id: f.sourceId, error: f.error })),
    };
  }
}
```

### Step 3: Platform-Specific Handlers

#### Google Slides Migration
```typescript
// lib/google-slides-migrator.ts
import { google } from 'googleapis';

async function migrateFromGoogleSlides(
  driveFileId: string,
  gamma: GammaClient
) {
  const drive = google.drive('v3');

  // Export as PowerPoint
  const exportResponse = await drive.files.export({
    fileId: driveFileId,
    mimeType: 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
  }, { responseType: 'arraybuffer' });

  // Import to Gamma
  const presentation = await gamma.presentations.import({
    file: Buffer.from(exportResponse.data as ArrayBuffer),
    filename: 'exported.pptx',
    source: 'google_slides',
  });

  return presentation;
}
```

#### PowerPoint Migration with Metadata
```typescript
// lib/powerpoint-migrator.ts
import JSZip from 'jszip';
import { parseStringPromise } from 'xml2js';

async function extractPowerPointMetadata(filePath: string) {
  const fileBuffer = await fs.readFile(filePath);
  const zip = await JSZip.loadAsync(fileBuffer);

  // Extract core properties
  const coreXml = await zip.file('docProps/core.xml')?.async('string');
  if (!coreXml) return {};

  const core = await parseStringPromise(coreXml);

  return {
    title: core['cp:coreProperties']?.['dc:title']?.[0],
    creator: core['cp:coreProperties']?.['dc:creator']?.[0],
    created: core['cp:coreProperties']?.['dcterms:created']?.[0],
    modified: core['cp:coreProperties']?.['dcterms:modified']?.[0],
  };
}

async function migrateWithMetadata(source: SourcePresentation, gamma: GammaClient) {
  const metadata = await extractPowerPointMetadata(source.path);
  const fileBuffer = await fs.readFile(source.path);

  const presentation = await gamma.presentations.import({
    file: fileBuffer,
    filename: path.basename(source.path),
    title: metadata.title || source.title,
    metadata: {
      originalCreator: metadata.creator,
      originalCreated: metadata.created,
      migratedAt: new Date().toISOString(),
    },
  });

  return presentation;
}
```

### Step 4: Post-Migration Validation
```typescript
// scripts/validate-migration.ts
async function validateMigration(sourceId: string, gammaId: string) {
  const gamma = new GammaClient({ apiKey: process.env.GAMMA_API_KEY });

  const presentation = await gamma.presentations.get(gammaId, {
    include: ['slides', 'assets'],
  });

  const validations = {
    exists: !!presentation,
    hasSlides: presentation.slides?.length > 0,
    allAssetsLoaded: presentation.assets?.every(a => a.status === 'loaded'),
    canExport: false,
  };

  // Test export capability
  try {
    const exportTest = await gamma.exports.create(gammaId, {
      format: 'pdf',
      dryRun: true,
    });
    validations.canExport = exportTest.valid;
  } catch {
    validations.canExport = false;
  }

  return {
    sourceId,
    gammaId,
    validations,
    passed: Object.values(validations).every(v => v),
  };
}
```

### Step 5: Rollback Plan
```typescript
// lib/rollback.ts
interface MigrationSnapshot {
  timestamp: Date;
  mappings: Array<{ sourceId: string; gammaId: string }>;
}

async function createSnapshot(results: MigrationResult[]): Promise<string> {
  const snapshot: MigrationSnapshot = {
    timestamp: new Date(),
    mappings: results
      .filter(r => r.success && r.gammaId)
      .map(r => ({ sourceId: r.sourceId, gammaId: r.gammaId! })),
  };

  const snapshotPath = `migration-snapshot-${Date.now()}.json`;
  await fs.writeFile(snapshotPath, JSON.stringify(snapshot, null, 2));

  return snapshotPath;
}

async function rollbackMigration(snapshotPath: string) {
  const snapshot: MigrationSnapshot = JSON.parse(
    await fs.readFile(snapshotPath, 'utf-8')
  );

  const gamma = new GammaClient({ apiKey: process.env.GAMMA_API_KEY });

  console.log(`Rolling back ${snapshot.mappings.length} presentations...`);

  for (const mapping of snapshot.mappings) {
    try {
      await gamma.presentations.delete(mapping.gammaId);
      console.log(`Deleted: ${mapping.gammaId}`);
    } catch (error) {
      console.error(`Failed to delete ${mapping.gammaId}: ${error.message}`);
    }
  }

  console.log('Rollback complete');
}
```