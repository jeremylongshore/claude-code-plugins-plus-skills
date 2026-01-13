# Implementation Guide

### Step 1: Measure Baseline Performance
```typescript
import { Lindy } from '@lindy-ai/sdk';

interface PerformanceMetrics {
  avgLatency: number;
  p95Latency: number;
  p99Latency: number;
  throughput: number;
  errorRate: number;
}

async function measureBaseline(agentId: string, iterations = 100): Promise<PerformanceMetrics> {
  const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });
  const latencies: number[] = [];
  let errors = 0;

  const start = Date.now();

  for (let i = 0; i < iterations; i++) {
    const runStart = Date.now();
    try {
      await lindy.agents.run(agentId, { input: 'Benchmark test' });
      latencies.push(Date.now() - runStart);
    } catch (e) {
      errors++;
    }
  }

  const totalTime = (Date.now() - start) / 1000;
  latencies.sort((a, b) => a - b);

  return {
    avgLatency: latencies.reduce((a, b) => a + b, 0) / latencies.length,
    p95Latency: latencies[Math.floor(latencies.length * 0.95)],
    p99Latency: latencies[Math.floor(latencies.length * 0.99)],
    throughput: iterations / totalTime,
    errorRate: errors / iterations,
  };
}
```

### Step 2: Optimize Agent Instructions
```typescript
// BEFORE: Verbose instructions (slow)
const slowAgent = {
  instructions: `
    You are a helpful assistant that should carefully consider
    each request and provide detailed, comprehensive responses.
    Think step by step about each query. Consider all possibilities.
    Provide examples and explanations for everything.
  `,
};

// AFTER: Concise instructions (fast)
const fastAgent = {
  instructions: `
    Be concise. Answer directly. Skip pleasantries.
    Format: [Answer] (1-2 sentences)
  `,
  config: {
    maxTokens: 100, // Limit response length
  },
};
```

### Step 3: Enable Streaming
```typescript
// Non-streaming (waits for full response)
const result = await lindy.agents.run(agentId, { input });
console.log(result.output); // Logs after full response

// Streaming (immediate partial responses)
const stream = await lindy.agents.runStream(agentId, { input });

for await (const chunk of stream) {
  process.stdout.write(chunk.delta); // Real-time output
}
```

### Step 4: Implement Caching
```typescript
import NodeCache from 'node-cache';

const cache = new NodeCache({ stdTTL: 300 }); // 5 minute TTL

async function runWithCache(agentId: string, input: string) {
  const cacheKey = `${agentId}:${crypto.createHash('md5').update(input).digest('hex')}`;

  // Check cache
  const cached = cache.get(cacheKey);
  if (cached) {
    return cached;
  }

  // Run agent
  const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });
  const result = await lindy.agents.run(agentId, { input });

  // Cache result
  cache.set(cacheKey, result);

  return result;
}
```

### Step 5: Optimize Concurrency
```typescript
// Poor: Sequential execution
for (const input of inputs) {
  await lindy.agents.run(agentId, { input }); // Slow!
}

// Better: Parallel with controlled concurrency
import pLimit from 'p-limit';

const limit = pLimit(5); // Max 5 concurrent

const results = await Promise.all(
  inputs.map(input =>
    limit(() => lindy.agents.run(agentId, { input }))
  )
);
```