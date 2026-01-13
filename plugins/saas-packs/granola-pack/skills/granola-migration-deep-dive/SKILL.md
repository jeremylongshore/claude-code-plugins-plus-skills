---
name: granola-migration-deep-dive
license: MIT
allowed-tools: Read, Write, Edit
description: Deep dive migration guide from other meeting note tools to granola. use
  when migrating from otter.ai, fireflies, fathom, or other tools, planning data migration,
  or executing transition strategies. trigger with phrases like "migrate to granola",
  "...
---
# Granola Migration Deep Dive

## Overview
Comprehensive guide for migrating to Granola from other meeting note-taking tools.

## Migration Sources

### Supported Source Tools
| Tool | Export Format | Migration Complexity |
|------|--------------|---------------------|
| Otter.ai | TXT, SRT, PDF | Medium |
| Fireflies.ai | TXT, JSON, PDF | Medium |
| Fathom | Markdown, CSV | Low |
| Zoom Native | VTT, TXT | Low |
| Google Meet | SRT, DOCX | Low |
| Microsoft Teams | VTT, DOCX | Low |
| Manual Notes | Markdown | Low |

## Migration Planning

### Assessment Checklist
```markdown
## Pre-Migration Assessment

Data Volume:
- [ ] Total meetings to migrate: ___
- [ ] Date range: ___ to ___
- [ ] Total storage size: ___ GB
- [ ] Number of users: ___

Content Types:
- [ ] Transcripts: ___
- [ ] AI summaries: ___
- [ ] Action items: ___
- [ ] Audio files: ___

Integrations:
- [ ] CRM connections: ___
- [ ] Slack/Teams channels: ___
- [ ] Documentation tools: ___
- [ ] Workflow automations: ___

Timeline:
- [ ] Target cutover date: ___
- [ ] Parallel running period: ___ weeks
- [ ] User training dates: ___
```

### Migration Strategy Options

#### Option 1: Clean Start
```markdown
## Clean Start (Recommended for < 100 meetings)

Approach:
- Start fresh with Granola
- Archive historical data externally
- No data import

Pros:
- Simplest approach
- No migration complexity
- Clean slate

Cons:
- Historical search not in Granola
- Need external archive access

Best For:
- Small teams
- Minimal historical needs
- Quick deployment
```

#### Option 2: Selective Migration
```markdown
## Selective Migration (100-1000 meetings)

Approach:
- Migrate key meetings only
- Archive rest externally
- Selective import

Selection Criteria:
- Client meetings (last 6 months)
- Decision-making meetings
- Recurring important meetings
- Referenced action items

Pros:
- Important data preserved
- Manageable scope
- Faster completion

Cons:
- Requires selection effort
- Incomplete history
```

#### Option 3: Full Migration
```markdown
## Full Migration (Enterprise)

Approach:
- Export all historical data
- Transform to Granola format
- Import everything

Pros:
- Complete history
- Full searchability
- No external archive needed

Cons:
- Complex and time-consuming
- May require professional services
- Higher cost
```

## Source-Specific Migration

### From Otter.ai

#### Export Process
```markdown
## Otter.ai Export

1. Log into Otter.ai
2. Go to each conversation
3. Click ... menu > Export
4. Select format:
   - TXT for transcript
   - PDF for formatted notes
   - SRT for subtitles
5. Repeat for all conversations

Bulk Export (Pro/Business):
1. Settings > My Account
2. Click "Export All"
3. Wait for email
4. Download zip file
```

#### Data Mapping
```yaml
# Otter.ai → Granola Mapping

Otter Field:          Granola Field:
conversation_title → meeting_title
date              → meeting_date
transcript        → transcript
summary           → summary
action_items      → action_items
speakers          → attendees (partial)
keywords          → (no direct mapping)
```

