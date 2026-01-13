# Testing Webhooks

## Testing Webhooks

```typescript
// tests/webhooks/apollo.test.ts
import { describe, it, expect } from 'vitest';
import request from 'supertest';
import crypto from 'crypto';
import app from '../../src/app';

function signPayload(payload: any, secret: string): string {
  return crypto
    .createHmac('sha256', secret)
    .update(JSON.stringify(payload))
    .digest('hex');
}

describe('Apollo Webhooks', () => {
  const secret = 'test-webhook-secret';

  beforeAll(() => {
    process.env.APOLLO_WEBHOOK_SECRET = secret;
  });

  it('rejects requests without signature', async () => {
    const response = await request(app)
      .post('/webhooks/apollo')
      .send({ event: 'contact.created' });

    expect(response.status).toBe(401);
  });

  it('rejects requests with invalid signature', async () => {
    const response = await request(app)
      .post('/webhooks/apollo')
      .set('x-apollo-signature', 'invalid')
      .send({ event: 'contact.created' });

    expect(response.status).toBe(401);
  });

  it('processes contact.created event', async () => {
    const payload = {
      event: 'contact.created',
      timestamp: new Date().toISOString(),
      data: {
        contact: {
          id: 'test-123',
          email: 'test@example.com',
          name: 'Test User',
        },
      },
    };

    const signature = signPayload(payload, secret);

    const response = await request(app)
      .post('/webhooks/apollo')
      .set('x-apollo-signature', signature)
      .send(payload);

    expect(response.status).toBe(200);
    expect(response.body.received).toBe(true);
  });

  it('processes email.opened event', async () => {
    const payload = {
      event: 'email.opened',
      timestamp: new Date().toISOString(),
      data: {
        email_id: 'email-123',
        contact_id: 'contact-123',
        sequence_id: 'seq-123',
      },
    };

    const signature = signPayload(payload, secret);

    const response = await request(app)
      .post('/webhooks/apollo')
      .set('x-apollo-signature', signature)
      .send(payload);

    expect(response.status).toBe(200);
  });
});
```