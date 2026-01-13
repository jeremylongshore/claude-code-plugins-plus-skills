# Multi-Step Workflow Example

## Multi-Step Workflow Example

```yaml
Name: Complete Meeting Follow-up

Step 1 - Trigger:
  App: Granola
  Event: New Note Created

Step 2 - Action:
  App: OpenAI
  Event: Generate Follow-up Email
  Prompt: "Write a follow-up email for: {{summary}}"

Step 3 - Action:
  App: Gmail
  Event: Create Draft
  To: {{attendees}}
  Subject: "Follow-up: {{meeting_title}}"
  Body: {{openai_response}}

Step 4 - Action:
  App: Notion
  Event: Create Page
  Content: {{full_notes}}

Step 5 - Action:
  App: Slack
  Event: Send Message
  Message: "Follow-up draft ready for {{meeting_title}}"
```