# Runbook: Rate Limiting Issues

## Runbook: Rate Limiting Issues

### Symptoms
- HTTP 429 responses
- "Rate limit exceeded" errors
- Degraded performance

### Diagnosis
```bash
# Check current rate limit status
curl -I -H "Authorization: $LINEAR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "{ viewer { name } }"}' \
  https://api.linear.app/graphql 2>&1 | grep -i ratelimit

# Check application metrics
curl -s http://localhost:9090/api/v1/query?query=linear_rate_limit_remaining | jq
```

### Resolution Steps
1. **Identify rate limit cause**
   ```bash
   # Check request patterns
   grep "linear" /var/log/app/*.log | grep -E "[0-9]{4}-[0-9]{2}-[0-9]{2}" | wc -l
   ```

2. **Implement emergency throttling**
   ```typescript
   // Emergency rate limiter
   const EMERGENCY_MODE = true;
   const MIN_DELAY_MS = 5000;

   async function emergencyThrottle<T>(fn: () => Promise<T>): Promise<T> {
     if (EMERGENCY_MODE) {
       await new Promise(r => setTimeout(r, MIN_DELAY_MS));
     }
     return fn();
   }
   ```

3. **Disable non-critical operations**
   - Stop background sync jobs
   - Disable polling (if using)
   - Queue non-urgent requests

4. **Wait for rate limit reset**
   - Linear resets every minute
   - Monitor X-RateLimit-Reset header