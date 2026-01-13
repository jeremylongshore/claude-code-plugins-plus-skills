# Examples

### Quick Deploy Script
```bash
#!/bin/bash
# Platform-agnostic deploy helper
case "$1" in
  vercel)
    vercel secrets add windsurf_api_key "$WINDSURF_API_KEY"
    vercel --prod
    ;;
  fly)
    fly secrets set WINDSURF_API_KEY="$WINDSURF_API_KEY"
    fly deploy
    ;;
esac
```