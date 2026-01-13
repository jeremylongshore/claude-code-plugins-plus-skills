# Component Responsibilities

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