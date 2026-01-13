---
name: granola-data-handling
license: MIT
allowed-tools: Read, Write, Edit
description: Data export, retention, and gdpr compliance for granola. use when managing
  data exports, configuring retention policies, or ensuring regulatory compliance.
  trigger with phrases like "granola export", "granola data", "granola gdpr", "granola
  retent...
---
# Granola Data Handling

## Overview
Manage data export, retention policies, and regulatory compliance for Granola meeting data.

## Prerequisites
- Granola admin access
- Understanding of data regulations (GDPR, CCPA)
- Export destination prepared

## Data Types in Granola

### Data Classification
| Data Type | Sensitivity | Retention | Export Format |
|-----------|-------------|-----------|---------------|
| Meeting Notes | Medium | Configurable | Markdown, JSON |
| Transcripts | High | Configurable | Text, JSON |
| Audio | High | Short-term | WAV, MP3 |
| Attendee Info | PII | With notes | JSON |
| Action Items | Medium | With notes | Markdown |
| Metadata | Low | Long-term | JSON |

### Data Locations
```
Granola Data Storage
├── Cloud Storage (Primary)
│   ├── Notes & Summaries
│   ├── Transcripts
│   └── Metadata
├── Temporary Storage
│   ├── Audio (processing)
│   └── Upload queue
└── Local Cache (Device)
    ├── Recent notes
    └── App settings
```

## Data Export

### Individual Export
```markdown
## Export Single Meeting

1. Open meeting in Granola
2. Click ... menu
3. Select "Export"
4. Choose format:
   - Markdown (.md)
   - PDF (.pdf)
   - Word (.docx)
   - JSON (full data)
5. Download file
```

### Bulk Export
```markdown
## Export All Data

1. Settings > Data > Export
2. Select "All Data"
3. Choose date range (optional)
4. Select format: JSON (recommended)
5. Confirm export request
6. Wait for email with download link
7. Download within 24 hours
```

### Export Formats

#### Markdown Export
```markdown
# Meeting Title

**Date:** January 6, 2025
**Duration:** 45 minutes
**Attendees:** Sarah Chen, Mike Johnson

## Summary
[AI-generated summary]

## Key Points
- [Point 1]
- [Point 2]

## Action Items
- [ ] Task 1 (@assignee, due: date)

## Transcript
[Full transcript if included]
```

#### JSON Export
```json
{
  "export_version": "1.0",
  "export_date": "2025-01-06T15:00:00Z",
  "user": {
    "id": "user_123",
    "email": "user@company.com"
  },
  "meetings": [
    {
      "id": "note_abc123",
      "title": "Sprint Planning",
      "date": "2025-01-06",
      "start_time": "2025-01-06T14:00:00Z",
      "end_time": "2025-01-06T14:45:00Z",
      "attendees": [
        {"name": "Sarah Chen", "email": "sarah@company.com"}
      ],
      "summary": "Discussed Q1 priorities...",
      "transcript": "Full transcript text...",
      "action_items": [
        {"text": "Review PRs", "assignee": "mike", "due": "2025-01-08"}
      ],
      "created_at": "2025-01-06T14:46:00Z",
      "updated_at": "2025-01-06T15:00:00Z"
    }
  ]
}
```

## Data Retention

### Configure Retention Policy
```markdown
## Retention Settings

Location: Settings > Privacy > Data Retention

Options:
1. Keep Forever (default)
   - All data retained indefinitely
   - User must manually delete

2. Time-Based Deletion
   - Notes: 30/60/90/365 days
   - Transcripts: 7/30/90 days
   - Audio: Immediately/7/30 days

3. Storage-Based
   - Delete oldest when quota reached
   - Archive to external before delete
```

### Recommended Retention by Type
| Data Type | Recommendation | Reason |
|-----------|---------------|--------|
| Notes | 1-2 years | Reference value |
| Transcripts | 90 days | Storage efficiency |
| Audio | Delete after processing | Privacy, storage |
| Metadata | 2 years | Analytics value |

