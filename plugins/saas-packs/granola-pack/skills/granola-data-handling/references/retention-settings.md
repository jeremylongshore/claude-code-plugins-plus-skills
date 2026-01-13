# Retention Settings

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