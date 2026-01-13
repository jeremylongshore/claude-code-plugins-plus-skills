# Multi-Integration Workflows

## Multi-Integration Workflows

### Complete Meeting Follow-up
```yaml
# Multi-step automation

1. Meeting ends in Granola
     ↓
2. Summary posted to Slack #team-channel
     ↓
3. Full notes created in Notion
     ↓
4. Action items created in Linear
     ↓
5. HubSpot contact updated (if external)
     ↓
6. Follow-up email drafted in Gmail
```

### Implementation
```yaml
Zapier Paths:
  Path A (Internal Meeting):
    → Slack notification
    → Notion page
    → Linear tasks

  Path B (Client Meeting):
    → Slack notification
    → Notion page
    → HubSpot note
    → Gmail draft

Filter:
  If attendees contain external domain → Path B
  Else → Path A
```