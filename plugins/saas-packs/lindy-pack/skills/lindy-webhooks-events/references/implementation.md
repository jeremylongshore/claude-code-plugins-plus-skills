# Implementation Guide

### Step 1: Register Webhook
```typescript
import { Lindy } from '@lindy-ai/sdk';

const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

async function registerWebhook() {
  const webhook = await lindy.webhooks.create({
    url: 'https://myapp.com/webhooks/lindy',
    events: [
      'agent.run.started',
      'agent.run.completed',
      'agent.run.failed',
      'automation.triggered',
    ],
    secret: process.env.WEBHOOK_SECRET,
  });

  console.log(`Webhook ID: ${webhook.id}`);
  return webhook;
}
```

### Step 2: Create Webhook Handler
```typescript
// routes/webhooks/lindy.ts
import express from 'express';
import crypto from 'crypto';

const router = express.Router();

function verifySignature(payload: string, signature: string, secret: string): boolean {
  const expected = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(`sha256=${expected}`)
  );
}

router.post('/lindy', express.raw({ type: 'application/json' }), (req, res) => {
  const signature = req.headers['x-lindy-signature'] as string;
  const payload = req.body.toString();

  // Verify signature
  if (!verifySignature(payload, signature, process.env.WEBHOOK_SECRET!)) {
    return res.status(401).send('Invalid signature');
  }

  const event = JSON.parse(payload);

  // Handle event
  switch (event.type) {
    case 'agent.run.completed':
      handleRunCompleted(event.data);
      break;
    case 'agent.run.failed':
      handleRunFailed(event.data);
      break;
    case 'automation.triggered':
      handleAutomationTriggered(event.data);
      break;
    default:
      console.log('Unhandled event:', event.type);
  }

  res.status(200).send('OK');
});

export default router;
```

### Step 3: Implement Event Handlers
```typescript
// handlers/lindy-events.ts

interface RunCompletedEvent {
  runId: string;
  agentId: string;
  input: string;
  output: string;
  duration: number;
}

interface RunFailedEvent {
  runId: string;
  agentId: string;
  error: string;
  errorCode: string;
}

async function handleRunCompleted(data: RunCompletedEvent) {
  console.log(`Run ${data.runId} completed in ${data.duration}ms`);

  // Store result
  await db.runs.create({
    runId: data.runId,
    agentId: data.agentId,
    output: data.output,
    status: 'completed',
  });

  // Trigger downstream actions
  await processResult(data);
}

async function handleRunFailed(data: RunFailedEvent) {
  console.error(`Run ${data.runId} failed: ${data.error}`);

  // Alert on failure
  await alerting.send({
    severity: 'high',
    message: `Lindy agent failed: ${data.errorCode}`,
    details: data,
  });

  // Retry if appropriate
  if (data.errorCode === 'TIMEOUT') {
    await retryRun(data.runId);
  }
}

async function handleAutomationTriggered(data: any) {
  console.log(`Automation ${data.automationId} triggered`);

  // Log automation trigger
  await db.automations.log({
    automationId: data.automationId,
    triggeredAt: new Date(),
    input: data.input,
  });
}
```

### Step 4: Test Webhooks
```typescript
// Test webhook delivery
async function testWebhook(webhookId: string) {
  const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

  const result = await lindy.webhooks.test(webhookId, {
    type: 'agent.run.completed',
    data: {
      runId: 'test_run_123',
      agentId: 'agt_test',
      output: 'Test output',
      duration: 1000,
    },
  });

  console.log('Test result:', result);
}
```