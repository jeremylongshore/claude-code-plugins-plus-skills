# Examples

### Quick Deploy Script
```bash
#!/bin/bash
# Platform-agnostic deploy helper
case "$1" in
  vercel)
    vercel secrets add clay_api_key "$CLAY_API_KEY"
    vercel --prod
    ;;
  fly)
    fly secrets set CLAY_API_KEY="$CLAY_API_KEY"
    fly deploy
    ;;
esac
```