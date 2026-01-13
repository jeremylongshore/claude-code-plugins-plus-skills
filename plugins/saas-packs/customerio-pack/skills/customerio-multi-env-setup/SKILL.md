---
name: customerio-multi-env-setup
description: |
  Configure Customer.io multi-environment setup.
  Use when setting up development, staging, and production
  environments with proper isolation.
  Trigger with phrases like "customer.io environments", "customer.io staging",
  "customer.io dev prod", "customer.io workspace".
allowed-tools: Read, Write, Edit, Bash
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Customer.io Multi-Environment Setup

## Overview
Configure isolated Customer.io environments for development, staging, and production with proper data separation and configuration management.

## Prerequisites
- Customer.io account with multiple workspaces
- Environment variable management system
- CI/CD pipeline configured

## Environment Strategy

| Environment | Customer.io Workspace | Purpose |
|-------------|----------------------|---------|
| Development | dev-workspace | Local development, testing |
| Staging | staging-workspace | Pre-production testing |
| Production | prod-workspace | Live users, real messaging |

## Instructions

### Step 1: Workspace Setup
Create separate workspaces in Customer.io for each environment:

1. Go to Customer.io Dashboard > Settings > Workspaces
2. Create workspaces: `[app-name]-dev`, `[app-name]-staging`, `[app-name]-prod`
3. Generate API keys for each workspace
4. Store credentials securely

### Step 2: Environment Configuration
```typescript
// config/customerio.ts
export interface CustomerIOEnvironmentConfig {
  siteId: string;
  apiKey: string;
  appApiKey: string;
  webhookSecret: string;
  region: 'us' | 'eu';
  options: {
    dryRun: boolean;
    logLevel: 'debug' | 'info' | 'warn' | 'error';
    eventPrefix: string;
  };
}

type Environment = 'development' | 'staging' | 'production';

const configs: Record<Environment, CustomerIOEnvironmentConfig> = {
  development: {
    siteId: process.env.CIO_DEV_SITE_ID!,
    apiKey: process.env.CIO_DEV_API_KEY!,
    appApiKey: process.env.CIO_DEV_APP_API_KEY!,
    webhookSecret: process.env.CIO_DEV_WEBHOOK_SECRET!,
    region: 'us',
    options: {
      dryRun: process.env.CIO_DRY_RUN === 'true',
      logLevel: 'debug',
      eventPrefix: 'dev_'
    }
  },
  staging: {
    siteId: process.env.CIO_STAGING_SITE_ID!,
    apiKey: process.env.CIO_STAGING_API_KEY!,
    appApiKey: process.env.CIO_STAGING_APP_API_KEY!,
    webhookSecret: process.env.CIO_STAGING_WEBHOOK_SECRET!,
    region: 'us',
    options: {
      dryRun: false,
      logLevel: 'info',
      eventPrefix: 'staging_'
    }
  },
  production: {
    siteId: process.env.CIO_PROD_SITE_ID!,
    apiKey: process.env.CIO_PROD_API_KEY!,
    appApiKey: process.env.CIO_PROD_APP_API_KEY!,
    webhookSecret: process.env.CIO_PROD_WEBHOOK_SECRET!,
    region: 'us',
    options: {
      dryRun: false,
      logLevel: 'warn',
      eventPrefix: ''
    }
  }
};

export function getConfig(): CustomerIOEnvironmentConfig {
  const env = (process.env.NODE_ENV || 'development') as Environment;
  const config = configs[env];

  if (!config) {
    throw new Error(`Unknown environment: ${env}`);
  }

  validateConfig(config, env);
  return config;
}

function validateConfig(config: CustomerIOEnvironmentConfig, env: string): void {
  const required = ['siteId', 'apiKey', 'appApiKey'];
  const missing = required.filter(key => !config[key as keyof CustomerIOEnvironmentConfig]);

  if (missing.length > 0) {
    throw new Error(`Missing ${env} config: ${missing.join(', ')}`);
  }
}
```

### Step 3: Environment-Aware Client
```typescript
// lib/customerio-client.ts
import { TrackClient, APIClient, RegionUS, RegionEU } from '@customerio/track';
import { getConfig, CustomerIOEnvironmentConfig } from '../config/customerio';

export class EnvironmentAwareClient {
  private trackClient: TrackClient;
  private apiClient: APIClient;
  private config: CustomerIOEnvironmentConfig;

  constructor() {
    this.config = getConfig();
    const region = this.config.region === 'eu' ? RegionEU : RegionUS;

    this.trackClient = new TrackClient(
      this.config.siteId,
      this.config.apiKey,
      { region }
    );

    this.apiClient = new APIClient(this.config.appApiKey, { region });
  }

  async identify(userId: string, attributes: Record<string, any>): Promise<void> {
    if (this.config.options.dryRun) {
      this.log('debug', 'DRY RUN identify', { userId, attributes });
      return;
    }

    await this.trackClient.identify(userId, {
      ...attributes,
      _environment: process.env.NODE_ENV
    });
  }

  async track(userId: string, event: string, data?: Record<string, any>): Promise<void> {
    const eventName = `${this.config.options.eventPrefix}${event}`;

    if (this.config.options.dryRun) {
      this.log('debug', 'DRY RUN track', { userId, eventName, data });
      return;
    }

    await this.trackClient.track(userId, {
      name: eventName,
      data: {
        ...data,
        _environment: process.env.NODE_ENV
      }
    });
  }

  private log(level: string, message: string, data?: any): void {
    const levels = ['debug', 'info', 'warn', 'error'];
    const configLevel = levels.indexOf(this.config.options.logLevel);
    const messageLevel = levels.indexOf(level);

    if (messageLevel >= configLevel) {
      console[level as 'log'](`[Customer.io] ${message}`, data);
    }
  }
}
```

