# Deployment Platforms

## Deployment Platforms

### Vercel Deployment
```json
// vercel.json
{
  "env": {
    "APOLLO_API_KEY": "@apollo-api-key"
  },
  "build": {
    "env": {
      "APOLLO_API_KEY": "@apollo-api-key"
    }
  }
}
```

```bash
# Add secret to Vercel
vercel secrets add apollo-api-key "your-api-key"

# Deploy
vercel --prod
```

### Google Cloud Run
```yaml
# cloudbuild.yaml
steps:
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/apollo-service', '.']

  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/apollo-service']

  - name: 'gcr.io/cloud-builders/gcloud'
    args:
      - 'run'
      - 'deploy'
      - 'apollo-service'
      - '--image=gcr.io/$PROJECT_ID/apollo-service'
      - '--platform=managed'
      - '--region=us-central1'
      - '--set-secrets=APOLLO_API_KEY=apollo-api-key:latest'
      - '--allow-unauthenticated'
```

```bash
# Create secret in Google Cloud
gcloud secrets create apollo-api-key --data-file=-
echo -n "your-api-key" | gcloud secrets versions add apollo-api-key --data-file=-

# Grant access to Cloud Run
gcloud secrets add-iam-policy-binding apollo-api-key \
  --member="serviceAccount:YOUR-SA@PROJECT.iam.gserviceaccount.com" \
  --role="roles/secretmanager.secretAccessor"
```

### AWS Lambda
```yaml
# serverless.yml
service: apollo-integration

provider:
  name: aws
  runtime: nodejs20.x
  region: us-east-1
  environment:
    APOLLO_API_KEY: ${ssm:/apollo/api-key~true}

functions:
  search:
    handler: src/handlers/search.handler
    events:
      - http:
          path: /api/apollo/search
          method: post
    timeout: 30

  enrich:
    handler: src/handlers/enrich.handler
    events:
      - http:
          path: /api/apollo/enrich
          method: get
    timeout: 30
```

```bash
# Store secret in SSM
aws ssm put-parameter \
  --name "/apollo/api-key" \
  --type "SecureString" \
  --value "your-api-key"

# Deploy
serverless deploy --stage production
```

### Kubernetes
```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: apollo-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: apollo-service
  template:
    metadata:
      labels:
        app: apollo-service
    spec:
      containers:
        - name: apollo-service
          image: your-registry/apollo-service:latest
          ports:
            - containerPort: 3000
          env:
            - name: APOLLO_API_KEY
              valueFrom:
                secretKeyRef:
                  name: apollo-secrets
                  key: api-key
          livenessProbe:
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 10
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /health/apollo
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 5
          resources:
            requests:
              memory: "256Mi"
              cpu: "100m"
            limits:
              memory: "512Mi"
              cpu: "500m"
---
apiVersion: v1
kind: Secret
metadata:
  name: apollo-secrets
type: Opaque
stringData:
  api-key: your-api-key  # Use sealed-secrets in production
```