# Examples

### Quick Deploy Script
```bash
#!/bin/bash
# Platform-agnostic deploy helper
case "$1" in
  vercel)
    vercel secrets add vastai_api_key "$VASTAI_API_KEY"
    vercel --prod
    ;;
  fly)
    fly secrets set VASTAI_API_KEY="$VASTAI_API_KEY"
    fly deploy
    ;;
esac
```