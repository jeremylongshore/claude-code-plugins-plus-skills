# Examples

### Quick Deploy Script
```bash
#!/bin/bash
# Platform-agnostic deploy helper
case "$1" in
  vercel)
    vercel secrets add firecrawl_api_key "$FIRECRAWL_API_KEY"
    vercel --prod
    ;;
  fly)
    fly secrets set FIRECRAWL_API_KEY="$FIRECRAWL_API_KEY"
    fly deploy
    ;;
esac
```