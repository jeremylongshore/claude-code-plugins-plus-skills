---
name: granola-ci-integration
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Configure Granola CI/CD integration with automated workflows. Use when
  setting up automated meeting note processing, integrating with development pipelines,
  or building Zapier automations. Trigger with phrases like "granola CI", "granola
  automatio...
---
# Granola CI Integration

## Overview
Build automated workflows that process Granola meeting notes as part of your development pipeline.

## Prerequisites
- Granola Pro or Business plan
- Zapier account
- GitHub repository (for Actions)
- Development workflow understanding

## Architecture

### Meeting-to-Action Pipeline
```
Meeting Ends
     ↓
Granola Processes Notes
     ↓
Zapier Webhook Triggered
     ↓
Processing Pipeline
     ├── Create Issues/Tasks
     ├── Update Documentation
     ├── Notify Team
     └── Update CRM
```

## Zapier Webhook Setup

### Step 1: Create Webhook Endpoint
```yaml
# Create a Zapier Zap
Trigger: Granola - New Note Created
Filter: Meeting title contains "sprint" OR "planning"
```

### Step 2: Parse Meeting Content
```javascript
// Zapier Code Step - Parse Action Items
const noteContent = inputData.note_content;

// Extract action items
const actionPattern = /- \[ \] (.+?)(?:\(@(\w+)\))?/g;
const actions = [];
let match;

while ((match = actionPattern.exec(noteContent)) !== null) {
  actions.push({
    task: match[1].trim(),
    assignee: match[2] || 'unassigned'
  });
}

return { actions: JSON.stringify(actions) };
```

### Step 3: Create GitHub Issues
```yaml
Action: GitHub - Create Issue
Repository: your-org/your-repo
Title: "Meeting Action: {{task}}"
Body: |
  From meeting: {{meeting_title}}
  Date: {{meeting_date}}

  Task: {{task}}
  Assignee: {{assignee}}

  ---
  Auto-created by Granola integration
Labels: ["from-meeting", "action-item"]
Assignee: {{assignee}}
```

## GitHub Actions Integration

### Workflow: Process Meeting Notes
```yaml
# .github/workflows/process-meeting-notes.yml
name: Process Meeting Notes

on:
  repository_dispatch:
    types: [granola-meeting-completed]

jobs:
  process-notes:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Parse Meeting Notes
        id: parse
        run: |
          echo "Processing meeting: ${{ github.event.client_payload.title }}"
          echo "Date: ${{ github.event.client_payload.date }}"

      - name: Update Meeting Log
        run: |
          # Append to meetings log
          echo "| ${{ github.event.client_payload.date }} | ${{ github.event.client_payload.title }} | [Link](${{ github.event.client_payload.url }}) |" >> docs/meetings.md

      - name: Create Issue for Action Items
        uses: actions/github-script@v7
        with:
          script: |
            const actions = JSON.parse('${{ github.event.client_payload.action_items }}');

            for (const action of actions) {
              await github.rest.issues.create({
                owner: context.repo.owner,
                repo: context.repo.repo,
                title: `Meeting Action: ${action.task}`,
                body: `From: ${{ github.event.client_payload.title }}\n\n${action.task}`,
                labels: ['meeting-action']
              });
            }

      - name: Commit Changes
        run: |
          git config user.name "Granola Bot"
          git config user.email "bot@granola.ai"
          git add docs/meetings.md
          git commit -m "docs: add meeting notes from ${{ github.event.client_payload.date }}"
          git push
```

### Trigger Workflow from Zapier
```yaml
# Zapier Webhook Action
Method: POST
URL: https://api.github.com/repos/your-org/your-repo/dispatches
Headers:
  Authorization: Bearer {{github_token}}
  Accept: application/vnd.github.v3+json
Body:
  {
    "event_type": "granola-meeting-completed",
    "client_payload": {
      "title": "{{meeting_title}}",
      "date": "{{meeting_date}}",
      "url": "{{granola_link}}",
      "summary": "{{summary}}",
      "action_items": {{action_items_json}}
    }
  }
```

## Linear Integration Pipeline

### Auto-Create Tasks from Meetings
```yaml
# Zapier Multi-Step Workflow
Step 1 - Trigger:
  App: Granola
  Event: New Note Created

Step 2 - Filter:
  Condition: Summary contains "TODO" or "action item"

Step 3 - Parse:
  App: Code by Zapier
  Script: Extract action items with assignees

Step 4 - Loop:
  For each action item:
    App: Linear
    Action: Create Issue
    Team: Engineering
    Title: {{action.task}}
    Description: |
      From meeting: {{meeting_title}}
      Date: {{meeting_date}}

      Context: {{surrounding_text}}
    Assignee: {{action.assignee}}
    State: Todo
```

## Slack Bot Integration

### Meeting Summary Bot
```yaml
# Automated Slack Post
Trigger: New Granola Note

Slack Message:
  Channel: #dev-meetings
  Blocks:
    - type: header
      text: "Meeting Notes: {{meeting_title}}"
    - type: section
      text: "{{summary}}"
    - type: divider
    - type: section
      text: "*Action Items:*\n{{action_items}}"
    - type: actions
      elements:
        - type: button
          text: "View Full Notes"
          url: "{{granola_link}}"
        - type: button
          text: "Create Tasks"
          action_id: "create_tasks"
```

## Testing & Validation

### Test Webhook Endpoint
```bash
# Test Zapier webhook with sample data
curl -X POST https://hooks.zapier.com/hooks/catch/YOUR_HOOK_ID \
  -H "Content-Type: application/json" \
  -d '{
    "meeting_title": "Test Sprint Planning",
    "meeting_date": "2025-01-06",
    "summary": "Discussed Q1 priorities",
    "action_items": [
      {"task": "Review PRs", "assignee": "mike"},
      {"task": "Update docs", "assignee": "sarah"}
    ]
  }'
```

### Validate Integration
```markdown
## Integration Test Checklist
- [ ] Schedule test meeting
- [ ] Complete meeting with sample action items
- [ ] Verify Zapier trigger fires
- [ ] Check GitHub issues created
- [ ] Confirm Slack notification sent
- [ ] Validate Linear tasks appear
```

## Error Handling

### Retry Configuration
```yaml
# Zapier Error Handling
On Error:
  Retry: 3 times
  Delay: 5 minutes between retries
  Fallback: Send error to Slack #ops-alerts
```

### Common Errors
| Error | Cause | Solution |
|-------|-------|----------|
| Webhook timeout | Large payload | Add processing delay |
| Auth expired | Token invalid | Refresh OAuth tokens |
| Rate limited | Too many requests | Add delays between actions |
| Parse failed | Note format changed | Update parsing logic |

## Resources
- [Zapier Webhooks](https://zapier.com/help/create/code-webhooks)
- [GitHub Actions Events](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)

## Next Steps
Proceed to `granola-deploy-integration` for native app integrations.
