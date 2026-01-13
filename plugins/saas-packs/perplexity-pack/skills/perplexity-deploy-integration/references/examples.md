# Examples

### Quick Deploy Script
```bash
#!/bin/bash
# Platform-agnostic deploy helper
case "$1" in
  vercel)
    vercel secrets add perplexity_api_key "$PERPLEXITY_API_KEY"
    vercel --prod
    ;;
  fly)
    fly secrets set PERPLEXITY_API_KEY="$PERPLEXITY_API_KEY"
    fly deploy
    ;;
esac
```