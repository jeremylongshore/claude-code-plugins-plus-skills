# Implementation Guide

### Step 1: Analyze Current Usage
```typescript
import { Lindy } from '@lindy-ai/sdk';

async function analyzeUsage() {
  const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

  const usage = await lindy.usage.monthly({
    startDate: '2025-01-01',
    endDate: '2025-01-31',
  });

  const analysis = {
    totalRuns: usage.agentRuns.total,
    totalCost: usage.billing.total,
    costPerRun: usage.billing.total / usage.agentRuns.total,
    topAgents: usage.byAgent
      .sort((a: any, b: any) => b.cost - a.cost)
      .slice(0, 5),
    peakHours: usage.byHour
      .sort((a: any, b: any) => b.runs - a.runs)
      .slice(0, 5),
  };

  console.log('Usage Analysis:', analysis);
  return analysis;
}
```

### Step 2: Implement Usage Budgets
```typescript
interface Budget {
  monthly: number;
  daily: number;
  perAgent: number;
}

const budget: Budget = {
  monthly: 500, // $500/month
  daily: 20,    // $20/day
  perAgent: 50, // $50/agent/month
};

async function checkBudget(): Promise<boolean> {
  const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

  const usage = await lindy.usage.current();

  if (usage.billing.monthly >= budget.monthly) {
    console.error('Monthly budget exceeded!');
    await sendAlert('Budget exceeded', { usage, budget });
    return false;
  }

  if (usage.billing.today >= budget.daily) {
    console.warn('Daily budget exceeded');
    return false;
  }

  return true;
}
```

### Step 3: Optimize Agent Costs
```typescript
// Cost-optimized agent configuration
const optimizedAgent = {
  name: 'Cost-Efficient Agent',
  instructions: 'Be brief. Answer in 1-2 sentences.',
  config: {
    model: 'gpt-3.5-turbo', // Cheaper model
    maxTokens: 100,         // Limit output
    temperature: 0.3,       // Less creative = fewer tokens
  },
};

// Route simple queries to cheaper agents
async function routeQuery(input: string) {
  const isSimple = input.length < 100 && !input.includes('analyze');

  const agentId = isSimple
    ? 'agt_cheap_simple'
    : 'agt_expensive_complex';

  return lindy.agents.run(agentId, { input });
}
```

### Step 4: Implement Caching to Reduce Calls
```typescript
import NodeCache from 'node-cache';

const cache = new NodeCache({ stdTTL: 3600 }); // 1 hour cache

async function cachedRun(agentId: string, input: string) {
  const cacheKey = `${agentId}:${input}`;

  // Check cache first (free!)
  const cached = cache.get(cacheKey);
  if (cached) {
    console.log('Cache hit - $0');
    return cached;
  }

  // Only call API if cache miss
  const result = await lindy.agents.run(agentId, { input });
  cache.set(cacheKey, result);

  console.log('Cache miss - API call made');
  return result;
}
```

### Step 5: Set Up Cost Alerts
```typescript
async function setupCostAlerts() {
  const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

  // Alert at 80% of budget
  await lindy.billing.alerts.create({
    threshold: 400, // $400 of $500 budget
    type: 'monthly',
    channels: ['email', 'slack'],
    message: 'Approaching monthly budget limit',
  });

  // Daily anomaly detection
  await lindy.billing.alerts.create({
    threshold: 50, // 50% above average
    type: 'anomaly',
    channels: ['slack'],
    message: 'Unusual spending detected',
  });
}
```