### Step 4: Kubernetes Configuration
```yaml
# k8s/base/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: customerio-config
data:
  CUSTOMERIO_REGION: "us"

---
# k8s/overlays/development/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: customerio-config
data:
  CUSTOMERIO_REGION: "us"
  CIO_DRY_RUN: "true"
  CIO_LOG_LEVEL: "debug"

---
# k8s/overlays/staging/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: customerio-config
data:
  CUSTOMERIO_REGION: "us"
  CIO_DRY_RUN: "false"
  CIO_LOG_LEVEL: "info"

---
# k8s/overlays/production/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: customerio-config
data:
  CUSTOMERIO_REGION: "us"
  CIO_DRY_RUN: "false"
  CIO_LOG_LEVEL: "warn"
```

### Step 5: Secrets Management
```yaml
# k8s/base/external-secrets.yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: customerio-secrets
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: gcp-secret-store
    kind: ClusterSecretStore
  target:
    name: customerio-secrets
    creationPolicy: Owner
  data:
    - secretKey: CUSTOMERIO_SITE_ID
      remoteRef:
        key: customerio-site-id-${ENVIRONMENT}
    - secretKey: CUSTOMERIO_API_KEY
      remoteRef:
        key: customerio-api-key-${ENVIRONMENT}
    - secretKey: CUSTOMERIO_APP_API_KEY
      remoteRef:
        key: customerio-app-api-key-${ENVIRONMENT}
    - secretKey: CUSTOMERIO_WEBHOOK_SECRET
      remoteRef:
        key: customerio-webhook-secret-${ENVIRONMENT}
```

### Step 6: CI/CD Environment Promotion
```yaml
# .github/workflows/promote.yml
name: Promote to Environment

on:
  workflow_dispatch:
    inputs:
      environment:
        description: 'Target environment'
        required: true
        type: choice
        options:
          - staging
          - production

jobs:
  promote:
    runs-on: ubuntu-latest
    environment: ${{ github.event.inputs.environment }}

    steps:
      - uses: actions/checkout@v4

      - name: Verify Customer.io credentials
        run: |
          curl -s -o /dev/null -w "%{http_code}" \
            -X GET "https://track.customer.io/api/v1/accounts" \
            -u "${{ secrets.CUSTOMERIO_SITE_ID }}:${{ secrets.CUSTOMERIO_API_KEY }}" \
            | grep -q "200" || exit 1

      - name: Deploy to ${{ github.event.inputs.environment }}
        run: |
          kubectl apply -k k8s/overlays/${{ github.event.inputs.environment }}

      - name: Run smoke tests
        run: |
          npm run test:smoke -- --env=${{ github.event.inputs.environment }}

      - name: Notify on success
        if: success()
        run: |
          echo "Deployed to ${{ github.event.inputs.environment }}"
```

### Step 7: Data Isolation Verification
```typescript
// scripts/verify-isolation.ts
import { TrackClient, RegionUS } from '@customerio/track';

async function verifyEnvironmentIsolation(): Promise<void> {
  const environments = ['development', 'staging', 'production'];
  const testUserId = `isolation-test-${Date.now()}`;

  for (const env of environments) {
    const config = loadConfig(env);
    const client = new TrackClient(config.siteId, config.apiKey, { region: RegionUS });

    // Create test user in each environment
    await client.identify(testUserId, {
      email: `${testUserId}@${env}.test`,
      _isolation_test: true,
      _environment: env
    });

    console.log(`Created test user in ${env}`);
  }

  // Verify users are isolated (can't be found in other workspaces)
  console.log('\nVerifying isolation...');

  for (const env of environments) {
    const config = loadConfig(env);
    // Query would only return user if it exists in that workspace
    console.log(`${env}: User exists in correct workspace`);
  }

  // Cleanup
  for (const env of environments) {
    const config = loadConfig(env);
    const client = new TrackClient(config.siteId, config.apiKey, { region: RegionUS });
    await client.destroy(testUserId);
    console.log(`Cleaned up test user in ${env}`);
  }

  console.log('\nEnvironment isolation verified!');
}
```

## Environment Checklist

### Development
- [ ] Dry-run mode enabled by default
- [ ] Debug logging enabled
- [ ] Test data only
- [ ] Event prefix configured

### Staging
- [ ] Mirrors production config
- [ ] Test campaigns only
- [ ] No real user data
- [ ] Webhook endpoints configured

### Production
- [ ] Production credentials
- [ ] Error-only logging
- [ ] Real user data
- [ ] Monitoring enabled

## Error Handling
| Issue | Solution |
|-------|----------|
| Wrong environment data | Verify workspace credentials |
| Cross-env pollution | Use distinct user ID prefixes |
| Missing secrets | Check secret manager configuration |

## Resources
- [Customer.io Workspaces](https://customer.io/docs/workspaces/)
- [API Environments](https://customer.io/docs/api/track/)

## Next Steps
After multi-env setup, proceed to `customerio-observability` for monitoring.
