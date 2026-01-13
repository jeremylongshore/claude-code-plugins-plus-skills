# Examples

### Quick Deploy Script
```bash
#!/bin/bash
# Platform-agnostic deploy helper
case "$1" in
  vercel)
    vercel secrets add replit_api_key "$REPLIT_API_KEY"
    vercel --prod
    ;;
  fly)
    fly secrets set REPLIT_API_KEY="$REPLIT_API_KEY"
    fly deploy
    ;;
esac
```