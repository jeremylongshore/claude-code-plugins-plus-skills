# Event Handler Pattern

## Event Handler Pattern

```typescript
type ClayEventType = 'resource.created' | 'resource.updated' | 'resource.deleted';

interface ClayEvent {
  id: string;
  type: ClayEventType;
  data: Record<string, any>;
  created: string;
}

const eventHandlers: Record<ClayEventType, (data: any) => Promise<void>> = {
  'resource.created': async (data) => { /* handle */ },
  'resource.updated': async (data) => { /* handle */ },
  'resource.deleted': async (data) => { /* handle */ }
};

async function handleClayEvent(event: ClayEvent): Promise<void> {
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