#### Conversion Script
```python
#!/usr/bin/env python3
"""Convert Otter.ai exports to Granola format"""

import json
import os
from datetime import datetime

def convert_otter_to_granola(otter_file, output_dir):
    with open(otter_file, 'r') as f:
        content = f.read()

    # Parse Otter format (varies by export type)
    # This is a simplified example

    granola_note = f"""# Meeting Notes

**Imported from:** Otter.ai
**Original Date:** {datetime.now().strftime('%Y-%m-%d')}

## Transcript
{content}

## Action Items
[Review and extract manually]

---
*Migrated to Granola on {datetime.now().strftime('%Y-%m-%d')}*
"""

    output_file = os.path.join(output_dir, 'imported_note.md')
    with open(output_file, 'w') as f:
        f.write(granola_note)

    return output_file
```

### From Fireflies.ai

#### Export Process
```markdown
## Fireflies Export

1. Log into Fireflies.ai
2. Go to Meetings
3. Select meetings (checkbox)
4. Click "Export"
5. Choose format: JSON (recommended)
6. Download

API Export (Enterprise):
```bash
curl -X GET "https://api.fireflies.ai/v1/transcripts" \
  -H "Authorization: Bearer $FIREFLIES_API_KEY" \
  -o fireflies_export.json
```

#### Data Mapping
```yaml
# Fireflies → Granola Mapping

Fireflies Field:      Granola Field:
title             → meeting_title
date              → meeting_date
transcript        → transcript
summary           → summary
action_items      → action_items
participants      → attendees
```

### From Fathom

#### Export Process
```markdown
## Fathom Export

1. Open Fathom dashboard
2. Select call
3. Click "Download"
4. Choose: Markdown or CSV
5. Repeat for all calls

Batch Export:
- Contact Fathom support for bulk export
- Request API access if available
```

### From Native Recording (Zoom/Meet/Teams)

#### Zoom Cloud Recordings
```markdown
## Zoom Export

1. Go to Zoom web portal
2. Recordings > Cloud Recordings
3. Download:
   - Audio/Video file
   - VTT transcript
4. Upload audio to transcription service if needed
```

#### Google Meet
```markdown
## Google Meet Export

1. Check Google Drive
2. Find meeting recordings folder
3. Download transcript (if enabled)
4. Convert from SRT/VTT to text
```

## Data Transformation

### Transformation Pipeline
```
Source Export
     ↓
Parse Original Format
     ↓
Normalize Data Structure
     ↓
Map to Granola Schema
     ↓
Validate Integrity
     ↓
Generate Markdown Files
     ↓
Archive in Notion/Drive
```

### Batch Conversion Script
```python
#!/usr/bin/env python3
"""Batch convert meeting notes to Granola format"""

import os
import json
from pathlib import Path

def batch_convert(source_dir, output_dir, source_type):
    """Convert all files from source format to Granola Markdown"""

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    converters = {
        'otter': convert_otter,
        'fireflies': convert_fireflies,
        'zoom': convert_zoom_vtt,
    }

    converter = converters.get(source_type)
    if not converter:
        raise ValueError(f"Unknown source type: {source_type}")

    converted = []
    for file in Path(source_dir).glob('*'):
        try:
            output = converter(file, output_dir)
            converted.append(output)
            print(f"Converted: {file.name}")
        except Exception as e:
            print(f"Error converting {file.name}: {e}")

    print(f"\nConverted {len(converted)} files")
    return converted

if __name__ == "__main__":
    import sys
    batch_convert(sys.argv[1], sys.argv[2], sys.argv[3])
```

## Execution Plan

### Week 1: Preparation
```markdown
## Week 1 Tasks

Day 1-2: Assessment
- [ ] Inventory all source data
- [ ] Identify critical meetings
- [ ] Document integrations
- [ ] Define success criteria

Day 3-4: Export
- [ ] Export from source tool
- [ ] Verify export completeness
- [ ] Secure backup of exports
- [ ] Document any gaps

