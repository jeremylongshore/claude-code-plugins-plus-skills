# Vercel Deployment

## Vercel Deployment

### Environment Setup
```bash
# Add Retell AI secrets to Vercel
vercel secrets add retellai_api_key sk_live_***
vercel secrets add retellai_webhook_secret whsec_***

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
    "RETELLAI_API_KEY": "@retellai_api_key"
  },
  "functions": {
    "api/**/*.ts": {
      "maxDuration": 30
    }
  }
}
```