# Vercel Deployment

## Vercel Deployment

### Environment Setup
```bash
# Add Replit secrets to Vercel
vercel secrets add replit_api_key sk_live_***
vercel secrets add replit_webhook_secret whsec_***

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
    "REPLIT_API_KEY": "@replit_api_key"
  },
  "functions": {
    "api/**/*.ts": {
      "maxDuration": 30
    }
  }
}
```