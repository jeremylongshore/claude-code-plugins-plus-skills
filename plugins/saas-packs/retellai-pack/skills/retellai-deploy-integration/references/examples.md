# Examples

### Quick Deploy Script
```bash
#!/bin/bash
# Platform-agnostic deploy helper
case "$1" in
  vercel)
    vercel secrets add retellai_api_key "$RETELLAI_API_KEY"
    vercel --prod
    ;;
  fly)
    fly secrets set RETELLAI_API_KEY="$RETELLAI_API_KEY"
    fly deploy
    ;;
esac
```