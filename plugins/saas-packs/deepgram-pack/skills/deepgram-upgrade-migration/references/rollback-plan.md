# Rollback Plan

## Rollback Plan

### Prepare Rollback
```typescript
// lib/rollback.ts
interface DeploymentVersion {
  sdkVersion: string;
  model: string;
  config: Record<string, unknown>;
  deployedAt: Date;
}

class RollbackManager {
  private versions: DeploymentVersion[] = [];
  private maxVersions = 5;

  recordDeployment(version: Omit<DeploymentVersion, 'deployedAt'>) {
    this.versions.unshift({
      ...version,
      deployedAt: new Date(),
    });

    // Keep only last N versions
    this.versions = this.versions.slice(0, this.maxVersions);
  }

  getLastStableVersion(): DeploymentVersion | null {
    return this.versions[1] || null; // Skip current version
  }

  getRollbackInstructions(target: DeploymentVersion): string[] {
    return [
      `1. Update package.json: "@deepgram/sdk": "${target.sdkVersion}"`,
      `2. Run: npm install`,
      `3. Update config: model = "${target.model}"`,
      `4. Verify: npm test`,
      `5. Deploy: npm run deploy`,
      `6. Monitor: Check dashboards for 30 minutes`,
    ];
  }
}
```

### Emergency Rollback Script
```bash
#!/bin/bash
# scripts/emergency-rollback.sh

set -e

echo "=== Emergency Rollback ==="

# Store current version
CURRENT_VERSION=$(npm list @deepgram/sdk --json | jq -r '.dependencies["@deepgram/sdk"].version')
echo "Current version: $CURRENT_VERSION"

# Get previous version from git
git show HEAD~1:package-lock.json > /tmp/prev-lock.json
PREV_VERSION=$(cat /tmp/prev-lock.json | jq -r '.packages["node_modules/@deepgram/sdk"].version')
echo "Rolling back to: $PREV_VERSION"

# Confirm
read -p "Proceed with rollback? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
  exit 1
fi

# Rollback
npm install @deepgram/sdk@$PREV_VERSION --save-exact

# Verify
npm test

echo "Rollback complete. Deploy when ready."
```