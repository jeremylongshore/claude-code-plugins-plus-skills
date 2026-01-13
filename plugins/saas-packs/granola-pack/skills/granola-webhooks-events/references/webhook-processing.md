# Webhook Processing

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