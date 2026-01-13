# Vercel Deployment

## Vercel Deployment

### Environment Setup
```bash
# Add FireCrawl secrets to Vercel
vercel secrets add firecrawl_api_key sk_live_***
vercel secrets add firecrawl_webhook_secret whsec_***

# Link to project
vercel link

# Deploy preview
vercel

# Deploy production
vercel --prod
```

### vercel.json Configuration
```json
{
  "env": {
    "FIRECRAWL_API_KEY": "@firecrawl_api_key"
  },
  "functions": {
    "api/**/*.ts": {
      "maxDuration": 30
    }
  }
}
```