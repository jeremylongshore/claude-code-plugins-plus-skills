# Examples

### Quick Deploy Script
```bash
#!/bin/bash
# Platform-agnostic deploy helper
case "$1" in
  vercel)
    vercel secrets add posthog_api_key "$POSTHOG_API_KEY"
    vercel --prod
    ;;
  fly)
    fly secrets set POSTHOG_API_KEY="$POSTHOG_API_KEY"
    fly deploy
    ;;
esac
```