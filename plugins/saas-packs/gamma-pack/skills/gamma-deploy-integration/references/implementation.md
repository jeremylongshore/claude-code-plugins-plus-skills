# Implementation Guide

### Vercel Deployment

#### Step 1: Configure Vercel Project
```bash
# Install Vercel CLI
npm i -g vercel

# Link project
vercel link

# Set environment variable
vercel env add GAMMA_API_KEY production
```

#### Step 2: Create vercel.json
```json
{
  "framework": "nextjs",
  "buildCommand": "npm run build",
  "env": {
    "GAMMA_API_KEY": "@gamma_api_key"
  },
  "functions": {
    "api/**/*.ts": {
      "maxDuration": 30
    }
  }
}
```

#### Step 3: Deploy
```bash
# Preview deployment
vercel

# Production deployment
vercel --prod
```

### AWS Lambda Deployment

#### Step 1: Store Secret in AWS Secrets Manager
```bash
aws secretsmanager create-secret \
  --name gamma/api-key \
  --secret-string '{"apiKey":"your-gamma-api-key"}'
```

#### Step 2: Lambda Configuration
```typescript
// lambda/gamma-handler.ts
import { SecretsManager } from '@aws-sdk/client-secrets-manager';
import { GammaClient } from '@gamma/sdk';

const secretsManager = new SecretsManager({ region: 'us-east-1' });
let gamma: GammaClient;

async function getGammaClient() {
  if (!gamma) {
    const secret = await secretsManager.getSecretValue({
      SecretId: 'gamma/api-key',
    });
    const { apiKey } = JSON.parse(secret.SecretString!);
    gamma = new GammaClient({ apiKey });
  }
  return gamma;
}

export async function handler(event: any) {
  const client = await getGammaClient();
  const result = await client.presentations.create({
    title: event.title,
    prompt: event.prompt,
  });
  return { statusCode: 200, body: JSON.stringify(result) };
}
```

#### Step 3: SAM Template
```yaml
# template.yaml
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31

Resources:
  GammaFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: dist/gamma-handler.handler
      Runtime: nodejs20.x
      Timeout: 30
      MemorySize: 256
      Policies:
        - SecretsManagerReadWrite
      Environment:
        Variables:
          NODE_ENV: production
```

### Google Cloud Run Deployment

#### Step 1: Store Secret
```bash
echo -n "your-gamma-api-key" | \
  gcloud secrets create gamma-api-key --data-file=-
```

#### Step 2: Dockerfile
```dockerfile
FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY dist ./dist
CMD ["node", "dist/server.js"]
```

#### Step 3: Deploy
```bash
gcloud run deploy gamma-service \
  --image gcr.io/$PROJECT_ID/gamma-service \
  --platform managed \
  --region us-central1 \
  --set-secrets GAMMA_API_KEY=gamma-api-key:latest \
  --allow-unauthenticated
```

### GitHub Actions Deployment
```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build
        run: npm ci && npm run build

      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: '--prod'
```