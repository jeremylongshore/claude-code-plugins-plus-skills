---
name: fireflies-common-errors
license: MIT
allowed-tools: Read, Grep, Bash
description: Diagnose and fix fireflies.ai common errors and exceptions. use when
  encountering fireflies.ai errors, debugging failed requests, or troubleshooting
  integration issues. trigger with phrases like "fireflies error", "fix fireflies",
  "fireflies not w...
---
# Fireflies.ai Common Errors

## Overview
Quick reference for the top 10 most common Fireflies.ai errors and their solutions.

## Prerequisites
- Fireflies.ai SDK installed
- API credentials configured
- Access to error logs

## Instructions

### Step 1: Identify the Error
Check error message and code in your logs or console.

### Step 2: Find Matching Error Below
Match your error to one of the documented cases.

### Step 3: Apply Solution
Follow the solution steps for your specific error.

## Output
- Identified error cause
- Applied fix
- Verified resolution

## Error Handling

### Authentication Failed
**Error Message:**
```
Authentication error: Invalid API key
```

**Cause:** API key is missing, expired, or invalid.

**Solution:**
```bash
# Verify API key is set
echo $FIREFLIES_API_KEY
```

---

### Rate Limit Exceeded
**Error Message:**
```
Rate limit exceeded. Please retry after X seconds.
```

**Cause:** Too many requests in a short period.

**Solution:**
Implement exponential backoff. See `fireflies-rate-limits` skill.

---

### Network Timeout
**Error Message:**
```
Request timeout after 30000ms
```

**Cause:** Network connectivity or server latency issues.

**Solution:**
```typescript
// Increase timeout
const client = new Client({ timeout: 60000 });
```

## Examples

### Quick Diagnostic Commands
```bash
# Check Fireflies.ai status
curl -s https://status.fireflies.com

# Verify API connectivity
curl -I https://api.fireflies.com

# Check local configuration
env | grep FIREFLIES
```

### Escalation Path
1. Collect evidence with `fireflies-debug-bundle`
2. Check Fireflies.ai status page
3. Contact support with request ID

## Resources
- [Fireflies.ai Status Page](https://status.fireflies.com)
- [Fireflies.ai Support](https://docs.fireflies.com/support)
- [Fireflies.ai Error Codes](https://docs.fireflies.com/errors)

## Next Steps
For comprehensive debugging, see `fireflies-debug-bundle`.