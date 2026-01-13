---
name: granola-rate-limits
license: MIT
allowed-tools: Read, Write, Edit
description: Understand granola usage limits, quotas, and plan restrictions. use when
  hitting usage limits, planning capacity, or understanding plan differences. trigger
  with phrases like "granola limits", "granola quota", "granola usage", "granola plan
  limits...
---
# Granola Rate Limits

## Overview
Understand and manage Granola usage limits across different plan tiers.

## Plan Comparison

### Free Plan
| Limit | Value | Notes |
|-------|-------|-------|
| Meetings per month | 10 | Resets monthly |
| Meeting duration | 60 min | Per meeting |
| Storage | 5 GB | Total across all notes |
| Integrations | 2 | Basic only |
| Export formats | Markdown | Limited formats |

### Pro Plan ($10/month)
| Limit | Value | Notes |
|-------|-------|-------|
| Meetings per month | Unlimited | No caps |
| Meeting duration | 4 hours | Per meeting |
| Storage | 50 GB | Expandable |
| Integrations | All | Full access |
| Export formats | All | PDF, Docs, etc. |
| Templates | Custom | Create your own |

### Business Plan ($25/month)
| Limit | Value | Notes |
|-------|-------|-------|
| Meetings per month | Unlimited | No caps |
| Meeting duration | 8 hours | Extended |
| Storage | 200 GB | Team shared |
| Team members | Up to 50 | Per workspace |
| Admin controls | Full | SSO, audit logs |
| Priority support | Yes | 24-hour response |

### Enterprise Plan (Custom)
| Feature | Availability |
|---------|-------------|
| Custom limits | Negotiable |
| Dedicated support | Yes |
| SLA guarantees | Yes |
| Custom integrations | Yes |
| On-premise option | Available |

## Current Usage Check

### Check in Granola App
1. Open Granola
2. Go to Settings > Account
3. View "Usage" section
4. See:
   - Meetings this month
   - Storage used
   - Days until reset

### Usage Dashboard Elements
```
Monthly Usage:
[========--] 8/10 meetings

Storage:
[====------] 2.1 GB / 5 GB

Integrations:
[==========] 2/2 connected

Reset Date: February 1, 2025
```

## Rate Limit Behaviors

### When Approaching Limits
| % Used | Notification | Action |
|--------|-------------|--------|
| 75% | Warning banner | Plan ahead |
| 90% | Email alert | Consider upgrade |
| 100% | Recording blocked | Upgrade or wait |

### What Happens at Limits
- **Meeting limit reached:** New recordings blocked until reset
- **Storage full:** Cannot save new notes until space cleared
- **Duration exceeded:** Recording stops at limit

## Optimizing Usage

### Reduce Meeting Count
```markdown
## Strategies
1. Combine related meetings
2. Skip recording for informal chats
3. Use selective recording
4. Delete draft/test meetings
```

### Manage Storage
```markdown
## Storage Tips
1. Export old notes and delete from Granola
2. Compress attachments before linking
3. Archive completed projects
4. Delete duplicate recordings
```

### Calculate Needs
```markdown
## Usage Estimation

Monthly meetings: 20
Average duration: 45 min
Storage per meeting: ~50 MB

Required Plan: Pro
- Meeting limit: Unlimited (need > 10)
- Duration: 4 hrs (need 45 min) ✓
- Storage: 50 GB (need ~1 GB/month) ✓
```

## Limit Reset Schedule
- **Monthly limits:** Reset on billing date
- **Daily limits:** Reset at midnight UTC
- **Storage:** Does not auto-reset (manual management)

## Handling Limit Errors

### Error: "Meeting Limit Reached"
**Solutions:**
1. Wait for monthly reset
2. Upgrade to Pro plan
3. Delete unused meetings from current period

### Error: "Recording Duration Exceeded"
**Solutions:**
1. Upgrade plan for longer limits
2. Split long meetings into parts
3. Start new recording if needed

### Error: "Storage Full"
**Solutions:**
1. Export notes to external storage
2. Delete old meetings
3. Upgrade to higher storage plan

## API/Integration Limits

### Zapier Integration
| Plan | Zap Runs/Month |
|------|----------------|
| Free | Tied to Zapier plan |
| Pro | Tied to Zapier plan |
| Business | Priority queuing |

### Webhook Limits
- Rate: 10 requests/second
- Payload: 1 MB max
- Timeout: 30 seconds

## Resources
- [Granola Pricing](https://granola.ai/pricing)
- [Plan Comparison](https://granola.ai/compare)
- [Upgrade Options](https://granola.ai/upgrade)

## Next Steps
Proceed to `granola-security-basics` for security best practices.
