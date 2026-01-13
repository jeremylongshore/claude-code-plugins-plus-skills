# Data Transformation

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