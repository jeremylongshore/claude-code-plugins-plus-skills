# Event Handler Pattern

## Event Handler Pattern

```typescript
type Vast.aiEventType = 'resource.created' | 'resource.updated' | 'resource.deleted';

interface Vast.aiEvent {
  id: string;
  type: Vast.aiEventType;
  data: Record<string, any>;
  created: string;
}

const eventHandlers: Record<Vast.aiEventType, (data: any) => Promise<void>> = {
  'resource.created': async (data) => { /* handle */ },
  'resource.updated': async (data) => { /* handle */ },
  'resource.deleted': async (data) => { /* handle */ }
};

async function handleVast.aiEvent(event: Vast.aiEvent): Promise<void> {
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