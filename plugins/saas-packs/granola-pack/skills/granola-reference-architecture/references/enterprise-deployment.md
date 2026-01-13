# Enterprise Deployment

## Enterprise Deployment

### Multi-Workspace Architecture
```
Enterprise Granola Deployment
├── Corporate Workspace
│   ├── Executive Team
│   ├── Leadership
│   └── Board Meetings
├── Engineering Workspace
│   ├── Sprint Planning
│   ├── Tech Reviews
│   └── Team Syncs
├── Sales Workspace
│   ├── Client Calls
│   ├── Demos
│   └── QBRs
└── HR Workspace
    ├── Interviews
    ├── Reviews
    └── Training
```

### Access Control Matrix
| Workspace | Visibility | Sharing | SSO Group |
|-----------|------------|---------|-----------|
| Corporate | Private | Executive only | exec-team |
| Engineering | Team | Engineering + PM | engineering |
| Sales | Team + CRM | Sales + Success | sales |
| HR | Confidential | HR only | hr-team |

### Integration Per Workspace
```yaml
Corporate:
  - Notion (private database)
  - Slack (#exec-team private)
  - No CRM

Engineering:
  - Notion (engineering wiki)
  - Slack (#dev-meetings)
  - Linear (auto-tasks)
  - GitHub (PR references)

Sales:
  - Notion (sales playbook)
  - Slack (#sales-updates)
  - HubSpot (full sync)
  - Gong (call coaching)

HR:
  - Notion (confidential)
  - Slack (HR DMs only)
  - Greenhouse (if recruiting)
```