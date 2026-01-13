# Migration Validation

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