# Examples

### Dockerfile
```dockerfile
# Dockerfile
FROM node:20-slim AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

# Production image
FROM node:20-slim AS runner

WORKDIR /app

ENV NODE_ENV=production

# Create non-root user
RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 deepgram
USER deepgram

COPY --from=builder --chown=deepgram:nodejs /app/dist ./dist
COPY --from=builder --chown=deepgram:nodejs /app/node_modules ./node_modules
COPY --from=builder --chown=deepgram:nodejs /app/package.json ./

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1

CMD ["node", "dist/index.js"]
```

### Docker Compose
```yaml
# docker-compose.yml
version: '3.8'

services:
  deepgram-service:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DEEPGRAM_API_KEY=${DEEPGRAM_API_KEY}
    secrets:
      - deepgram_key
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    deploy:
      replicas: 3
      resources:
        limits:
          cpus: '1'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 256M

  redis:
    image: redis:7-alpine
    volumes:
      - redis-data:/data

secrets:
  deepgram_key:
    file: ./secrets/deepgram-api-key.txt

volumes:
  redis-data:
```

### Kubernetes Deployment
```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: deepgram-service
  labels:
    app: deepgram-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: deepgram-service
  template:
    metadata:
      labels:
        app: deepgram-service
    spec:
      serviceAccountName: deepgram-service
      containers:
        - name: deepgram-service
          image: your-registry/deepgram-service:latest
          ports:
            - containerPort: 3000
          env:
            - name: NODE_ENV
              value: "production"
            - name: DEEPGRAM_API_KEY
              valueFrom:
                secretKeyRef:
                  name: deepgram-secrets
                  key: api-key
          resources:
            requests:
              memory: "256Mi"
              cpu: "250m"
            limits:
              memory: "512Mi"
              cpu: "500m"
          livenessProbe:
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /ready
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 5
          securityContext:
            runAsNonRoot: true
            runAsUser: 1001
            readOnlyRootFilesystem: true
---
apiVersion: v1
kind: Service
metadata:
  name: deepgram-service
spec:
  selector:
    app: deepgram-service
  ports:
    - port: 80
      targetPort: 3000
  type: ClusterIP
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: deepgram-service
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: deepgram-service
  minReplicas: 3
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

### Kubernetes Secret
```yaml
# k8s/secret.yaml (use sealed-secrets or external-secrets in production)
apiVersion: v1
kind: Secret
metadata:
  name: deepgram-secrets
type: Opaque
stringData:
  api-key: ${DEEPGRAM_API_KEY}
```

### AWS Lambda (Serverless)
```yaml
# serverless.yml
service: deepgram-transcription

