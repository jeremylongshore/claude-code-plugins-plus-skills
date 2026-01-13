# Fireflies Export

## Fireflies Export

1. Log into Fireflies.ai
2. Go to Meetings
3. Select meetings (checkbox)
4. Click "Export"
5. Choose format: JSON (recommended)
6. Download

API Export (Enterprise):
```bash
curl -X GET "https://api.fireflies.ai/v1/transcripts" \
  -H "Authorization: Bearer $FIREFLIES_API_KEY" \
  -o fireflies_export.json
```

#### Data Mapping
```yaml
# Fireflies → Granola Mapping

Fireflies Field:      Granola Field:
title             → meeting_title
date              → meeting_date
transcript        → transcript
summary           → summary
action_items      → action_items
participants      → attendees
```

### From Fathom

#### Export Process
```markdown