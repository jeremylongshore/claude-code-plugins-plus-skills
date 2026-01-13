# Vercel Deployment

## Vercel Deployment

### Environment Setup
```bash
# Add Vast.ai secrets to Vercel
vercel secrets add vastai_api_key sk_live_***
vercel secrets add vastai_webhook_secret whsec_***

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
    "VASTAI_API_KEY": "@vastai_api_key"
  },
  "functions": {
    "api/**/*.ts": {
      "maxDuration": 30
    }
  }
}
```