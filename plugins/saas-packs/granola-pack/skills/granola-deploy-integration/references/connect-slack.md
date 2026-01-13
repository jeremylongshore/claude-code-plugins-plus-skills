# Connect Slack

## Connect Slack

1. Granola Settings > Integrations > Slack
2. Click "Connect Slack"
3. Select workspace
4. Authorize permissions:
   - Post messages
   - Access channels
   - Read user info
5. Configure default channel
```

#### Configuration Options
| Setting | Options | Recommendation |
|---------|---------|----------------|
| Default channel | Any channel | #meeting-notes |
| Auto-post | On/Off | On for team meetings |
| Include summary | Yes/No | Yes |
| Include actions | Yes/No | Yes |
| Mention attendees | Yes/No | For important meetings |

#### Message Format
```
Meeting Notes: Sprint Planning
January 6, 2025 | 45 minutes | 5 attendees

Summary:
Discussed Q1 priorities. Agreed on feature freeze
date of Jan 15th. Will focus on bug fixes next sprint.

Action Items:
- @sarah: Schedule design review (due: Jan 8)
- @mike: Create deployment checklist (due: Jan 10)
- @team: Review OKRs by Friday

[View Full Notes in Granola]
```

### Notion Integration

#### Setup
```markdown