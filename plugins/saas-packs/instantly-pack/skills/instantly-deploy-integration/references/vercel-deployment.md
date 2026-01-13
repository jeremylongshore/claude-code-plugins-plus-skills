# Vercel Deployment

## Vercel Deployment

### Environment Setup
```bash
# Add Instantly secrets to Vercel
vercel secrets add instantly_api_key sk_live_***
vercel secrets add instantly_webhook_secret whsec_***

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
    "INSTANTLY_API_KEY": "@instantly_api_key"
  },
  "functions": {
    "api/**/*.ts": {
      "maxDuration": 30
    }
  }
}
```