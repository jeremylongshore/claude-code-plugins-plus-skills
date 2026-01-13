# Deployment Topology

## Deployment Topology

```yaml
# kubernetes/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: juicebox-api
spec:
  replicas: 3
  template:
    spec:
      containers:
        - name: api
          resources:
            requests:
              memory: "256Mi"
              cpu: "250m"
            limits:
              memory: "512Mi"
              cpu: "500m"
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: juicebox-workers
spec:
  replicas: 2
  template:
    spec:
      containers:
        - name: worker
          resources:
            requests:
              memory: "512Mi"
              cpu: "500m"
```