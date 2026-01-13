# Examples

### Local Testing
```bash
# Build locally
docker build -t langchain-api .

# Run with env file
docker run -p 8080:8080 --env-file .env langchain-api

# Test endpoint
curl -X POST http://localhost:8080/chat \
    -H "Content-Type: application/json" \
    -d '{"input": "Hello!"}'
```

### AWS Deployment (ECS)
```bash
# Create ECR repository
aws ecr create-repository --repository-name langchain-api

# Push image
docker tag langchain-api:latest ACCOUNT.dkr.ecr.REGION.amazonaws.com/langchain-api:latest
docker push ACCOUNT.dkr.ecr.REGION.amazonaws.com/langchain-api:latest

# Deploy with Copilot
copilot deploy
```