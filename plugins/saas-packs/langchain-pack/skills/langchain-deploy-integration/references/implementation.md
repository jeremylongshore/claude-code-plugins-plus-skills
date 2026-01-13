# Implementation Guide

### Step 1: Create Dockerfile
```dockerfile
# Dockerfile
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Production stage
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy application code
COPY src/ ./src/
COPY main.py .

# Create non-root user
RUN useradd --create-home appuser
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8080/health')"

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
```

### Step 2: Create FastAPI Application
```python
# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import asynccontextmanager
import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Initialize LLM on startup
llm = None
chain = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global llm, chain
    # Startup
    llm = ChatOpenAI(
        model=os.environ.get("MODEL_NAME", "gpt-4o-mini"),
        max_retries=3
    )
    prompt = ChatPromptTemplate.from_template("{input}")
    chain = prompt | llm | StrOutputParser()
    yield
    # Shutdown
    pass

app = FastAPI(lifespan=lifespan)

class ChatRequest(BaseModel):
    input: str
    max_tokens: int = 1000

class ChatResponse(BaseModel):
    response: str

@app.get("/health")
async def health():
    return {"status": "healthy", "model": os.environ.get("MODEL_NAME")}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = await chain.ainvoke({"input": request.input})
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

### Step 3: Deploy to Google Cloud Run
```bash
# Build and push container
gcloud builds submit --tag gcr.io/PROJECT_ID/langchain-api

# Deploy to Cloud Run
gcloud run deploy langchain-api \
    --image gcr.io/PROJECT_ID/langchain-api \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --set-secrets=OPENAI_API_KEY=openai-api-key:latest \
    --memory 1Gi \
    --cpu 2 \
    --min-instances 1 \
    --max-instances 10 \
    --concurrency 80
```

### Step 4: Kubernetes Deployment
```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: langchain-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: langchain-api
  template:
    metadata:
      labels:
        app: langchain-api
    spec:
      containers:
      - name: langchain-api
        image: gcr.io/PROJECT_ID/langchain-api:latest
        ports:
        - containerPort: 8080
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: langchain-secrets
              key: openai-api-key
        - name: MODEL_NAME
          value: "gpt-4o-mini"
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 10
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 15
          periodSeconds: 20
---
apiVersion: v1
kind: Service
metadata:
  name: langchain-api
spec:
  selector:
    app: langchain-api
  ports:
  - port: 80
    targetPort: 8080
  type: LoadBalancer
```

### Step 5: Configure Autoscaling
```yaml
# k8s/hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: langchain-api-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: langchain-api
  minReplicas: 2
  maxReplicas: 20
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```