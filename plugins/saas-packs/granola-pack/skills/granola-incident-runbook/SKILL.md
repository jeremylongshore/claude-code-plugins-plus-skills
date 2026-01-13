---
name: granola-incident-runbook
description: |
  Incident response procedures for Granola meeting capture issues.
  Use when handling meeting capture failures, system outages,
  or urgent troubleshooting situations.
  Trigger with phrases like "granola incident", "granola outage",
  "granola emergency", "granola not recording", "granola down".
allowed-tools: Read, Write, Edit, Bash
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Granola Incident Runbook

## Overview
Standard operating procedures for responding to Granola incidents and meeting capture failures.

## Incident Severity Levels

| Level | Description | Response Time | Examples |
|-------|-------------|---------------|----------|
| P1 | Critical | < 15 min | Complete outage, data loss |
| P2 | High | < 1 hour | Recording failures, sync issues |
| P3 | Medium | < 4 hours | Single user issues, slow processing |
| P4 | Low | < 24 hours | UI bugs, minor inconveniences |

## Incident Response Flow

```
Incident Detected
       ↓
Assess Severity (5 min)
       ↓
Check Status Page (1 min)
       ↓
┌──────────────────────┐
│ Granola Issue?       │
├──────────────────────┤
│ Yes → Workaround     │
│ No  → Local Debug    │
└──────────────────────┘
       ↓
Communicate Status
       ↓
Track to Resolution
       ↓
Post-Incident Review
```

## Quick Status Check

### Step 1: Check Granola Status
```bash
# Check status page
curl -s https://status.granola.ai/api/v2/status.json | jq '.status'

# Or visit: https://status.granola.ai
```

### Step 2: Test Local Connectivity
```bash
# Test API connectivity
curl -I https://api.granola.ai/health

# Expected: HTTP 200 OK
```

### Step 3: Check Local App Status
```bash
# macOS - Check if Granola is running
pgrep -l Granola

# Check Granola logs
tail -f ~/Library/Logs/Granola/granola.log
```

## Incident: Recording Not Starting

### Symptoms
- Meeting starts but Granola doesn't record
- No recording indicator visible
- Calendar event not detected

### Immediate Actions
```markdown
## Quick Fix (< 5 min)

1. [ ] Manually click "Start Recording" in Granola
2. [ ] Check calendar is connected (Settings > Integrations)
3. [ ] Verify meeting is on synced calendar
4. [ ] Restart Granola app
5. [ ] Check audio permissions granted
```

### Root Cause Investigation
```markdown
## Investigate (if quick fix fails)

1. Calendar Sync Issue:
   - Last sync time?
   - OAuth token valid?
   - Correct calendar selected?

2. Audio Permission:
   - System Preferences > Security > Microphone
   - Is Granola listed and checked?

3. App State:
   - Force quit and restart
   - Clear cache if needed
   - Check for updates
```

## Incident: No Audio Captured

### Symptoms
- Recording indicator shows
- Transcript is empty or says "No audio"
- Notes are blank

### Immediate Actions
```markdown
## Quick Fix

1. [ ] Check audio input device in System Preferences
2. [ ] Verify physical mic is not muted
3. [ ] Test mic with other app (Voice Memos)
4. [ ] Restart Granola app
5. [ ] Rejoin meeting if possible
```

### Workaround
```markdown
## If Audio Cannot Be Captured

1. Take manual notes during meeting
2. Record with backup tool (QuickTime, OBS)
3. Upload/transcribe after meeting
4. Document for post-incident review
```

## Incident: Processing Stuck

### Symptoms
- Meeting ended but notes not appearing
- Processing indicator spinning > 10 min
- Error message about processing

### Immediate Actions
```markdown
## Quick Fix

1. [ ] Wait up to 15 minutes (large meetings take longer)
2. [ ] Check internet connectivity
3. [ ] Check Granola status page for delays
4. [ ] Restart Granola app
5. [ ] Contact support if > 20 min
```

### Support Escalation
```markdown
## Contact Support

Email: help@granola.ai

Include:
- Meeting date/time
- Meeting ID (if available)
- Duration of meeting
- Error messages shown
- Steps already tried
```

## Incident: Integration Failure

### Symptoms
- Notes not syncing to Slack/Notion/etc.
- Zapier Zaps failing
- Error in integration logs

### Immediate Actions
```markdown
## Quick Fix

1. [ ] Check integration status (Settings > Integrations)
2. [ ] Reconnect if showing "Disconnected"
3. [ ] Test integration manually
4. [ ] Check destination app permissions
5. [ ] Verify Zapier Zap is enabled
```

### Manual Workaround
```markdown
## Manual Sync

If integration broken:
1. Export note as Markdown
2. Manually paste to Notion/Slack
3. Create tasks manually in Linear
4. Update CRM by hand if needed
```

## Incident: Complete Outage

### Symptoms
- Granola app won't load
- Status page shows outage
- Multiple users affected

### Immediate Actions
```markdown
## During Outage

1. [ ] Acknowledge internally (Slack)
2. [ ] Enable backup note-taking
3. [ ] Monitor status page
4. [ ] Document affected meetings

Communication Template:
"Granola is currently experiencing an outage.
Please take manual notes. We're monitoring
the situation and will update in 30 minutes."
```

### Backup Procedures
```markdown
## Alternative Note-Taking

1. Designate note-taker per meeting
2. Use Google Docs or Notion directly
3. Record via Zoom/Meet native recording
4. Upload to Granola when service restored
```

## Communication Templates

### Internal Notification (Slack)
```
:warning: Granola Incident

Status: [Investigating/Identified/Monitoring/Resolved]
Impact: [Description of impact]
Workaround: [Available workaround]
ETA: [Expected resolution time]
Updates: Every 30 minutes

Next update: [Time]
```

### User Notification (Email)
```
Subject: Granola Service Update

We're aware of issues with [specific issue] affecting
[scope of impact].

Impact: [What users will experience]
Status: [Current status]
Workaround: [Steps users can take]

We'll update you within [timeframe].

- The Granola Team
```

## Post-Incident

### Incident Report Template
```markdown
## Incident Report: [Title]

**Date:** [Date/Time]
**Duration:** [Start to resolution]
**Severity:** [P1/P2/P3/P4]
**Impact:** [Number of users, meetings affected]

**Timeline:**
- HH:MM - Incident detected
- HH:MM - Investigation started
- HH:MM - Root cause identified
- HH:MM - Resolution applied
- HH:MM - Service restored

**Root Cause:**
[Description of what caused the incident]

**Resolution:**
[What was done to resolve]

**Prevention:**
[Steps to prevent recurrence]

**Lessons Learned:**
- [Key takeaways]
```

### Review Meeting Agenda
```markdown
## Post-Incident Review

1. Incident summary (5 min)
2. Timeline review (10 min)
3. What went well (5 min)
4. What could improve (10 min)
5. Action items (10 min)
6. Assign owners and deadlines (5 min)
```

## Emergency Contacts

### Granola Support
- Email: help@granola.ai
- Enterprise: dedicated support channel
- Status: status.granola.ai

### Internal Escalation
```markdown
## Escalation Path

1. Primary: [IT Support]
2. Secondary: [Granola Admin]
3. Management: [Team Lead]
4. Executive: [VP/CTO] - P1 only
```

## Resources
- [Granola Status](https://status.granola.ai)
- [Support Center](https://granola.ai/help)
- [Known Issues](https://granola.ai/updates)

## Next Steps
Proceed to `granola-data-handling` for data management procedures.
