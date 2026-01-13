# Webhook Handler Implementation

## Webhook Handler Implementation

### Express Handler
```typescript
// src/routes/webhooks/apollo.ts
import { Router } from 'express';
import crypto from 'crypto';
import { z } from 'zod';

const router = Router();

// Webhook payload schemas
const ContactEventSchema = z.object({
  event: z.enum(['contact.created', 'contact.updated']),
  timestamp: z.string(),
  data: z.object({
    contact: z.object({
      id: z.string(),
      email: z.string().optional(),
      name: z.string().optional(),
      title: z.string().optional(),
      organization: z.object({
        name: z.string(),
      }).optional(),
    }),
    changes: z.record(z.any()).optional(),
  }),
});

const SequenceEventSchema = z.object({
  event: z.enum(['sequence.started', 'sequence.completed', 'sequence.paused']),
  timestamp: z.string(),
  data: z.object({
    sequence_id: z.string(),
    contact_id: z.string(),
    status: z.string().optional(),
  }),
});

const EmailEventSchema = z.object({
  event: z.enum(['email.sent', 'email.opened', 'email.clicked', 'email.replied', 'email.bounced']),
  timestamp: z.string(),
  data: z.object({
    email_id: z.string(),
    contact_id: z.string(),
    sequence_id: z.string().optional(),
    subject: z.string().optional(),
    link_url: z.string().optional(), // For click events
    bounce_reason: z.string().optional(), // For bounce events
  }),
});

// Verify webhook signature
function verifySignature(payload: string, signature: string, secret: string): boolean {
  const expectedSignature = crypto
    .createHmac('sha256', secret)
    .update(payload)
    .digest('hex');
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expectedSignature)
  );
}

// Middleware for signature verification
function verifyApolloWebhook(req: any, res: any, next: any) {
  const signature = req.headers['x-apollo-signature'];
  const webhookSecret = process.env.APOLLO_WEBHOOK_SECRET;

  if (!webhookSecret) {
    console.error('APOLLO_WEBHOOK_SECRET not configured');
    return res.status(500).json({ error: 'Webhook secret not configured' });
  }

  if (!signature) {
    return res.status(401).json({ error: 'Missing signature' });
  }

  const rawBody = JSON.stringify(req.body);
  if (!verifySignature(rawBody, signature, webhookSecret)) {
    return res.status(401).json({ error: 'Invalid signature' });
  }

  next();
}

// Main webhook endpoint
router.post('/apollo', verifyApolloWebhook, async (req, res) => {
  const { event } = req.body;

  try {
    // Route to appropriate handler
    if (event.startsWith('contact.')) {
      await handleContactEvent(ContactEventSchema.parse(req.body));
    } else if (event.startsWith('sequence.')) {
      await handleSequenceEvent(SequenceEventSchema.parse(req.body));
    } else if (event.startsWith('email.')) {
      await handleEmailEvent(EmailEventSchema.parse(req.body));
    } else {
      console.warn('Unknown event type:', event);
    }

    res.status(200).json({ received: true });
  } catch (error: any) {
    console.error('Webhook processing error:', error);
    res.status(400).json({ error: error.message });
  }
});

export default router;
```

### Event Handlers
```typescript
// src/services/webhooks/handlers.ts
import { prisma } from '../db';
import { publishEvent } from '../events';

export async function handleContactEvent(payload: any) {
  const { event, data } = payload;

  switch (event) {
    case 'contact.created':
      // Sync new contact to local database
      await prisma.contact.upsert({
        where: { apolloId: data.contact.id },
        create: {
          apolloId: data.contact.id,
          email: data.contact.email,
          name: data.contact.name,
          title: data.contact.title,
          company: data.contact.organization?.name,
          syncedAt: new Date(),
        },
        update: {
          email: data.contact.email,
          name: data.contact.name,
          title: data.contact.title,
          company: data.contact.organization?.name,
          syncedAt: new Date(),
        },
      });

      await publishEvent('apollo.contact.synced', {
        contactId: data.contact.id,
        action: 'created',
      });
      break;

    case 'contact.updated':
      await prisma.contact.update({
        where: { apolloId: data.contact.id },
        data: {
          ...data.changes,
          syncedAt: new Date(),
        },
      });

      await publishEvent('apollo.contact.synced', {
        contactId: data.contact.id,
        action: 'updated',
        changes: data.changes,
      });
      break;
  }
}

export async function handleSequenceEvent(payload: any) {
  const { event, data } = payload;

  switch (event) {
    case 'sequence.started':
      await prisma.sequenceEnrollment.create({
        data: {
          apolloContactId: data.contact_id,
          apolloSequenceId: data.sequence_id,
          status: 'active',
          startedAt: new Date(),
        },
      });
      break;

    case 'sequence.completed':
      await prisma.sequenceEnrollment.update({
        where: {
          apolloContactId_apolloSequenceId: {
            apolloContactId: data.contact_id,
            apolloSequenceId: data.sequence_id,
          },
        },
        data: {
          status: data.status || 'completed',
          completedAt: new Date(),
        },
      });
      break;
  }
}

export async function handleEmailEvent(payload: any) {
  const { event, data, timestamp } = payload;

  // Record email engagement
  await prisma.emailEngagement.create({
    data: {
      apolloEmailId: data.email_id,
      apolloContactId: data.contact_id,
      apolloSequenceId: data.sequence_id,
      eventType: event.replace('email.', ''),
      eventData: {
        subject: data.subject,
        linkUrl: data.link_url,
        bounceReason: data.bounce_reason,
      },
      occurredAt: new Date(timestamp),
    },
  });

  // Handle specific events
  if (event === 'email.replied') {
    // Notify sales team
    await publishEvent('apollo.lead.engaged', {
      contactId: data.contact_id,
      type: 'reply',
    });
  } else if (event === 'email.bounced') {
    // Mark contact as bounced
    await prisma.contact.update({
      where: { apolloId: data.contact_id },
      data: { emailStatus: 'bounced' },
    });
  }
}
```