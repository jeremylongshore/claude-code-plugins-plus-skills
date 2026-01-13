# Quick Diagnostics

## Quick Diagnostics

### Step 1: Immediate Assessment
```bash
#!/bin/bash
# quick-diag.sh - Run immediately when incident detected

echo "=== Juicebox Quick Diagnostics ==="
echo "Timestamp: $(date -u +%Y-%m-%dT%H:%M:%SZ)"

# Check Juicebox status page
echo ""
echo "=== Juicebox Status ==="
curl -s https://status.juicebox.ai/api/status | jq '.status'

# Check our API health
echo ""
echo "=== Our API Health ==="
curl -s http://localhost:8080/health/ready | jq '.'

# Check recent error logs
echo ""
echo "=== Recent Errors (last 5 min) ==="
kubectl logs -l app=juicebox-integration --since=5m | grep -i error | tail -20

# Check metrics
echo ""
echo "=== Error Rate ==="
curl -s http://localhost:9090/api/v1/query?query=rate\(juicebox_requests_total\{status=\"error\"\}\[5m\]\) | jq '.data.result[0].value[1]'
```

### Step 2: Identify Root Cause
```markdown