# Examples

### Quick Deploy Script
```bash
#!/bin/bash
# Platform-agnostic deploy helper
case "$1" in
  vercel)
    vercel secrets add exa_api_key "$EXA_API_KEY"
    vercel --prod
    ;;
  fly)
    fly secrets set EXA_API_KEY="$EXA_API_KEY"
    fly deploy
    ;;
esac
```