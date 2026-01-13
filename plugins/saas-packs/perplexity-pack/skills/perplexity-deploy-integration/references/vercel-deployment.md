# Vercel Deployment

## Vercel Deployment

### Environment Setup
```bash
# Add Perplexity secrets to Vercel
vercel secrets add perplexity_api_key sk_live_***
vercel secrets add perplexity_webhook_secret whsec_***

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
    "PERPLEXITY_API_KEY": "@perplexity_api_key"
  },
  "functions": {
    "api/**/*.ts": {
      "maxDuration": 30
    }
  }
}
```