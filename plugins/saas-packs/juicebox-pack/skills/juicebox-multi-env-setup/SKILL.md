---
name: juicebox-multi-env-setup
description: |
  Configure Juicebox multi-environment setup.
  Use when setting up dev/staging/production environments,
  managing per-environment configurations, or implementing environment isolation.
  Trigger with phrases like "juicebox environments", "juicebox staging",
  "juicebox dev prod", "juicebox environment setup".
allowed-tools: Read, Write, Edit, Bash
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Juicebox Multi-Environment Setup

## Overview
Configure Juicebox across development, staging, and production environments with proper isolation and security.

## Prerequisites
- Separate Juicebox accounts or API keys per environment
- Secret management solution (Vault, AWS Secrets Manager, etc.)
- CI/CD pipeline with environment variables
- Environment detection in application

## Environment Strategy

| Environment | Purpose | API Key | Rate Limits | Data |
|-------------|---------|---------|-------------|------|
| Development | Local dev | Sandbox | Relaxed | Mock/Test |
| Staging | Pre-prod testing | Test | Production | Subset |
| Production | Live system | Production | Full | Real |

## Instructions

### Step 1: Environment Configuration
```typescript
// config/environments.ts
interface JuiceboxEnvConfig {
  apiKey: string;
  baseUrl: string;
  timeout: number;
  retries: number;
  sandbox: boolean;
}

const configs: Record<string, JuiceboxEnvConfig> = {
  development: {
    apiKey: process.env.JUICEBOX_API_KEY_DEV!,
    baseUrl: 'https://sandbox.api.juicebox.ai',
    timeout: 30000,
    retries: 1,
    sandbox: true
  },
  staging: {
    apiKey: process.env.JUICEBOX_API_KEY_STAGING!,
    baseUrl: 'https://api.juicebox.ai',
    timeout: 30000,
    retries: 2,
    sandbox: false
  },
  production: {
    apiKey: process.env.JUICEBOX_API_KEY_PROD!,
    baseUrl: 'https://api.juicebox.ai',
    timeout: 60000,
    retries: 3,
    sandbox: false
  }
};

export function getConfig(): JuiceboxEnvConfig {
  const env = process.env.NODE_ENV || 'development';
  const config = configs[env];

  if (!config) {
    throw new Error(`Unknown environment: ${env}`);
  }

  if (!config.apiKey) {
    throw new Error(`JUICEBOX_API_KEY not set for ${env}`);
  }

  return config;
}
```

### Step 2: Secret Management by Environment
```typescript
// lib/secrets.ts
import { SecretsManager } from '@aws-sdk/client-secrets-manager';

const secretPaths: Record<string, string> = {
  development: 'juicebox/dev/api-key',
  staging: 'juicebox/staging/api-key',
  production: 'juicebox/prod/api-key'
};

export async function getApiKey(): Promise<string> {
  const env = process.env.NODE_ENV || 'development';

  // In development, allow env var fallback
  if (env === 'development' && process.env.JUICEBOX_API_KEY_DEV) {
    return process.env.JUICEBOX_API_KEY_DEV;
  }

  // Production environments must use secret manager
  const client = new SecretsManager({ region: process.env.AWS_REGION });
  const result = await client.getSecretValue({
    SecretId: secretPaths[env]
  });

  return JSON.parse(result.SecretString!).apiKey;
}
```

### Step 3: Environment-Aware Client Factory
```typescript
// lib/client-factory.ts
import { JuiceboxClient } from '@juicebox/sdk';
import { getConfig } from '../config/environments';
import { getApiKey } from './secrets';

let clientInstance: JuiceboxClient | null = null;

export async function getJuiceboxClient(): Promise<JuiceboxClient> {
  if (clientInstance) return clientInstance;

  const config = getConfig();
  const apiKey = await getApiKey();

  clientInstance = new JuiceboxClient({
    apiKey,
    baseUrl: config.baseUrl,
    timeout: config.timeout,
    retries: config.retries
  });

  // Add environment-specific middleware
  if (process.env.NODE_ENV === 'development') {
    clientInstance.use(logRequestsMiddleware);
  }

  return clientInstance;
}
```

### Step 4: Kubernetes ConfigMaps
```yaml
# k8s/base/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: juicebox-config
data:
  JUICEBOX_TIMEOUT: "30000"
  JUICEBOX_RETRIES: "3"

---
# k8s/overlays/development/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: juicebox-config
data:
  JUICEBOX_BASE_URL: "https://sandbox.api.juicebox.ai"
  JUICEBOX_SANDBOX: "true"

---
# k8s/overlays/staging/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: juicebox-config
data:
  JUICEBOX_BASE_URL: "https://api.juicebox.ai"
  JUICEBOX_SANDBOX: "false"

---
# k8s/overlays/production/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: juicebox-config
data:
  JUICEBOX_BASE_URL: "https://api.juicebox.ai"
  JUICEBOX_SANDBOX: "false"
  JUICEBOX_TIMEOUT: "60000"
```

### Step 5: Environment Guards
```typescript
// lib/environment-guards.ts
export function requireProduction(): void {
  if (process.env.NODE_ENV !== 'production') {
    throw new Error('This operation is only allowed in production');
  }
}

export function preventProduction(): void {
  if (process.env.NODE_ENV === 'production') {
    throw new Error('This operation is not allowed in production');
  }
}

// Usage
async function resetTestData(): Promise<void> {
  preventProduction();
  await db.profiles.deleteMany({});
}

async function sendBulkOutreach(): Promise<void> {
  requireProduction();
  // ... production-only logic
}
```

## Environment Checklist

```markdown
## Environment Setup Verification

### Development
- [ ] Sandbox API key configured
- [ ] Mock data available
- [ ] Debug logging enabled
- [ ] Rate limits relaxed

### Staging
- [ ] Test API key configured
- [ ] Production-like data subset
- [ ] Monitoring enabled
- [ ] Matches production config

### Production
- [ ] Production API key in secret manager
- [ ] All guards enabled
- [ ] Monitoring and alerting
- [ ] Backup and recovery tested
```

## Output
- Environment-specific configurations
- Secret management per environment
- Kubernetes overlays
- Environment guards

## Resources
- [Multi-Environment Guide](https://juicebox.ai/docs/environments)
- [12-Factor App Config](https://12factor.net/config)

## Next Steps
After environment setup, see `juicebox-observability` for monitoring.
