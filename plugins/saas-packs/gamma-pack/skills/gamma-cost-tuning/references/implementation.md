# Implementation Guide

### Step 1: Usage Monitoring
```typescript
// Track usage per operation
interface UsageTracker {
  presentations: number;
  generations: number;
  exports: number;
  apiCalls: number;
}

const dailyUsage: UsageTracker = {
  presentations: 0,
  generations: 0,
  exports: 0,
  apiCalls: 0,
};

function trackUsage(operation: keyof UsageTracker) {
  dailyUsage[operation]++;

  // Check if approaching limits
  const limits = { presentations: 100, generations: 50, exports: 100, apiCalls: 60 };
  const percentage = (dailyUsage[operation] / limits[operation]) * 100;

  if (percentage >= 80) {
    console.warn(`Warning: ${operation} usage at ${percentage}%`);
    alertOps(`Gamma ${operation} usage high: ${percentage}%`);
  }
}

// Wrap API calls
async function createPresentation(opts: object) {
  trackUsage('apiCalls');
  trackUsage('presentations');
  if (opts.generateAI) trackUsage('generations');

  return gamma.presentations.create(opts);
}
```

### Step 2: Implement Usage Quotas
```typescript
interface UserQuota {
  userId: string;
  presentationsRemaining: number;
  generationsRemaining: number;
  exportsRemaining: number;
  resetsAt: Date;
}

async function checkQuota(userId: string, operation: string): Promise<boolean> {
  const quota = await getQuota(userId);

  const quotaField = `${operation}Remaining` as keyof UserQuota;
  if (typeof quota[quotaField] === 'number' && quota[quotaField] <= 0) {
    throw new QuotaExceededError(`${operation} quota exceeded`);
  }

  return true;
}

async function consumeQuota(userId: string, operation: string) {
  await db.quotas.update({
    where: { userId },
    data: { [`${operation}Remaining`]: { decrement: 1 } },
  });
}

// Usage in API route
app.post('/api/presentations', async (req, res) => {
  await checkQuota(req.userId, 'presentations');
  const result = await gamma.presentations.create(req.body);
  await consumeQuota(req.userId, 'presentations');
  res.json(result);
});
```

### Step 3: Optimize AI Generation Usage
```typescript
// Expensive: Full AI generation for each request
const expensive = await gamma.presentations.create({
  prompt: 'Create 20 slides about AI',
  generateAI: true,
  slideCount: 20, // Uses lots of AI credits
});

// Cost-effective: Template + targeted AI
const costEffective = await gamma.presentations.create({
  template: 'business-pitch', // Pre-made structure
  title: 'Our AI Solution',
  slides: [
    { title: 'Introduction', content: predefinedContent },
    { title: 'Problem', generateAI: true }, // AI only where needed
    { title: 'Solution', generateAI: true },
    { title: 'Team', content: teamData }, // No AI needed
    { title: 'Contact', content: contactInfo },
  ],
});
```

### Step 4: Caching to Reduce API Calls
```typescript
import Redis from 'ioredis';

const redis = new Redis(process.env.REDIS_URL);
const CACHE_TTL = 3600; // 1 hour

async function getCachedOrFetch<T>(
  key: string,
  fetchFn: () => Promise<T>
): Promise<T> {
  // Check cache
  const cached = await redis.get(key);
  if (cached) {
    return JSON.parse(cached);
  }

  // Fetch and cache
  const data = await fetchFn();
  await redis.setex(key, CACHE_TTL, JSON.stringify(data));

  return data;
}

// Usage - reduces repeated API calls
const presentation = await getCachedOrFetch(
  `presentation:${id}`,
  () => gamma.presentations.get(id)
);
```

### Step 5: Batch Operations
```typescript
// Expensive: Individual operations
for (const item of items) {
  await gamma.presentations.create(item); // N API calls
}

// Cost-effective: Batch operation
await gamma.presentations.createBatch(items); // 1 API call

// Or queue for off-peak processing
await queue.addBulk(items.map(item => ({
  name: 'create-presentation',
  data: item,
  opts: { delay: calculateOffPeakDelay() },
})));
```

### Step 6: Cost Alerts and Budgets
```typescript
// Set up budget alerts
const budget = {
  monthly: 100, // $100/month
  current: 0,
  alertThresholds: [50, 75, 90, 100],
};

async function recordCost(operation: string, cost: number) {
  budget.current += cost;

  for (const threshold of budget.alertThresholds) {
    const percentage = (budget.current / budget.monthly) * 100;
    if (percentage >= threshold) {
      await sendBudgetAlert(threshold, budget.current);
    }
  }

  if (budget.current >= budget.monthly) {
    await disableNonCriticalFeatures();
  }
}
```