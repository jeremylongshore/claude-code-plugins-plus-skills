# Event Handler Pattern

## Event Handler Pattern

```typescript
type ReplitEventType = 'resource.created' | 'resource.updated' | 'resource.deleted';

interface ReplitEvent {
  id: string;
  type: ReplitEventType;
  data: Record<string, any>;
  created: string;
}

const eventHandlers: Record<ReplitEventType, (data: any) => Promise<void>> = {
  'resource.created': async (data) => { /* handle */ },
  'resource.updated': async (data) => { /* handle */ },
  'resource.deleted': async (data) => { /* handle */ }
};

async function handleReplitEvent(event: ReplitEvent): Promise<void> {
  const handler = eventHandlers[event.type];

  if (!handler) {
    console.log(`Unhandled event type: ${event.type}`);
    return;
  }

  try {
    await handler(event.data);
    console.log(`Processed ${event.type}: ${event.id}`);
  } catch (error) {
    console.error(`Failed to process ${event.type}: ${event.id}`, error);
    throw error; // Rethrow to trigger retry
  }
}
```