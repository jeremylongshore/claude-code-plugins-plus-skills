# Vercel Deployment

## Vercel Deployment

### Environment Setup
```bash
# Add Clay secrets to Vercel
vercel secrets add clay_api_key sk_live_***
vercel secrets add clay_webhook_secret whsec_***

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
    "CLAY_API_KEY": "@clay_api_key"
  },
  "functions": {
    "api/**/*.ts": {
      "maxDuration": 30
    }
  }
}
```