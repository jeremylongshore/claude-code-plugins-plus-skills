# Zapier Webhook Setup

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