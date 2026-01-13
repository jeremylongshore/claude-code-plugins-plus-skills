# Vercel Deployment

## Vercel Deployment

### Environment Setup
```bash
# Add Exa secrets to Vercel
vercel secrets add exa_api_key sk_live_***
vercel secrets add exa_webhook_secret whsec_***

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
    "EXA_API_KEY": "@exa_api_key"
  },
  "functions": {
    "api/**/*.ts": {
      "maxDuration": 30
    }
  }
}
```