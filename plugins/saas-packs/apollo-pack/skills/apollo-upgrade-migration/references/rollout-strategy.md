# Rollout Strategy

## Rollout Strategy

### Phase 1: Canary (1%)
```yaml
# kubernetes/apollo-canary.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: apollo-config-canary
data:
  APOLLO_USE_NEW_API: "true"
---
# Deploy to 1% of traffic
```

### Phase 2: Gradual Rollout
```typescript
// Gradual rollout based on user ID
function shouldUseNewApi(userId: string): boolean {
  const rolloutPercentage = parseInt(process.env.APOLLO_NEW_API_ROLLOUT || '0');
  const hash = hashCode(userId) % 100;
  return hash < rolloutPercentage;
}

function hashCode(str: string): number {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = ((hash << 5) - hash) + str.charCodeAt(i);
    hash |= 0;
  }
  return Math.abs(hash);
}
```

### Phase 3: Full Migration
```bash
# After successful canary
export APOLLO_USE_NEW_API=true

# Remove compat layer
rm src/lib/apollo/compat.ts

# Update all imports
find src -name "*.ts" -exec sed -i 's/apolloCompat/apollo/g' {} \;
```