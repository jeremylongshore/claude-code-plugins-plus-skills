# Examples

### Multi-Trigger Setup
```typescript
async function setupAutomations(agentId: string) {
  // Daily summary at 9 AM
  await lindy.automations.create({
    agentId,
    type: 'schedule',
    config: { cron: '0 9 * * *', input: 'Generate daily summary' },
  });

  // Webhook for external events
  await lindy.automations.create({
    agentId,
    type: 'webhook',
    config: { path: '/events', method: 'POST' },
  });

  // Email trigger for support
  await lindy.automations.create({
    agentId,
    type: 'email',
    config: { triggerAddress: 'support@mycompany.com' },
  });
}
```