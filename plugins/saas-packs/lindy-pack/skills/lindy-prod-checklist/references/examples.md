# Examples

### Deployment Gate Script
```bash
#!/bin/bash
# deploy-gate.sh

echo "Running Lindy pre-deployment checks..."

npx ts-node scripts/pre-deployment-check.ts
if [ $? -ne 0 ]; then
  echo "Pre-deployment checks FAILED"
  exit 1
fi

echo "All checks passed. Proceeding with deployment."
```