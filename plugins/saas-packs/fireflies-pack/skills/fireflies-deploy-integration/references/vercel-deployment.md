# Vercel Deployment

## Vercel Deployment

### Environment Setup
```bash
# Add Fireflies.ai secrets to Vercel
vercel secrets add fireflies_api_key sk_live_***
vercel secrets add fireflies_webhook_secret whsec_***

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
    "FIREFLIES_API_KEY": "@fireflies_api_key"
  },
  "functions": {
    "api/**/*.ts": {
      "maxDuration": 30
    }
  }
}
```