### Retention Policy Template
```yaml
# Company Retention Policy

Default:
  notes: 365 days
  transcripts: 90 days
  audio: delete_after_processing

By Workspace:
  HR:
    notes: 730 days  # 2 years (legal)
    transcripts: 30 days
    audio: delete_immediately

  Sales:
    notes: 365 days
    transcripts: 90 days  # CRM reference
    audio: 30 days

  Engineering:
    notes: 180 days
    transcripts: 7 days
    audio: delete_after_processing
```

## GDPR Compliance

### Rights Implementation
| Right | Implementation | Process |
|-------|---------------|---------|
| Access | Data export | Self-service export |
| Rectification | Edit notes | User can edit |
| Erasure | Delete account | Settings > Delete |
| Portability | JSON export | Full data download |
| Objection | Opt-out | Don't record specific meetings |

### Subject Access Request (SAR)
```markdown
## Handling SAR

1. Receive Request
   - Verify identity
   - Log request with timestamp

2. Locate Data
   - Search by email address
   - Include all workspaces
   - Check shared notes

3. Compile Response
   - Export user's data (JSON)
   - Include metadata
   - Document third-party sharing

4. Deliver Within 30 Days
   - Secure delivery method
   - Provide in readable format
   - Explain data categories

5. Document Completion
   - Log response date
   - Store proof of delivery
```

### Data Deletion Request
```markdown
## Right to Be Forgotten

1. Verify Identity
   - Email confirmation
   - Additional verification for sensitive data

2. Scope Deletion
   - All personal data
   - Shared notes (mark as deleted, retain structure)
   - Integration data (notify third parties)

3. Execute Deletion
   - Delete from primary storage
   - Delete from backups (within 30 days)
   - Revoke integrations

4. Confirm Completion
   - Notify requestor
   - Provide confirmation ID
   - Document process
```

### DPA (Data Processing Agreement)
```markdown
## DPA Checklist

Granola provides:
- [ ] Standard DPA template
- [ ] SCCs for international transfer
- [ ] Sub-processor list
- [ ] Security measures documentation
- [ ] Breach notification procedures

Company must:
- [ ] Sign DPA with Granola
- [ ] Update privacy policy
- [ ] Obtain consent for recording
- [ ] Train staff on procedures
```

## CCPA Compliance

### California Consumer Rights
| Right | Implementation |
|-------|---------------|
| Know | Disclosure of data collected |
| Delete | Account deletion |
| Opt-out | No sale (Granola doesn't sell data) |
| Non-discrimination | Equal service |

### Privacy Notice Requirements
```markdown
## Meeting Recording Notice

Include in meeting invites:
"This meeting may be recorded using Granola AI
for note-taking purposes. By attending, you consent
to recording. Contact [email] with questions or
to request data access/deletion."
```

## Data Security

### Encryption Standards
| State | Method | Standard |
|-------|--------|----------|
| At Rest | AES-256 | Industry standard |
| In Transit | TLS 1.3 | Latest protocol |
| Backup | AES-256 | Same as primary |

### Access Controls
```markdown
## Data Access Matrix

| Role | Notes | Transcripts | Audio | Admin |
|------|-------|-------------|-------|-------|
| Owner | RWD | RWD | RD | Full |
| Admin | RW | RW | R | Limited |
| Member | RW | R | - | None |
| Viewer | R | - | - | None |

R = Read, W = Write, D = Delete
```

## Archival Strategy

### Long-Term Archive
```markdown
## Archive Workflow

Monthly:
1. Export notes > 6 months old
2. Format: JSON (complete)
3. Store in company archive
4. Verify export integrity
5. Delete from Granola
6. Update archive index

Archive Storage:
- Primary: Google Cloud Storage
- Backup: AWS S3 Glacier
- Retention: 7 years
```

### Archive Access
```markdown
## Retrieving Archived Data

1. Search archive index
2. Locate in storage bucket
3. Download JSON file
4. Parse for required data
5. Re-import to Granola if needed
```

## Resources
- [Granola Privacy Policy](https://granola.ai/privacy)
- [Granola Security](https://granola.ai/security)
- [GDPR Documentation](https://granola.ai/gdpr)

## Next Steps
Proceed to `granola-enterprise-rbac` for role-based access control.
