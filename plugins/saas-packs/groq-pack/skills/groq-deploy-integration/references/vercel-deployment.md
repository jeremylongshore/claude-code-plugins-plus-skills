# Vercel Deployment

## Vercel Deployment

### Environment Setup
```bash
# Add Groq secrets to Vercel
vercel secrets add groq_api_key sk_live_***
vercel secrets add groq_webhook_secret whsec_***

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
    "GROQ_API_KEY": "@groq_api_key"
  },
  "functions": {
    "api/**/*.ts": {
      "maxDuration": 30
    }
  }
}
```