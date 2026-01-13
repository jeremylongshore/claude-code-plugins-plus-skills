# Examples

### Quick Diagnostic Commands
```bash
# Check PostHog status
curl -s https://status.posthog.com

# Verify API connectivity
curl -I https://api.posthog.com

# Check local configuration
env | grep POSTHOG
```

### Escalation Path
1. Collect evidence with `posthog-debug-bundle`
2. Check PostHog status page
3. Contact support with request ID