# Examples

### Running Different Environments
```bash
# Development
ENVIRONMENT=development python main.py

# Staging
ENVIRONMENT=staging python main.py

# Production
ENVIRONMENT=production python main.py
```

### Environment Promotion Workflow
```bash
# 1. Test in development
ENVIRONMENT=development pytest tests/

# 2. Deploy to staging
gcloud run deploy langchain-api-staging \
    --set-env-vars="ENVIRONMENT=staging"

# 3. Run integration tests
ENVIRONMENT=staging pytest tests/integration/

# 4. Deploy to production
gcloud run deploy langchain-api \
    --set-env-vars="ENVIRONMENT=production"
```