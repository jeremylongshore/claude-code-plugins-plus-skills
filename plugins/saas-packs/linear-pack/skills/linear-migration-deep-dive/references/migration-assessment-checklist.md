# Migration Assessment Checklist

## Migration Assessment Checklist

### Data Volume
- [ ] Count total issues: ____
- [ ] Count total projects: ____
- [ ] Count total users: ____
- [ ] Attachments size: ____ GB
- [ ] Custom fields count: ____

### Workflow Analysis
- [ ] Document current statuses/states
- [ ] Map status transitions
- [ ] Identify automation rules
- [ ] List integrations in use

### User Mapping
- [ ] Export user list from source
- [ ] Map to Linear users
- [ ] Plan for unmapped users

### Timeline
- [ ] Migration window: ____
- [ ] Parallel run period: ____
- [ ] Cutover date: ____
- [ ] Rollback deadline: ____
```

### Phase 2: Workflow Mapping

```typescript
// migration/workflow-mapping.ts

// Jira to Linear status mapping
const JIRA_STATUS_MAP: Record<string, string> = {
  "To Do": "Todo",
  "In Progress": "In Progress",
  "In Review": "In Review",
  "Done": "Done",
  "Closed": "Done",
  "Backlog": "Backlog",
  "Blocked": "In Progress", // Linear uses labels for blocked
};

// Jira to Linear priority mapping
const JIRA_PRIORITY_MAP: Record<string, number> = {
  "Highest": 1, // Urgent
  "High": 2,
  "Medium": 3,
  "Low": 4,
  "Lowest": 4,
};

// Jira to Linear issue type mapping
const JIRA_TYPE_MAP: Record<string, { labelName: string }> = {
  "Bug": { labelName: "Bug" },
  "Story": { labelName: "Feature" },
  "Task": { labelName: "Task" },
  "Epic": { labelName: "Epic" },
  "Subtask": { labelName: "Subtask" },
};

// Asana to Linear mapping
const ASANA_SECTION_MAP: Record<string, string> = {
  "To Do": "Todo",
  "Doing": "In Progress",
  "Review": "In Review",
  "Complete": "Done",
};
```