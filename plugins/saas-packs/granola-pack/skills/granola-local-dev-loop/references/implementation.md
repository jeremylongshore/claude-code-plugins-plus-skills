# Implementation Guide

### Step 1: Export Notes Workflow
Configure automatic export of meeting notes:

1. Open Granola Settings
2. Go to Integrations > Zapier
3. Connect your Zapier account
4. Create a Zap: "New Granola Note" trigger

### Step 2: Set Up Local Sync
Create a local directory for meeting notes:

```bash
# Create meeting notes directory
mkdir -p ~/dev/meeting-notes

# Create sync script
cat > ~/dev/scripts/sync-granola-notes.sh << 'EOF'
#!/bin/bash
# Sync Granola notes to local project

NOTES_DIR="$HOME/dev/meeting-notes"
PROJECT_DIR="$1"

if [ -z "$PROJECT_DIR" ]; then
    echo "Usage: sync-granola-notes.sh <project-dir>"
    exit 1
fi

# Copy relevant notes to project docs
cp -r "$NOTES_DIR"/*.md "$PROJECT_DIR/docs/meetings/" 2>/dev/null

echo "Synced meeting notes to $PROJECT_DIR/docs/meetings/"
EOF

chmod +x ~/dev/scripts/sync-granola-notes.sh
```

### Step 3: Integrate with Git Workflow
```bash
# Add meeting notes to .gitignore if sensitive
echo "docs/meetings/*.md" >> .gitignore

# Or track action items only
cat > docs/meetings/README.md << 'EOF'
# Meeting Notes

Action items and decisions from team meetings.
Full notes available in Granola app.
EOF
```

### Step 4: Create Action Item Extractor
```python
#!/usr/bin/env python3
# extract_action_items.py

import re
import sys

def extract_actions(note_file):
    with open(note_file, 'r') as f:
        content = f.read()

    # Find action items section
    actions = re.findall(r'- \[ \] (.+)', content)

    for action in actions:
        print(f"TODO: {action}")

if __name__ == "__main__":
    extract_actions(sys.argv[1])
```