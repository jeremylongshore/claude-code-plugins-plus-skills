# Examples

### Complete Migration Script
```bash
#!/bin/bash
# migrate-to-lindy.sh

echo "Starting Lindy migration..."

# Phase 1: Assessment
npm run migration:assess

# Phase 2: Export
npm run migration:export

# Phase 3: Transform
npm run migration:transform

# Phase 4: Validate
npm run migration:validate

# Phase 5: Import (with checkpoint)
npm run migration:checkpoint create pre-import
npm run migration:import

# Phase 6: Test
npm run migration:test

echo "Migration complete!"
```