Day 5: Granola Setup
- [ ] Configure Granola workspace
- [ ] Set up integrations
- [ ] Create templates
- [ ] Test with sample meeting
```

### Week 2: Migration
```markdown
## Week 2 Tasks

Day 1-2: Conversion
- [ ] Run conversion scripts
- [ ] Validate converted data
- [ ] Fix any errors
- [ ] Create import packages

Day 3-4: Import
- [ ] Import to external archive (Notion)
- [ ] Tag as historical
- [ ] Verify accessibility
- [ ] Set up search

Day 5: Verification
- [ ] Spot check random samples
- [ ] Verify key meetings accessible
- [ ] Test search functionality
- [ ] Document location
```

### Week 3-4: Parallel Running
```markdown
## Parallel Period

Both tools active:
- Record in Granola (primary)
- Source tool as backup
- Compare quality
- Gather feedback

Daily:
- [ ] Monitor both tools
- [ ] Note any issues
- [ ] Collect user feedback

End of parallel:
- [ ] Review comparison
- [ ] Address issues
- [ ] Get sign-off
- [ ] Schedule cutover
```

### Week 5: Cutover
```markdown
## Cutover Tasks

Day 1: Final Export
- [ ] Export any new data from source
- [ ] Run final conversion
- [ ] Complete import

Day 2: Disable Source
- [ ] Turn off source tool recording
- [ ] Downgrade/cancel subscription
- [ ] Remove integrations

Day 3-5: Support
- [ ] Monitor closely
- [ ] Address issues immediately
- [ ] Document lessons learned
- [ ] Celebrate completion!
```

## User Communication

### Announcement Template
```markdown
## Migration Announcement

Subject: Switching to Granola for Meeting Notes

Team,

We're migrating from [Source Tool] to Granola for meeting notes.

**Key Dates:**
- Parallel running: [Start] - [End]
- Full cutover: [Date]

**What You Need to Do:**
1. Install Granola: granola.ai/download
2. Sign in with company SSO
3. Attend training: [Date/Link]

**Why Granola:**
- No meeting bot required
- Better privacy
- Improved integrations

**Historical Notes:**
Your past meeting notes will be available in [Notion/Drive].

Questions? Contact [Support Email].

Thanks,
[Your Name]
```

### Training Agenda
```markdown
## Granola Training (30 min)

1. Introduction (5 min)
   - Why Granola
   - Key differences from [Source]

2. Setup (10 min)
   - Install app
   - Connect calendar
   - Grant permissions

3. First Meeting (10 min)
   - How recording works
   - Taking live notes
   - Reviewing AI notes

4. Q&A (5 min)
   - Common questions
   - Where to get help
```

## Rollback Plan

### If Migration Fails
```markdown
## Rollback Procedure

Triggers for Rollback:
- > 20% of meetings not captured
- Critical integration failure
- User adoption < 30%
- Data loss detected

Rollback Steps:
1. Communicate pause to team
2. Re-enable source tool
3. Export any Granola notes
4. Investigate issues
5. Plan remediation
6. Attempt migration again

Note: Rollback only possible during parallel period
```

## Resources
- [Granola Migration Guide](https://granola.ai/help/migration)
- [Import Support](https://granola.ai/support)
- [Enterprise Migration Services](https://granola.ai/enterprise)

## Post-Migration

### Success Metrics
```markdown
## 30-Day Review

Adoption:
- [ ] Active users: ___% of total
- [ ] Meetings captured: ___/week
- [ ] Notes shared: ___

Quality:
- [ ] User satisfaction: ___/5
- [ ] Transcription accuracy: ___%
- [ ] Action item detection: ___%

Issues:
- [ ] Open tickets: ___
- [ ] Resolved: ___
- [ ] Escalated: ___
```

### Lessons Learned
```markdown
## Post-Migration Review

What Went Well:
-

What Could Improve:
-

Recommendations:
-

Documentation Updates:
-
```
