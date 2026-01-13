# Examples

### Quick Deploy Script
```bash
#!/bin/bash
# Platform-agnostic deploy helper
case "$1" in
  vercel)
    vercel secrets add groq_api_key "$GROQ_API_KEY"
    vercel --prod
    ;;
  fly)
    fly secrets set GROQ_API_KEY="$GROQ_API_KEY"
    fly deploy
    ;;
esac
```