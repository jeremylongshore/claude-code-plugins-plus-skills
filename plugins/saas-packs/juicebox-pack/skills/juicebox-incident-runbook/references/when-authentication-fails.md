# When Authentication Fails

## When Authentication Fails

1. **Verify API Key**
   ```bash
   # Mask key for logging
   echo "Key prefix: ${JUICEBOX_API_KEY:0:10}..."

   # Test auth
   curl -H "Authorization: Bearer $JUICEBOX_API_KEY" \
     https://api.juicebox.ai/v1/auth/me
   ```

2. **Check Key Status in Dashboard**
   - Log into https://app.juicebox.ai
   - Verify key is active and not revoked

3. **Rotate Key if Compromised**
   - Generate new key in dashboard
   - Update secret manager
   - Restart pods
   ```bash
   kubectl rollout restart deployment/juicebox-integration
   ```

4. **Verify Recovery**
   - Check health endpoint
   - Monitor error rate
```

### Rate Limit Response
```markdown