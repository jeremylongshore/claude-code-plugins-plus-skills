# Event Filtering

## Event Filtering

### Zapier Filters
```yaml
# Filter by meeting type
Filter Step:
  Condition:
    meeting_title contains "sprint"
    OR meeting_title contains "planning"
    OR attendees count > 3
  Action: Continue

# Filter by content
Filter Step:
  Condition:
    summary contains "decision"
    OR action_items exists
  Action: Continue
```

### Code-Based Filtering
```javascript
// Zapier Code Step
const data = inputData;

// Only process if has action items
if (!data.action_items || data.action_items.length === 0) {
  return { skip: true };
}

// Only process external meetings
const externalDomains = ['client.com', 'partner.org'];
const hasExternal = data.attendees.some(a =>
  externalDomains.some(d => a.email.includes(d))
);

if (!hasExternal) {
  return { skip: true };
}

return { process: true, ...data };
```