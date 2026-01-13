---
name: deepgram-upgrade-migration
license: MIT
allowed-tools: Read, Grep, Bash
description: Plan and execute deepgram sdk upgrades and migrations. use when upgrading
  sdk versions, migrating to new api versions, or transitioning between deepgram models.
  trigger with phrases like "upgrade deepgram", "deepgram migration", "update deepgram
  s...
---
# Deepgram Upgrade Migration

## Overview
Guide for planning and executing Deepgram SDK upgrades and API migrations safely.

## Prerequisites
- Current SDK version documented
- Test environment available
- Rollback plan prepared
- Changelog reviewed

## Migration Types

### 1. SDK Version Upgrade
Upgrading the Deepgram SDK package (e.g., v2.x to v3.x)

### 2. Model Migration
Transitioning between transcription models (e.g., Nova to Nova-2)

### 3. API Version Migration
Moving between API versions (v1 to v2)

## Instructions

### Step 1: Assess Current State
Document current versions, configurations, and usage patterns.

### Step 2: Review Breaking Changes
Check changelogs and migration guides for breaking changes.

### Step 3: Plan Migration
Create detailed migration plan with rollback procedures.

### Step 4: Test Thoroughly
Test in staging environment before production rollout.

### Step 5: Execute Migration
Perform migration with monitoring and validation.

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

## Model Migration Guide

### Nova to Nova-2 Migration
```typescript
// Model comparison
const modelComparison = {
  'nova': {
    accuracy: 'Good',
    speed: 'Fast',
    languages: 36,
    deprecated: false,
  },
  'nova-2': {
    accuracy: 'Best',
    speed: 'Fast',
    languages: 47,
    deprecated: false,
  },
};

// Migration is simple - just change the model parameter
const { result, error } = await deepgram.listen.prerecorded.transcribeUrl(
  { url: audioUrl },
  {
    model: 'nova-2',  // Changed from 'nova'
    // All other options remain the same
    smart_format: true,
    punctuate: true,
    diarize: true,
  }
);
```

### A/B Testing Models
```typescript
// lib/model-ab-test.ts
interface ModelTestResult {
  model: string;
  transcript: string;
  confidence: number;
  processingTime: number;
}

export async function compareModels(
  audioUrl: string,
  models: string[] = ['nova', 'nova-2']
): Promise<ModelTestResult[]> {
  const client = createClient(process.env.DEEPGRAM_API_KEY!);
  const results: ModelTestResult[] = [];

  for (const model of models) {
    const startTime = Date.now();

    const { result, error } = await client.listen.prerecorded.transcribeUrl(
      { url: audioUrl },
      { model, smart_format: true }
    );

    if (error) {
      console.error(`Error with model ${model}:`, error);
      continue;
    }

    const alternative = result.results.channels[0].alternatives[0];

    results.push({
      model,
      transcript: alternative.transcript,
      confidence: alternative.confidence,
      processingTime: Date.now() - startTime,
    });
  }

  return results;
}

// Compare results
function analyzeResults(results: ModelTestResult[]) {
  console.log('\n=== Model Comparison ===\n');

  for (const result of results) {
    console.log(`Model: ${result.model}`);
    console.log(`  Confidence: ${(result.confidence * 100).toFixed(2)}%`);
    console.log(`  Processing Time: ${result.processingTime}ms`);
    console.log(`  Transcript Length: ${result.transcript.length} chars`);
    console.log();
  }

  // Find best model
  const best = results.reduce((a, b) =>
    a.confidence > b.confidence ? a : b
  );
  console.log(`Best Model: ${best.model} (${(best.confidence * 100).toFixed(2)}% confidence)`);
}
```

## Rollback Plan

### Prepare Rollback
```typescript
// lib/rollback.ts
interface DeploymentVersion {
  sdkVersion: string;
  model: string;
  config: Record<string, unknown>;
  deployedAt: Date;
}

class RollbackManager {
  private versions: DeploymentVersion[] = [];
  private maxVersions = 5;

  recordDeployment(version: Omit<DeploymentVersion, 'deployedAt'>) {
    this.versions.unshift({
      ...version,
      deployedAt: new Date(),
    });

    // Keep only last N versions
    this.versions = this.versions.slice(0, this.maxVersions);
  }

  getLastStableVersion(): DeploymentVersion | null {
    return this.versions[1] || null; // Skip current version
  }

  getRollbackInstructions(target: DeploymentVersion): string[] {
    return [
      `1. Update package.json: "@deepgram/sdk": "${target.sdkVersion}"`,
      `2. Run: npm install`,
      `3. Update config: model = "${target.model}"`,
      `4. Verify: npm test`,
      `5. Deploy: npm run deploy`,
      `6. Monitor: Check dashboards for 30 minutes`,
    ];
  }
}
```

