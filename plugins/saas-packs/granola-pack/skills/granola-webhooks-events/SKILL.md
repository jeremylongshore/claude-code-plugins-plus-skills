---
name: granola-webhooks-events
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Handle granola webhook events and build event-driven automations. use
  when building custom integrations, processing meeting events, or creating real-time
  notification systems. trigger with phrases like "granola webhooks", "granola events",
  "granol...
---
# Granola Webhooks & Events

## Overview
Build event-driven automations using Granola's Zapier webhooks and event triggers.

## Prerequisites
- Granola Pro or Business plan
- Zapier account
- Webhook endpoint (or Zapier as processor)
- Understanding of event-driven architecture

## Available Events

### Granola Zapier Triggers
| Event | Description | Payload |
|-------|-------------|---------|
| New Note Created | Meeting ended, notes ready | Full note data |
| Note Updated | Notes manually edited | Updated content |
| Note Shared | Notes shared with others | Share details |

## Event Payloads

### New Note Created
```json
{
  "event_type": "note.created",
  "timestamp": "2025-01-06T14:30:00Z",
  "data": {
    "note_id": "note_abc123",
    "meeting_title": "Sprint Planning",
    "meeting_date": "2025-01-06",
    "start_time": "2025-01-06T14:00:00Z",
    "end_time": "2025-01-06T14:30:00Z",
    "duration_minutes": 30,
    "attendees": [
      {
        "name": "Sarah Chen",
        "email": "sarah@company.com"
      }
    ],
    "summary": "Discussed Q1 priorities...",
    "action_items": [
      {
        "text": "Review PRs",
        "assignee": "@mike",
        "due_date": "2025-01-08"
      }
    ],
    "key_points": [
      "Agreed on feature freeze date",
      "Sprint velocity improving"
    ],
    "transcript_available": true,
    "granola_url": "https://app.granola.ai/notes/note_abc123"
  }
}
```

### Note Updated
```json
{
  "event_type": "note.updated",
  "timestamp": "2025-01-06T15:00:00Z",
  "data": {
    "note_id": "note_abc123",
    "changes": {
      "summary": {
        "old": "Discussed Q1 priorities...",
        "new": "Finalized Q1 priorities..."
      },
      "action_items": {
        "added": [{"text": "New action", "assignee": "@alex"}],
        "removed": []
      }
    },
    "updated_by": "user@company.com"
  }
}
```

## Webhook Processing

### Zapier Webhook Receiver
```yaml
# Create Catch Hook in Zapier
Trigger: Webhooks by Zapier
Event: Catch Hook
URL: https://hooks.zapier.com/hooks/catch/YOUR_HOOK_ID/

# Configure in Granola (via Zapier integration)
Granola → Zapier → Your Webhook
```

### Custom Webhook Endpoint
```javascript
// Express.js webhook handler
const express = require('express');
const app = express();

app.use(express.json());

app.post('/webhook/granola', (req, res) => {
  const event = req.body;

  console.log(`Received event: ${event.event_type}`);

  switch (event.event_type) {
    case 'note.created':
      handleNewNote(event.data);
      break;
    case 'note.updated':
      handleNoteUpdate(event.data);
      break;
    default:
      console.log('Unknown event type');
  }

  res.status(200).json({ received: true });
});

async function handleNewNote(data) {
  // Process new meeting notes
  console.log(`New note: ${data.meeting_title}`);

  // Extract action items
  for (const action of data.action_items) {
    await createTask(action);
  }

  // Send notification
  await notifyTeam(data);
}

app.listen(3000);
```

### Python Webhook Handler
```python
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/webhook/granola', methods=['POST'])
def granola_webhook():
    event = request.json

    event_type = event.get('event_type')
    data = event.get('data')

    if event_type == 'note.created':
        process_new_note(data)
    elif event_type == 'note.updated':
        process_note_update(data)

    return jsonify({'status': 'ok'}), 200

def process_new_note(data):
    print(f"Processing: {data['meeting_title']}")

    # Create issues for action items
    for action in data.get('action_items', []):
        create_github_issue(action)

    # Post to Slack
    post_to_slack(data)

if __name__ == '__main__':
    app.run(port=3000)
```

## Event Filtering

### Zapier Filters
```yaml
# Filter by meeting type
Filter Step:
  Condition:
    meeting_title contains "sprint"
    OR meeting_title contains "planning"
    OR attendees count > 3
  Action: Continue

# Filter by content
Filter Step:
  Condition:
    summary contains "decision"
    OR action_items exists
  Action: Continue
```

### Code-Based Filtering
```javascript
// Zapier Code Step
const data = inputData;

// Only process if has action items
if (!data.action_items || data.action_items.length === 0) {
  return { skip: true };
}

// Only process external meetings
const externalDomains = ['client.com', 'partner.org'];
const hasExternal = data.attendees.some(a =>
  externalDomains.some(d => a.email.includes(d))
);

if (!hasExternal) {
  return { skip: true };
}

return { process: true, ...data };
```

## Real-Time Processing Patterns

### Pattern 1: Immediate Notification
```yaml
Event Flow:
  Meeting Ends (T+0)
       ↓
  Notes Ready (T+2 min)
       ↓
  Webhook Fires (T+2.1 min)
       ↓
  Slack Notification (T+2.2 min)

Total Latency: ~2-3 minutes
```

### Pattern 2: Batch Processing
```yaml
Event Flow:
  Notes Created → Queue
       ↓
  Every 15 minutes:
    - Aggregate notes
    - Generate digest
    - Send single notification

Use Case: Reduce notification noise
```

### Pattern 3: Conditional Routing
```yaml
Event Received:
  │
  ├── If external attendee → CRM Update
  │
  ├── If action items > 3 → Create Project
  │
  ├── If duration > 60 min → Request Summary
  │
  └── Default → Standard Processing
```

## Error Handling

### Retry Logic
```javascript
async function processWithRetry(data, maxRetries = 3) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      await processEvent(data);
      return { success: true };
    } catch (error) {
      console.error(`Attempt ${attempt} failed:`, error);

      if (attempt === maxRetries) {
        await notifyError(data, error);
        return { success: false, error };
      }

      // Exponential backoff
      await sleep(Math.pow(2, attempt) * 1000);
    }
  }
}
```

### Dead Letter Queue
```yaml
On Error:
  1. Log error details
  2. Store failed event in queue
  3. Alert ops team
  4. Retry after 1 hour
  5. If still failing, archive for manual review
```

## Monitoring & Observability

### Event Logging
```javascript
// Log all events for debugging
function logEvent(event) {
  const log = {
    timestamp: new Date().toISOString(),
    event_type: event.event_type,
    note_id: event.data.note_id,
    meeting_title: event.data.meeting_title,
    processing_time: Date.now()
  };

  console.log(JSON.stringify(log));
}
```

### Metrics to Track
| Metric | Description | Alert Threshold |
|--------|-------------|-----------------|
| Events/hour | Processing volume | > 100/hr |
| Latency | Time to process | > 30 seconds |
| Error rate | Failed events | > 5% |
| Queue depth | Pending events | > 50 |

## Resources
- [Zapier Webhooks](https://zapier.com/help/create/code-webhooks)
- [Webhook Best Practices](https://zapier.com/blog/webhook-best-practices)

## Next Steps
Proceed to `granola-performance-tuning` for optimization techniques.
