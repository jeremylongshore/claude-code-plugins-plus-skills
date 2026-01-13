# Model Migration Guide

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