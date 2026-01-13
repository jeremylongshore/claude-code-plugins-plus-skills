# Vercel Deployment

## Vercel Deployment

### Environment Setup
```bash
# Add PostHog secrets to Vercel
vercel secrets add posthog_api_key sk_live_***
vercel secrets add posthog_webhook_secret whsec_***

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
    "POSTHOG_API_KEY": "@posthog_api_key"
  },
  "functions": {
    "api/**/*.ts": {
      "maxDuration": 30
    }
  }
}
```