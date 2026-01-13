# Vercel Deployment

## Vercel Deployment

### Environment Setup
```bash
# Add Ideogram secrets to Vercel
vercel secrets add ideogram_api_key sk_live_***
vercel secrets add ideogram_webhook_secret whsec_***

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
    "IDEOGRAM_API_KEY": "@ideogram_api_key"
  },
  "functions": {
    "api/**/*.ts": {
      "maxDuration": 30
    }
  }
}
```