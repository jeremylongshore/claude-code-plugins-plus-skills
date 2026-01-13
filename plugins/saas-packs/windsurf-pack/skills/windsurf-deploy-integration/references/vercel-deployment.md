# Vercel Deployment

## Vercel Deployment

### Environment Setup
```bash
# Add Windsurf secrets to Vercel
vercel secrets add windsurf_api_key sk_live_***
vercel secrets add windsurf_webhook_secret whsec_***

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
    "WINDSURF_API_KEY": "@windsurf_api_key"
  },
  "functions": {
    "api/**/*.ts": {
      "maxDuration": 30
    }
  }
}
```