### Emergency Rollback Script
```bash
#!/bin/bash
# scripts/emergency-rollback.sh

set -e

echo "=== Emergency Rollback ==="

# Store current version
CURRENT_VERSION=$(npm list @deepgram/sdk --json | jq -r '.dependencies["@deepgram/sdk"].version')
echo "Current version: $CURRENT_VERSION"

# Get previous version from git
git show HEAD~1:package-lock.json > /tmp/prev-lock.json
PREV_VERSION=$(cat /tmp/prev-lock.json | jq -r '.packages["node_modules/@deepgram/sdk"].version')
echo "Rolling back to: $PREV_VERSION"

# Confirm
read -p "Proceed with rollback? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  exit 1
fi

# Rollback
npm install @deepgram/sdk@$PREV_VERSION --save-exact

# Verify
npm test

echo "Rollback complete. Deploy when ready."
```

## Migration Validation

### Validation Script
```typescript
// scripts/validate-migration.ts
import { createClient } from '@deepgram/sdk';

interface ValidationResult {
  test: string;
  passed: boolean;
  details?: string;
}

async function validateMigration(): Promise<ValidationResult[]> {
  const results: ValidationResult[] = [];
  const client = createClient(process.env.DEEPGRAM_API_KEY!);

  // Test 1: API connectivity
  try {
    const { error } = await client.manage.getProjects();
    results.push({
      test: 'API Connectivity',
      passed: !error,
      details: error?.message,
    });
  } catch (err) {
    results.push({
      test: 'API Connectivity',
      passed: false,
      details: err instanceof Error ? err.message : 'Unknown error',
    });
  }

  // Test 2: Pre-recorded transcription
  try {
    const { result, error } = await client.listen.prerecorded.transcribeUrl(
      { url: 'https://static.deepgram.com/examples/nasa-podcast.wav' },
      { model: 'nova-2', smart_format: true }
    );

    results.push({
      test: 'Pre-recorded Transcription',
      passed: !error && !!result?.results?.channels?.[0]?.alternatives?.[0]?.transcript,
      details: error?.message,
    });
  } catch (err) {
    results.push({
      test: 'Pre-recorded Transcription',
      passed: false,
      details: err instanceof Error ? err.message : 'Unknown error',
    });
  }

  // Test 3: Live transcription connection
  try {
    const connection = client.listen.live({ model: 'nova-2' });

    await new Promise<void>((resolve, reject) => {
      connection.on('open', () => {
        connection.finish();
        resolve();
      });
      connection.on('error', reject);
      setTimeout(() => reject(new Error('Timeout')), 10000);
    });

    results.push({
      test: 'Live Transcription',
      passed: true,
    });
  } catch (err) {
    results.push({
      test: 'Live Transcription',
      passed: false,
      details: err instanceof Error ? err.message : 'Unknown error',
    });
  }

  return results;
}

// Run validation
validateMigration().then(results => {
  console.log('\n=== Migration Validation Results ===\n');

  for (const result of results) {
    const status = result.passed ? 'PASS' : 'FAIL';
    console.log(`[${status}] ${result.test}`);
    if (result.details) {
      console.log(`       ${result.details}`);
    }
  }

  const allPassed = results.every(r => r.passed);
  process.exit(allPassed ? 0 : 1);
});
```

## Resources
- [Deepgram SDK Changelog](https://github.com/deepgram/deepgram-js-sdk/releases)
- [Deepgram Python SDK Changelog](https://github.com/deepgram/deepgram-python-sdk/releases)
- [Model Migration Guide](https://developers.deepgram.com/docs/model-migration)
- [API Deprecation Schedule](https://developers.deepgram.com/docs/deprecation)

## Next Steps
Proceed to `deepgram-ci-integration` for CI/CD integration.
