# Immediate Actions By Error Type

## Immediate Actions by Error Type

### 401/403 - Authentication
```bash
# Verify API key is set
kubectl get secret clay-secrets -o jsonpath='{.data.api-key}' | base64 -d

# Check if key was rotated
# → Verify in Clay dashboard

# Remediation: Update secret and restart pods
kubectl create secret generic clay-secrets --from-literal=api-key=NEW_KEY --dry-run=client -o yaml | kubectl apply -f -
kubectl rollout restart deployment/clay-integration
```

### 429 - Rate Limited
```bash
# Check rate limit headers
curl -v https://api.clay.com 2>&1 | grep -i rate

# Enable request queuing
kubectl set env deployment/clay-integration RATE_LIMIT_MODE=queue

# Long-term: Contact Clay for limit increase
```

### 500/503 - Clay Errors
```bash
# Enable graceful degradation
kubectl set env deployment/clay-integration CLAY_FALLBACK=true

# Notify users of degraded service
# Update status page

# Monitor Clay status for resolution
```