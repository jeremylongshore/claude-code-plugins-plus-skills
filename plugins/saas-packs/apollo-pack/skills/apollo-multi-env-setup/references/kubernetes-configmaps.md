# Kubernetes Configmaps

## Kubernetes ConfigMaps

```yaml
# k8s/configmaps/apollo-config-dev.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: apollo-config
  namespace: development
data:
  NODE_ENV: "development"
  APOLLO_RATE_LIMIT: "10"
  APOLLO_CACHE_TTL: "60"
  APOLLO_LOG_LEVEL: "debug"
  APOLLO_FEATURES_SEARCH: "true"
  APOLLO_FEATURES_ENRICHMENT: "true"
  APOLLO_FEATURES_SEQUENCES: "false"
  APOLLO_FEATURES_WEBHOOKS: "false"
---
# k8s/configmaps/apollo-config-staging.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: apollo-config
  namespace: staging
data:
  NODE_ENV: "staging"
  APOLLO_RATE_LIMIT: "50"
  APOLLO_CACHE_TTL: "300"
  APOLLO_LOG_LEVEL: "info"
  APOLLO_FEATURES_SEARCH: "true"
  APOLLO_FEATURES_ENRICHMENT: "true"
  APOLLO_FEATURES_SEQUENCES: "true"
  APOLLO_FEATURES_WEBHOOKS: "true"
---
# k8s/configmaps/apollo-config-prod.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: apollo-config
  namespace: production
data:
  NODE_ENV: "production"
  APOLLO_RATE_LIMIT: "90"
  APOLLO_CACHE_TTL: "900"
  APOLLO_LOG_LEVEL: "warn"
  APOLLO_FEATURES_SEARCH: "true"
  APOLLO_FEATURES_ENRICHMENT: "true"
  APOLLO_FEATURES_SEQUENCES: "true"
  APOLLO_FEATURES_WEBHOOKS: "true"
```