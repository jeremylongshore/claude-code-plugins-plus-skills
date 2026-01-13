# Otter.Ai Export

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