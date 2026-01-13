# Event Payloads

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