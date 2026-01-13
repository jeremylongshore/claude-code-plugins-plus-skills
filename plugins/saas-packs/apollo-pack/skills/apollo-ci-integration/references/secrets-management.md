# Secrets Management

## Secrets Management

### GitHub Secrets Setup
```bash
# Add secrets via GitHub CLI
gh secret set APOLLO_API_KEY_TEST --body "your-test-api-key"
gh secret set APOLLO_API_KEY_PROD --body "your-prod-api-key"

# List configured secrets
gh secret list
```

### Environment-Based Secrets
```yaml
# .github/workflows/deploy.yml
jobs:
  deploy-staging:
    environment: staging
    steps:
      - name: Deploy to staging
        env:
          APOLLO_API_KEY: ${{ secrets.APOLLO_API_KEY }}
        run: npm run deploy:staging

  deploy-production:
    environment: production
    needs: deploy-staging
    steps:
      - name: Deploy to production
        env:
          APOLLO_API_KEY: ${{ secrets.APOLLO_API_KEY }}
        run: npm run deploy:production
```