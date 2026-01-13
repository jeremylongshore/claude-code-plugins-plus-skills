# Workspace Creation

## Workspace Creation

1. Organization Settings > Workspaces
2. Click "Create Workspace"
3. Configure:
   - Name: Engineering
   - Slug: engineering
   - Description: Engineering team meetings
   - Owner: eng-lead@company.com
4. Save and proceed to settings
```

### Step 3: Configure Per-Workspace Settings
```yaml
# Engineering Workspace Settings
Workspace: Engineering

Privacy:
  default_sharing: team
  external_sharing: disabled
  transcript_access: members_only

Integrations:
  - Slack: #dev-meetings channel
  - Linear: Auto-create tasks
  - Notion: Engineering wiki database
  - GitHub: Link PRs in notes

Templates:
  - Sprint Planning
  - Code Review
  - Tech Design
  - 1:1 Engineering

Retention:
  notes: 1 year
  transcripts: 90 days
  audio: 7 days

Permissions:
  - Admins: Full access
  - Members: Create, edit own
  - Viewers: Read only (for PMs)
```