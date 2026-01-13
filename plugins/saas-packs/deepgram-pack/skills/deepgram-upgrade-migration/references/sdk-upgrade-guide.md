# Sdk Upgrade Guide

## SDK Upgrade Guide

### Check Current Version
```bash
# Node.js
npm list @deepgram/sdk

# Python
pip show deepgram-sdk
```

### Review Changelog
```bash
# View npm package changelog
npm view @deepgram/sdk versions --json

# Or check GitHub releases
curl -s https://api.github.com/repos/deepgram/deepgram-js-sdk/releases/latest
```

### TypeScript SDK v2 to v3 Migration
```typescript
// v2 (old)
import Deepgram from '@deepgram/sdk';
const deepgram = new Deepgram(apiKey);
const response = await deepgram.transcription.preRecorded(
  { url: audioUrl },
  { punctuate: true }
);

// v3 (new)
import { createClient } from '@deepgram/sdk';
const deepgram = createClient(apiKey);
const { result, error } = await deepgram.listen.prerecorded.transcribeUrl(
  { url: audioUrl },
  { punctuate: true }
);
```

### Breaking Changes Checklist
```typescript
// lib/migration-check.ts
interface MigrationCheck {
  name: string;
  check: () => boolean;
  fix: string;
}

const v3MigrationChecks: MigrationCheck[] = [
  {
    name: 'Import statement',
    check: () => {
      // Check if old import style is used
      return true;
    },
    fix: 'Change: import Deepgram from "@deepgram/sdk" to import { createClient } from "@deepgram/sdk"',
  },
  {
    name: 'Client initialization',
    check: () => true,
    fix: 'Change: new Deepgram(key) to createClient(key)',
  },
  {
    name: 'Transcription method',
    check: () => true,
    fix: 'Change: deepgram.transcription.preRecorded() to deepgram.listen.prerecorded.transcribeUrl()',
  },
  {
    name: 'Response handling',
    check: () => true,
    fix: 'Change: const response = await ... to const { result, error } = await ...',
  },
  {
    name: 'Error handling',
    check: () => true,
    fix: 'Handle error in destructured response instead of try/catch only',
  },
];

export function runMigrationChecks() {
  console.log('=== SDK v3 Migration Checklist ===\n');
  for (const check of v3MigrationChecks) {
    console.log(`[ ] ${check.name}`);
    console.log(`    Fix: ${check.fix}\n`);
  }
}
```