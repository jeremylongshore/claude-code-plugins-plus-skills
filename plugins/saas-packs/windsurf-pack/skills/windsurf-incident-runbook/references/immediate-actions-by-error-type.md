# Immediate Actions By Error Type

## Immediate Actions by Error Type

### 401/403 - Authentication
```bash
# Verify API key is set
kubectl get secret windsurf-secrets -o jsonpath='{.data.api-key}' | base64 -d

# Check if key was rotated
# → Verify in Windsurf dashboard

# Remediation: Update secret and restart pods
kubectl create secret generic windsurf-secrets --from-literal=api-key=NEW_KEY --dry-run=client -o yaml | kubectl apply -f -
kubectl rollout restart deployment/windsurf-integration
```

### 429 - Rate Limited
```bash
# Check rate limit headers
curl -v https://api.windsurf.com 2>&1 | grep -i rate

# Enable request queuing
kubectl set env deployment/windsurf-integration RATE_LIMIT_MODE=queue

# Long-term: Contact Windsurf for limit increase
```

### 500/503 - Windsurf Errors
```bash
# Enable graceful degradation
kubectl set env deployment/windsurf-integration WINDSURF_FALLBACK=true

# Notify users of degraded service
# Update status page

# Monitor Windsurf status for resolution
```