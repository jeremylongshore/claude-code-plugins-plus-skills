---
name: ideogram-common-errors
license: MIT
allowed-tools: Read, Grep, Bash
description: Diagnose and fix ideogram common errors and exceptions. use when encountering
  ideogram errors, debugging failed requests, or troubleshooting integration issues.
  trigger with phrases like "ideogram error", "fix ideogram", "ideogram not working",
  "d...
---
# Ideogram Common Errors

## Overview
Quick reference for the top 10 most common Ideogram errors and their solutions.

## Prerequisites
- Ideogram SDK installed
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
echo $IDEOGRAM_API_KEY
```

---

### Rate Limit Exceeded
**Error Message:**
```
Rate limit exceeded. Please retry after X seconds.
```

**Cause:** Too many requests in a short period.

**Solution:**
Implement exponential backoff. See `ideogram-rate-limits` skill.

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
# Check Ideogram status
curl -s https://status.ideogram.com

# Verify API connectivity
curl -I https://api.ideogram.com

# Check local configuration
env | grep IDEOGRAM
```

### Escalation Path
1. Collect evidence with `ideogram-debug-bundle`
2. Check Ideogram status page
3. Contact support with request ID

## Resources
- [Ideogram Status Page](https://status.ideogram.com)
- [Ideogram Support](https://docs.ideogram.com/support)
- [Ideogram Error Codes](https://docs.ideogram.com/errors)

## Next Steps
For comprehensive debugging, see `ideogram-debug-bundle`.