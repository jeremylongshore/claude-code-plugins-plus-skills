---
name: granola-reference-architecture
license: MIT
allowed-tools: Read, Write, Edit
description: Enterprise meeting workflow architecture with granola. use when designing
  enterprise deployments, planning integrations, or architecting meeting management
  systems. trigger with phrases like "granola architecture", "granola enterprise",
  "granola s...
---
# Granola Reference Architecture

## Overview
Enterprise reference architecture for meeting management using Granola as the core capture platform.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                      MEETING ECOSYSTEM                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐         │
│  │   Google    │    │   Zoom      │    │   Teams     │         │
│  │  Calendar   │    │             │    │             │         │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘         │
│         │                  │                  │                 │
│         └─────────────────┬┴─────────────────┘                 │
│                           │                                     │
│                    ┌──────▼──────┐                              │
│                    │   GRANOLA   │                              │
│                    │   (Core)    │                              │
│                    │             │                              │
│                    │ • Capture   │                              │
│                    │ • Transcribe│                              │
│                    │ • Summarize │                              │
│                    └──────┬──────┘                              │
│                           │                                     │
│                    ┌──────▼──────┐                              │
│                    │   ZAPIER    │                              │
│                    │ (Middleware)│                              │
│                    └──────┬──────┘                              │
│                           │                                     │
│    ┌──────────┬───────────┼───────────┬──────────┐             │
│    │          │           │           │          │             │
│    ▼          ▼           ▼           ▼          ▼             │
│ ┌──────┐ ┌───────┐ ┌─────────┐ ┌────────┐ ┌──────────┐        │
│ │Slack │ │Notion │ │HubSpot  │ │ Linear │ │Analytics │        │
│ │      │ │       │ │(CRM)    │ │(Tasks) │ │  (BI)    │        │
│ └──────┘ └───────┘ └─────────┘ └────────┘ └──────────┘        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Component Responsibilities

### Tier 1: Meeting Platforms
| Platform | Role | Integration |
|----------|------|-------------|
| Google Meet | Video conferencing | Calendar sync |
| Zoom | Video conferencing | Calendar sync |
| Microsoft Teams | Video conferencing | Outlook sync |

### Tier 2: Granola (Core)
| Function | Description |
|----------|-------------|
| Audio Capture | Local device recording |
| Transcription | Real-time speech-to-text |
| Summarization | AI-generated meeting notes |
| Template Engine | Structured note formats |

### Tier 3: Middleware (Zapier)
| Function | Description |
|----------|-------------|
| Event Routing | Direct notes to appropriate systems |
| Data Transform | Format notes for target systems |
| Filtering | Route based on meeting type |
| Orchestration | Multi-step workflows |

### Tier 4: Destination Systems
| System | Purpose | Data Flow |
|--------|---------|-----------|
| Slack | Notifications | Summary + actions |
| Notion | Documentation | Full notes |
| HubSpot | CRM | Contact updates |
| Linear | Tasks | Action items |
| Analytics | Insights | Metrics |

## Data Flow Patterns

### Pattern 1: Standard Meeting
```
Meeting Ends
     ↓
Granola Processes (2 min)
     ↓
Zapier Trigger
     ↓
┌────────────────────┐
│ Parallel Actions   │
├────────────────────┤
│ → Slack notify     │
│ → Notion archive   │
│ → Linear tasks     │
└────────────────────┘
```

### Pattern 2: Client Meeting
```
Meeting Ends (external attendee detected)
     ↓
Granola Processes
     ↓
Zapier Trigger + Filter
     ↓
┌────────────────────┐
│ CRM Path           │
├────────────────────┤
│ → HubSpot note     │
│ → Contact update   │
│ → Deal activity    │
│ → Follow-up task   │
└────────────────────┘
     +
┌────────────────────┐
│ Standard Path      │
├────────────────────┤
│ → Notion archive   │
│ → Slack notify     │
└────────────────────┘
```

### Pattern 3: Executive Meeting
```
Meeting Ends (VP+ attendee)
     ↓
Granola Processes
     ↓
Special Handling:
     ↓
┌────────────────────┐
│ High-Touch Path    │
├────────────────────┤
│ → Private Notion   │
│ → EA notification  │
│ → Action tracking  │
│ → No public Slack  │
└────────────────────┘
```

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

## Security Architecture

### Data Classification
| Data Type | Classification | Handling |
|-----------|---------------|----------|
| Transcripts | Confidential | Encrypted, access-controlled |
| Summaries | Internal | Team-shared |
| Action Items | Internal | Public within org |
| Attendee Names | PII | GDPR compliant |

### Encryption & Access
```
Data at Rest: AES-256
Data in Transit: TLS 1.3
Access Control: RBAC + SSO
Audit: Full logging enabled
Retention: Configurable per workspace
```

## Scalability Considerations

### Volume Planning
| Team Size | Meetings/Month | Storage/Year | Plan |
|-----------|---------------|--------------|------|
| 1-10 | 100-500 | 5-25 GB | Pro |
| 10-50 | 500-2500 | 25-125 GB | Business |
| 50-200 | 2500-10000 | 125-500 GB | Enterprise |
| 200+ | 10000+ | 500+ GB | Enterprise+ |

### Performance Budgets
| Metric | Target | Measurement |
|--------|--------|-------------|
| Note availability | < 3 min | Post-meeting |
| Integration latency | < 1 min | Zapier to destination |
| Search response | < 500 ms | Within Granola |
| Export time | < 30 sec | For any meeting |

## Disaster Recovery

### Backup Strategy
```markdown
Primary: Granola cloud storage
Secondary: Nightly export to company storage
Tertiary: Weekly archive to cold storage

Recovery Points:
- RPO: 24 hours (daily export)
- RTO: 4 hours (restore from export)
```

### Failover Procedures
```markdown
If Granola unavailable:
1. Manual notes during meeting
2. Record with backup tool
3. Transcribe post-meeting
4. Manual upload when restored
```

## Resources
- [Granola Enterprise](https://granola.ai/enterprise)
- [Security Whitepaper](https://granola.ai/security)
- [Architecture Guide](https://granola.ai/help/architecture)

## Next Steps
Proceed to `granola-multi-env-setup` for multi-environment configuration.
