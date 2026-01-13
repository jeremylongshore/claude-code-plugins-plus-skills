# Examples

### Quick Deploy Script
```bash
#!/bin/bash
# Platform-agnostic deploy helper
case "$1" in
  vercel)
    vercel secrets add fireflies_api_key "$FIREFLIES_API_KEY"
    vercel --prod
    ;;
  fly)
    fly secrets set FIREFLIES_API_KEY="$FIREFLIES_API_KEY"
    fly deploy
    ;;
esac
```