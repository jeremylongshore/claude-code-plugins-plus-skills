# Examples

### Quick Deploy Script
```bash
#!/bin/bash
# Platform-agnostic deploy helper
case "$1" in
  vercel)
    vercel secrets add ideogram_api_key "$IDEOGRAM_API_KEY"
    vercel --prod
    ;;
  fly)
    fly secrets set IDEOGRAM_API_KEY="$IDEOGRAM_API_KEY"
    fly deploy
    ;;
esac
```