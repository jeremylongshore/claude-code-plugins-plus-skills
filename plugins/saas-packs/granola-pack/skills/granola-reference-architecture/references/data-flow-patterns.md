# Data Flow Patterns

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