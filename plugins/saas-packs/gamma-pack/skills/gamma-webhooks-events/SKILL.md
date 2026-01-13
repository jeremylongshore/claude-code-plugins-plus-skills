---
name: gamma-webhooks-events
license: MIT
allowed-tools: Read, Write, Edit
description: Handle gamma webhooks and events for real-time updates. use when implementing
  webhook receivers, processing events, or building real-time gamma integrations.
  trigger with phrases like "gamma webhooks", "gamma events", "gamma notifications",
  "gamma...
---
# Gamma Webhooks & Events

## Overview
Implement webhook handlers and event processing for real-time Gamma updates.

## Prerequisites
- Public endpoint for webhook delivery
- Webhook secret from Gamma dashboard
- Understanding of event-driven architecture

## Instructions

### Step 1: Register Webhook Endpoint
```typescript
// Register via API
const webhook = await gamma.webhooks.create({
  url: 'https://your-app.com/webhooks/gamma',
  events: [
    'presentation.created',
    'presentation.updated',
    'presentation.exported',
    'presentation.deleted',
  ],
  secret: process.env.GAMMA_WEBHOOK_SECRET,
});

console.log('Webhook registered:', webhook.id);
```

### Step 2: Create Webhook Handler
```typescript
// routes/webhooks/gamma.ts
import express from 'express';
import crypto from 'crypto';

const router = express.Router();

// Verify webhook signature
function verifySignature(payload: string, signature: string): boolean {
  const secret = process.env.GAMMA_WEBHOOK_SECRET!;
  const expected = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');

  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(`sha256=${expected}`)
  );
}

router.post('/gamma',
  express.raw({ type: 'application/json' }),
  async (req, res) => {
    const signature = req.headers['x-gamma-signature'] as string;
    const payload = req.body.toString();

    // Verify signature
    if (!verifySignature(payload, signature)) {
      return res.status(401).json({ error: 'Invalid signature' });
    }

    // Parse event
    const event = JSON.parse(payload);

    // Acknowledge receipt quickly
    res.status(200).json({ received: true });

    // Process event async
    await processEvent(event);
  }
);

export default router;
```

### Step 3: Event Processing
```typescript
// services/gamma-events.ts
interface GammaEvent {
  id: string;
  type: string;
  data: any;
  timestamp: string;
}

type EventHandler = (data: any) => Promise<void>;

const handlers: Record<string, EventHandler> = {
  'presentation.created': async (data) => {
    console.log('New presentation:', data.id);
    await notifyTeam(`New presentation created: ${data.title}`);
    await updateDatabase({ presentationId: data.id, status: 'created' });
  },

  'presentation.updated': async (data) => {
    console.log('Presentation updated:', data.id);
    await updateDatabase({ presentationId: data.id, status: 'updated' });
  },

  'presentation.exported': async (data) => {
    console.log('Export complete:', data.exportUrl);
    await sendExportNotification(data.userId, data.exportUrl);
  },

  'presentation.deleted': async (data) => {
    console.log('Presentation deleted:', data.id);
    await cleanupAssets(data.id);
  },
};

export async function processEvent(event: GammaEvent) {
  const handler = handlers[event.type];

  if (!handler) {
    console.warn('Unhandled event type:', event.type);
    return;
  }

  try {
    await handler(event.data);
    await recordEventProcessed(event.id);
  } catch (err) {
    console.error('Event processing failed:', err);
    await recordEventFailed(event.id, err);
  }
}
```

### Step 4: Event Queue for Reliability
```typescript
// services/event-queue.ts
import Bull from 'bull';

const eventQueue = new Bull('gamma-events', {
  redis: process.env.REDIS_URL,
});

// Add to queue instead of processing directly
export async function queueEvent(event: GammaEvent) {
  await eventQueue.add(event, {
    attempts: 3,
    backoff: {
      type: 'exponential',
      delay: 5000,
    },
  });
}

// Process queue
eventQueue.process(async (job) => {
  await processEvent(job.data);
});

eventQueue.on('failed', (job, err) => {
  console.error(`Event ${job.id} failed:`, err.message);
  // Send to dead letter queue or alert
});
```

### Step 5: Webhook Management
```typescript
// List webhooks
const webhooks = await gamma.webhooks.list();

// Update webhook
await gamma.webhooks.update(webhookId, {
  events: ['presentation.created', 'presentation.exported'],
});

// Delete webhook
await gamma.webhooks.delete(webhookId);

// Test webhook
await gamma.webhooks.test(webhookId);
```

## Event Types Reference

| Event | Description | Payload |
|-------|-------------|---------|
| `presentation.created` | New presentation | id, title, userId |
| `presentation.updated` | Slides modified | id, changes[] |
| `presentation.exported` | Export completed | id, format, url |
| `presentation.deleted` | Presentation removed | id |
| `presentation.shared` | Sharing updated | id, shareSettings |

## Output
- Verified webhook handler
- Event processing pipeline
- Reliable queue system
- Webhook management API

## Error Handling
| Error | Cause | Solution |
|-------|-------|----------|
| Invalid signature | Secret mismatch | Verify webhook secret |
| Timeout | Slow processing | Use async queue |
| Duplicate events | Retry delivery | Implement idempotency |
| Missing events | Endpoint down | Use reliable hosting |

## Resources
- [Gamma Webhooks Guide](https://gamma.app/docs/webhooks)
- [Webhook Best Practices](https://gamma.app/docs/webhooks-best-practices)

## Next Steps
Proceed to `gamma-performance-tuning` for optimization.
