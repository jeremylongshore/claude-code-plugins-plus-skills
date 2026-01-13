# Examples

### Quick Deploy Script
```bash
#!/bin/bash
# Platform-agnostic deploy helper
case "$1" in
  vercel)
    vercel secrets add instantly_api_key "$INSTANTLY_API_KEY"
    vercel --prod
    ;;
  fly)
    fly secrets set INSTANTLY_API_KEY="$INSTANTLY_API_KEY"
    fly deploy
    ;;
esac
```