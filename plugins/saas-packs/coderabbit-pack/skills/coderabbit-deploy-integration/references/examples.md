# Examples

### Quick Deploy Script
```bash
#!/bin/bash
# Platform-agnostic deploy helper
case "$1" in
  vercel)
    vercel secrets add coderabbit_api_key "$CODERABBIT_API_KEY"
    vercel --prod
    ;;
  fly)
    fly secrets set CODERABBIT_API_KEY="$CODERABBIT_API_KEY"
    fly deploy
    ;;
esac
```