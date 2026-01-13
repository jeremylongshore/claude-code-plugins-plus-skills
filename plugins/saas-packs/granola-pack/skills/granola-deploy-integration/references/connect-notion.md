# Connect Notion

## Connect Notion

1. Granola Settings > Integrations > Notion
2. Click "Connect Notion"
3. Select workspace
4. Choose integration permissions:
   - Insert content
   - Read pages
   - Update pages
5. Select target database
```

#### Database Schema
```
Meeting Notes Database
├── Title (title)
├── Date (date)
├── Duration (number)
├── Attendees (multi-select)
├── Summary (rich text)
├── Action Items (relation → Tasks)
├── Tags (multi-select)
├── Status (select)
└── Granola Link (url)
```

#### Page Template
```markdown
# {{meeting_title}}

**Date:** {{date}}
**Duration:** {{duration}} minutes
**Attendees:** {{attendees}}

---