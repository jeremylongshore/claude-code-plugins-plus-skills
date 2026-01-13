# Webhook Registration

## Webhook Registration

```typescript
// scripts/register-webhooks.ts
import { apollo } from '../src/lib/apollo/client';

interface WebhookConfig {
  url: string;
  events: string[];
  secret: string;
}

async function registerWebhook(config: WebhookConfig) {
  // Note: Apollo webhook registration is typically done through the UI
  // This is a placeholder for future API support
  console.log('Webhook registration:', config);

  // For now, provide instructions
  console.log(`
To register webhooks in Apollo:

1. Go to Apollo Settings > Integrations > Webhooks
2. Click "Add Webhook"
3. Enter URL: ${config.url}
4. Select events: ${config.events.join(', ')}
5. Copy the webhook secret and add to your environment:
   APOLLO_WEBHOOK_SECRET=<secret>
  `);
}

const webhookConfig: WebhookConfig = {
  url: `${process.env.APP_URL}/webhooks/apollo`,
  events: [
    'contact.created',
    'contact.updated',
    'sequence.started',
    'sequence.completed',
    'email.sent',
    'email.opened',
    'email.clicked',
    'email.replied',
    'email.bounced',
  ],
  secret: process.env.APOLLO_WEBHOOK_SECRET!,
};

registerWebhook(webhookConfig);
```