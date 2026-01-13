# Zapier Integrations

## Zapier Integrations

### Popular Zapier Recipes

#### Granola → Google Docs
```yaml
Trigger: New Granola Note
Action: Create Google Doc

Configuration:
  Folder: Team Meeting Notes
  Title: "{{meeting_title}} - {{date}}"
  Content: |
    # {{meeting_title}}

    **Date:** {{date}}
    **Attendees:** {{attendees}}

    ## Summary
    {{summary}}

    ## Action Items
    {{action_items}}
```

#### Granola → Asana
```yaml
Trigger: New Granola Note
Filter: Contains action items
Action: Create Asana Task

Configuration:
  Project: Meeting Actions
  Name: "Action from {{meeting_title}}"
  Notes: "{{action_text}}\n\nFrom meeting: {{meeting_title}}"
  Assignee: Dynamic from parsed @mention
  Due Date: Parsed from note content
```

#### Granola → Airtable
```yaml
Trigger: New Granola Note
Action: Create Airtable Record

Configuration:
  Base: Meeting Archive
  Table: Notes
  Fields:
    Title: {{meeting_title}}
    Date: {{date}}
    Summary: {{summary}}
    Action Count: {{action_item_count}}
    Status: Active
    Link: {{granola_url}}
```