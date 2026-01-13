# Common Integration Patterns

## Common Integration Patterns

### Pattern 1: Notes to Notion
```yaml
Trigger: New Granola Note
Action: Create Notion Page

Configuration:
  Notion Database: Meeting Notes
  Title: {{meeting_title}}
  Date: {{meeting_date}}
  Content: {{note_content}}
  Participants: {{attendees}}
```

### Pattern 2: Action Items to Linear
```yaml
Trigger: New Granola Note
Filter: Contains "Action Item" or "TODO"
Action: Create Linear Issue

Configuration:
  Team: Engineering
  Title: "Meeting Action: {{action_text}}"
  Description: "From meeting: {{meeting_title}}"
  Assignee: {{extracted_assignee}}
```

### Pattern 3: Summary to Slack
```yaml
Trigger: New Granola Note
Action: Post to Slack Channel

Configuration:
  Channel: #team-updates
  Message: |
    :notepad_spiral: Meeting Notes: {{meeting_title}}

    **Summary:** {{summary}}

    **Action Items:**
    {{action_items}}

    Full notes: {{granola_link}}
```

### Pattern 4: CRM Update (HubSpot)
```yaml
Trigger: New Granola Note
Filter: Meeting contains client name
Action: Update HubSpot Contact

Configuration:
  Contact: {{client_email}}
  Note: "Meeting on {{date}}: {{summary}}"
  Last Contact: {{meeting_date}}
```