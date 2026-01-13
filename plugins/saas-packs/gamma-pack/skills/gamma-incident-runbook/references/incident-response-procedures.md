# Incident Response Procedures

## Incident Response Procedures

### Scenario 1: API Returning 5xx Errors

**Symptoms:**
- High error rate in monitoring
- Users reporting failed presentations
- 500/502/503 responses from Gamma

**Actions:**
1. Verify Gamma status: https://status.gamma.app
2. If Gamma outage confirmed:
   - Enable degraded mode / show maintenance message
   - Monitor status page for updates
   - No action needed on our side

3. If Gamma is operational:
   ```bash
   # Check our request patterns
   grep "5[0-9][0-9]" /var/log/app/gamma-*.log | \
     awk '{print $1}' | sort | uniq -c | sort -rn

   # Look for malformed requests
   grep -B5 "500" /var/log/app/gamma-*.log | grep "request"
   ```

4. Rollback recent deployments if issue correlates

### Scenario 2: Rate Limit Exceeded (429)

**Symptoms:**
- 429 responses in logs
- Rate limit metrics at zero
- Slow or queued requests

**Actions:**
1. Immediate mitigation:
   ```bash
   # Enable request throttling
   curl -X POST http://localhost:8080/admin/throttle \
     -d '{"gamma": {"rps": 10}}'
   ```

2. Check for runaway processes:
   ```bash
   # Find high-volume clients
   grep "gamma" /var/log/app/*.log | \
     awk '{print $5}' | sort | uniq -c | sort -rn | head -20
   ```

3. Enable circuit breaker:
   ```bash
   curl -X POST http://localhost:8080/admin/circuit-breaker \
     -d '{"service": "gamma", "state": "open"}'
   ```

4. Long-term: Review rate limit tier with Gamma

### Scenario 3: High Latency

**Symptoms:**
- Slow presentation creation
- Timeouts in logs
- P95 latency > 10s

**Actions:**
1. Check Gamma latency vs our latency:
   ```bash
   # Direct Gamma latency
   for i in {1..5}; do
     curl -w "%{time_total}\n" -o /dev/null -s \
       -H "Authorization: Bearer $GAMMA_API_KEY" \
       https://api.gamma.app/v1/ping
   done
   ```

2. If Gamma is slow:
   - Increase timeouts temporarily
   - Enable async mode for non-critical operations
   - Queue heavy operations

3. If our infrastructure is slow:
   - Check CPU/memory on app servers
   - Review connection pool settings
   - Check network connectivity

### Scenario 4: Authentication Failures (401/403)

**Symptoms:**
- All requests failing with 401
- "Invalid API key" errors
- Sudden authentication failures

**Actions:**
1. Verify API key:
   ```bash
   # Test key directly
   curl -H "Authorization: Bearer $GAMMA_API_KEY" \
     https://api.gamma.app/v1/ping

   # Check key format
   echo $GAMMA_API_KEY | head -c 20
   ```

2. If key is invalid:
   - Check if key was rotated
   - Deploy backup key: `GAMMA_API_KEY_SECONDARY`
   - Generate new key in Gamma dashboard

3. Notify team and update secrets