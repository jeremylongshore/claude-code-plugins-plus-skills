# Examples

### Automated Migration Script
```bash
#!/bin/bash
# migrate-lindy.sh

echo "Starting Lindy SDK migration..."

# Backup
cp package.json package.json.backup
cp -r src src.backup

# Update
npm install @lindy-ai/sdk@latest

# Run tests
npm test

if [ $? -eq 0 ]; then
  echo "Migration successful!"
  rm -rf src.backup package.json.backup
else
  echo "Migration failed. Rolling back..."
  mv package.json.backup package.json
  rm -rf src && mv src.backup src
  npm install
  exit 1
fi
```