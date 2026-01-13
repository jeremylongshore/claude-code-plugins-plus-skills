# Blue-Green Deployment

## Blue-Green Deployment

```yaml
# .github/workflows/blue-green.yml
name: Blue-Green Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Deploy to Green
        run: |
          kubectl apply -f k8s/deployment-green.yaml
          kubectl rollout status deployment/apollo-service-green

      - name: Run smoke tests on Green
        run: |
          GREEN_URL=$(kubectl get svc apollo-service-green -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
          curl -sf "http://$GREEN_URL/health/apollo" || exit 1

      - name: Switch traffic to Green
        if: success()
        run: |
          kubectl patch service apollo-service -p '{"spec":{"selector":{"version":"green"}}}'

      - name: Rollback on failure
        if: failure()
        run: |
          kubectl patch service apollo-service -p '{"spec":{"selector":{"version":"blue"}}}'
```