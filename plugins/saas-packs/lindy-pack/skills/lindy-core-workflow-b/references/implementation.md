# Implementation Guide

### Step 1: Define Automation Spec
```typescript
interface AutomationSpec {
  agentId: string;
  trigger: 'schedule' | 'webhook' | 'email' | 'event';
  schedule?: string; // cron expression
  webhookPath?: string;
  emailTrigger?: string;
  eventType?: string;
}

const automationSpec: AutomationSpec = {
  agentId: 'agt_abc123',
  trigger: 'schedule',
  schedule: '0 9 * * *', // Daily at 9 AM
};
```

### Step 2: Create Scheduled Automation
```typescript
import { Lindy } from '@lindy-ai/sdk';

const lindy = new Lindy({ apiKey: process.env.LINDY_API_KEY });

async function createScheduledAutomation(spec: AutomationSpec) {
  const automation = await lindy.automations.create({
    agentId: spec.agentId,
    type: 'schedule',
    config: {
      cron: spec.schedule,
      timezone: 'America/New_York',
      input: 'Run daily morning tasks',
    },
  });

  console.log(`Created automation: ${automation.id}`);
  return automation;
}
```

### Step 3: Create Webhook Trigger
```typescript
async function createWebhookAutomation(agentId: string, path: string) {
  const automation = await lindy.automations.create({
    agentId,
    type: 'webhook',
    config: {
      path: path,
      method: 'POST',
      inputMapping: {
        input: '{{body.message}}',
        context: '{{body.context}}',
      },
    },
  });

  console.log(`Webhook URL: ${automation.webhookUrl}`);
  return automation;
}
```

### Step 4: Create Email Trigger
```typescript
async function createEmailAutomation(agentId: string, triggerEmail: string) {
  const automation = await lindy.automations.create({
    agentId,
    type: 'email',
    config: {
      triggerAddress: triggerEmail,
      inputMapping: {
        input: '{{email.body}}',
        sender: '{{email.from}}',
        subject: '{{email.subject}}',
      },
    },
  });

  console.log(`Forward emails to: ${automation.triggerEmail}`);
  return automation;
}
```