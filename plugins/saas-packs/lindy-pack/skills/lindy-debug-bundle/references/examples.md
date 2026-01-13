# Examples

### Quick Health Check
```bash
# One-liner health check
curl -s -H "Authorization: Bearer $LINDY_API_KEY" \
  https://api.lindy.ai/v1/users/me | jq '.email'
```

### Full Debug Script
```bash
#!/bin/bash
# save as lindy-debug.sh

echo "Collecting Lindy debug info..."
npx ts-node debug/collect-agent-state.ts $1 > debug-bundle.json
echo "Bundle saved to debug-bundle.json"
```