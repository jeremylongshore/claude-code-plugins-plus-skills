# Secrets Management

## Secrets Management

```yaml
# k8s/secrets/apollo-secrets.yaml (use sealed-secrets in practice)
apiVersion: v1
kind: Secret
metadata:
  name: apollo-secrets
  namespace: ${NAMESPACE}
type: Opaque
stringData:
  api-key: ${APOLLO_API_KEY}
  webhook-secret: ${APOLLO_WEBHOOK_SECRET}
```

```bash
# Using External Secrets Operator
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: apollo-secrets
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: gcp-secret-manager
    kind: ClusterSecretStore
  target:
    name: apollo-secrets
  data:
    - secretKey: api-key
      remoteRef:
        key: apollo-api-key-${ENV}
    - secretKey: webhook-secret
      remoteRef:
        key: apollo-webhook-secret-${ENV}
```