provider:
  name: aws
  runtime: nodejs20.x
  stage: ${opt:stage, 'dev'}
  region: us-east-1
  memorySize: 512
  timeout: 30
  environment:
    NODE_ENV: production
  iam:
    role:
      statements:
        - Effect: Allow
          Action:
            - secretsmanager:GetSecretValue
          Resource:
            - arn:aws:secretsmanager:${self:provider.region}:*:secret:deepgram/*

functions:
  transcribe:
    handler: dist/handlers/transcribe.handler
    events:
      - http:
          path: /transcribe
          method: post
          cors: true
    environment:
      DEEPGRAM_SECRET_ARN: ${ssm:/deepgram/secret-arn}

  transcribeAsync:
    handler: dist/handlers/transcribe-async.handler
    events:
      - sqs:
          arn: !GetAtt TranscriptionQueue.Arn
    timeout: 300
    reservedConcurrency: 10

resources:
  Resources:
    TranscriptionQueue:
      Type: AWS::SQS::Queue
      Properties:
        QueueName: ${self:service}-transcription-queue
        VisibilityTimeout: 360
```

### Lambda Handler
```typescript
// src/handlers/transcribe.ts
import { APIGatewayProxyHandler } from 'aws-lambda';
import { SecretsManager } from '@aws-sdk/client-secrets-manager';
import { createClient } from '@deepgram/sdk';

const secretsManager = new SecretsManager({});
let deepgramKey: string | null = null;

async function getApiKey(): Promise<string> {
  if (deepgramKey) return deepgramKey;

  const { SecretString } = await secretsManager.getSecretValue({
    SecretId: process.env.DEEPGRAM_SECRET_ARN!,
  });

  deepgramKey = JSON.parse(SecretString!).apiKey;
  return deepgramKey!;
}

export const handler: APIGatewayProxyHandler = async (event) => {
  try {
    const body = JSON.parse(event.body || '{}');
    const { audioUrl, options = {} } = body;

    if (!audioUrl) {
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'audioUrl required' }),
      };
    }

    const apiKey = await getApiKey();
    const client = createClient(apiKey);

    const { result, error } = await client.listen.prerecorded.transcribeUrl(
      { url: audioUrl },
      { model: 'nova-2', smart_format: true, ...options }
    );

    if (error) {
      return {
        statusCode: 500,
        body: JSON.stringify({ error: error.message }),
      };
    }

    return {
      statusCode: 200,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        transcript: result.results.channels[0].alternatives[0].transcript,
        metadata: result.metadata,
      }),
    };
  } catch (err) {
    return {
      statusCode: 500,
      body: JSON.stringify({ error: 'Internal server error' }),
    };
  }
};
```

### Google Cloud Run
```yaml
# cloudbuild.yaml
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/deepgram-service:$COMMIT_SHA', '.']

  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/deepgram-service:$COMMIT_SHA']

  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk'
    entrypoint: gcloud
    args:
      - 'run'
      - 'deploy'
      - 'deepgram-service'
      - '--image=gcr.io/$PROJECT_ID/deepgram-service:$COMMIT_SHA'
      - '--region=us-central1'
      - '--platform=managed'
      - '--allow-unauthenticated'
      - '--set-secrets=DEEPGRAM_API_KEY=deepgram-api-key:latest'
      - '--memory=512Mi'
      - '--cpu=1'
      - '--min-instances=1'
      - '--max-instances=10'

images:
  - 'gcr.io/$PROJECT_ID/deepgram-service:$COMMIT_SHA'
```

### Vercel Deployment
```typescript
// api/transcribe.ts (Vercel Edge Function)
import { createClient } from '@deepgram/sdk';

export const config = {
  runtime: 'edge',
};

export default async function handler(request: Request) {
  if (request.method !== 'POST') {
    return new Response('Method not allowed', { status: 405 });
  }

  try {
    const { audioUrl } = await request.json();

    const client = createClient(process.env.DEEPGRAM_API_KEY!);

    const { result, error } = await client.listen.prerecorded.transcribeUrl(
      { url: audioUrl },
      { model: 'nova-2', smart_format: true }
    );

    if (error) {
      return new Response(JSON.stringify({ error: error.message }), {
        status: 500,
        headers: { 'Content-Type': 'application/json' },
      });
    }

    return new Response(
      JSON.stringify({
        transcript: result.results.channels[0].alternatives[0].transcript,
      }),
      { headers: { 'Content-Type': 'application/json' } }
    );
  } catch (err) {
    return new Response(JSON.stringify({ error: 'Internal error' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    });
  }
}
```

### Deploy Script
```bash
#!/bin/bash
# scripts/deploy.sh

set -e

ENVIRONMENT=$1

if [ -z "$ENVIRONMENT" ]; then
  echo "Usage: ./deploy.sh <staging|production>"
  exit 1
fi

echo "Deploying to $ENVIRONMENT..."

# Build
npm run build

# Run tests
npm test

# Deploy based on environment
case $ENVIRONMENT in
  staging)
    kubectl apply -f k8s/staging/
    kubectl rollout status deployment/deepgram-service -n staging
    ;;
  production)
    kubectl apply -f k8s/production/
    kubectl rollout status deployment/deepgram-service -n production
    ;;
  *)
    echo "Unknown environment: $ENVIRONMENT"
    exit 1
    ;;
esac

# Run smoke tests
npm run smoke-test

echo "Deployment complete!"
```