# Runbook: Api Authentication Failure

## Runbook: API Authentication Failure

### Symptoms
- All API calls returning 401/403
- "Authentication required" errors
- Sudden spike in auth errors

### Diagnosis
```bash
# Test API key directly
curl -I -H "Authorization: $LINEAR_API_KEY" \
  https://api.linear.app/graphql

# Check for key format issues
echo $LINEAR_API_KEY | head -c 8
# Should output: lin_api_

# Verify key in secrets manager
vault read secret/data/linear/production
# or
aws secretsmanager get-secret-value --secret-id linear/production
```

### Resolution Steps
1. **Verify API key is loaded correctly**
   ```bash
   # Check env var is set (don't print actual key)
   [ -n "$LINEAR_API_KEY" ] && echo "Key is set" || echo "Key is NOT set"
   ```

2. **Check if key was rotated/revoked**
   - Log into Linear dashboard
   - Navigate to Settings > API > Personal API keys
   - Verify key exists and is active

3. **Generate new API key if needed**
   - Create new key in Linear dashboard
   - Update secrets manager
   - Restart affected services

4. **Rollback if recent deployment**
   ```bash
   # Check last deployment
   git log --oneline -5

   # Rollback to previous version
   git revert HEAD
   ```