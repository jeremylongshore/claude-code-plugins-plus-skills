---
name: linear-multi-env-setup
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Configure Linear across development, staging, and production environments.
  Use when setting up multi-environment deployments, managing per-environment API
  keys, or implementing environment-specific Linear configurations. Trigger with phrases
  like ...
---
# Linear Multi-Environment Setup

## Overview
Configure Linear integrations across development, staging, and production environments.

## Prerequisites
- Separate Linear workspaces or API keys per environment
- Secret management solution (Vault, AWS Secrets Manager, GCP Secret Manager)
- CI/CD pipeline with environment variables
- Environment detection in application

## Instructions

### Step 1: Environment Configuration Structure
```typescript
// config/environments.ts
interface LinearEnvironmentConfig {
  apiKey: string;
  webhookSecret: string;
  defaultTeamKey: string;
  features: {
    syncEnabled: boolean;
    webhooksEnabled: boolean;
    debugMode: boolean;
  };
}

interface EnvironmentConfigs {
  development: LinearEnvironmentConfig;
  staging: LinearEnvironmentConfig;
  production: LinearEnvironmentConfig;
}

const configs: EnvironmentConfigs = {
  development: {
    apiKey: process.env.LINEAR_API_KEY_DEV!,
    webhookSecret: process.env.LINEAR_WEBHOOK_SECRET_DEV!,
    defaultTeamKey: "DEV",
    features: {
      syncEnabled: true,
      webhooksEnabled: false, // Use polling in dev
      debugMode: true,
    },
  },
  staging: {
    apiKey: process.env.LINEAR_API_KEY_STAGING!,
    webhookSecret: process.env.LINEAR_WEBHOOK_SECRET_STAGING!,
    defaultTeamKey: "STG",
    features: {
      syncEnabled: true,
      webhooksEnabled: true,
      debugMode: true,
    },
  },
  production: {
    apiKey: process.env.LINEAR_API_KEY_PROD!,
    webhookSecret: process.env.LINEAR_WEBHOOK_SECRET_PROD!,
    defaultTeamKey: "PROD",
    features: {
      syncEnabled: true,
      webhooksEnabled: true,
      debugMode: false,
    },
  },
};

export function getConfig(): LinearEnvironmentConfig {
  const env = process.env.NODE_ENV || "development";
  return configs[env as keyof EnvironmentConfigs];
}
```

### Step 2: Secret Management

**HashiCorp Vault:**
```typescript
// config/vault.ts
import Vault from "node-vault";

const vault = Vault({
  endpoint: process.env.VAULT_ADDR,
  token: process.env.VAULT_TOKEN,
});

export async function getLinearSecrets(environment: string) {
  const path = `secret/data/linear/${environment}`;
  const { data } = await vault.read(path);

  return {
    apiKey: data.data.api_key,
    webhookSecret: data.data.webhook_secret,
  };
}
```

**AWS Secrets Manager:**
```typescript
// config/aws-secrets.ts
import { SecretsManagerClient, GetSecretValueCommand } from "@aws-sdk/client-secrets-manager";

const client = new SecretsManagerClient({ region: "us-east-1" });

export async function getLinearSecrets(environment: string) {
  const command = new GetSecretValueCommand({
    SecretId: `linear/${environment}`,
  });

  const response = await client.send(command);
  return JSON.parse(response.SecretString!);
}
```

**GCP Secret Manager:**
```typescript
// config/gcp-secrets.ts
import { SecretManagerServiceClient } from "@google-cloud/secret-manager";

const client = new SecretManagerServiceClient();

export async function getLinearSecrets(environment: string) {
  const projectId = process.env.GCP_PROJECT_ID;
  const secretName = `linear-${environment}`;

  const [version] = await client.accessSecretVersion({
    name: `projects/${projectId}/secrets/${secretName}/versions/latest`,
  });

  return JSON.parse(version.payload!.data!.toString());
}
```

### Step 3: Environment-Aware Client Factory
```typescript
// lib/client-factory.ts
import { LinearClient } from "@linear/sdk";
import { getConfig } from "../config/environments";

let clientInstance: LinearClient | null = null;

export async function getLinearClient(): Promise<LinearClient> {
  if (clientInstance) return clientInstance;

  const config = getConfig();

  // In production, fetch from secret manager
  let apiKey = config.apiKey;
  if (process.env.NODE_ENV === "production") {
    const secrets = await getLinearSecrets("production");
    apiKey = secrets.apiKey;
  }

  clientInstance = new LinearClient({ apiKey });
  return clientInstance;
}

// For testing - allow client injection
export function setLinearClient(client: LinearClient): void {
  clientInstance = client;
}

export function resetLinearClient(): void {
  clientInstance = null;
}
```

### Step 4: Environment Guards
```typescript
// lib/environment-guards.ts
import { getConfig } from "../config/environments";

export function requireProduction(): void {
  if (process.env.NODE_ENV !== "production") {
    throw new Error("This operation requires production environment");
  }
}

export function preventProduction(): void {
  if (process.env.NODE_ENV === "production") {
    throw new Error("This operation is not allowed in production");
  }
}

export function isDebugMode(): boolean {
  return getConfig().features.debugMode;
}

// Decorator for production-only functions
export function productionOnly(
  target: any,
  propertyKey: string,
  descriptor: PropertyDescriptor
) {
  const originalMethod = descriptor.value;

  descriptor.value = function (...args: any[]) {
    requireProduction();
    return originalMethod.apply(this, args);
  };

  return descriptor;
}

// Safe issue deletion (prevents accidental production deletes)
export async function safeDeleteIssue(
  client: LinearClient,
  issueId: string
): Promise<void> {
  const env = process.env.NODE_ENV;

  if (env === "production") {
    // In production, archive instead of delete
    await client.archiveIssue(issueId);
    console.log(`Archived issue ${issueId} (production safe mode)`);
  } else {
    // In dev/staging, actually delete
    await client.deleteIssue(issueId);
    console.log(`Deleted issue ${issueId}`);
  }
}
```

### Step 5: Environment-Specific Webhook Configuration
```typescript
// config/webhooks.ts
interface WebhookConfig {
  url: string;
  events: string[];
  enabled: boolean;
}

const webhookConfigs: Record<string, WebhookConfig> = {
  development: {
    url: "http://localhost:3000/api/webhooks/linear",
    events: ["Issue", "IssueComment"], // Minimal events for dev
    enabled: false, // Use polling instead
  },
  staging: {
    url: "https://staging.yourapp.com/api/webhooks/linear",
    events: ["Issue", "IssueComment", "Project", "Cycle"],
    enabled: true,
  },
  production: {
    url: "https://yourapp.com/api/webhooks/linear",
    events: ["Issue", "IssueComment", "Project", "Cycle", "Label"],
    enabled: true,
  },
};

export function getWebhookConfig(): WebhookConfig {
  const env = process.env.NODE_ENV || "development";
  return webhookConfigs[env];
}
```

### Step 6: CI/CD Environment Configuration

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches:
      - main      # Deploy to staging
      - release/* # Deploy to production

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ github.ref == 'refs/heads/main' && 'staging' || 'production' }}

    steps:
      - uses: actions/checkout@v4

      - name: Configure environment
        run: |
          if [ "${{ github.ref }}" == "refs/heads/main" ]; then
            echo "DEPLOY_ENV=staging" >> $GITHUB_ENV
          else
            echo "DEPLOY_ENV=production" >> $GITHUB_ENV
          fi

      - name: Deploy
        run: npm run deploy
        env:
          NODE_ENV: ${{ env.DEPLOY_ENV }}
          LINEAR_API_KEY: ${{ secrets.LINEAR_API_KEY }}
          LINEAR_WEBHOOK_SECRET: ${{ secrets.LINEAR_WEBHOOK_SECRET }}
```

## Environment Validation
```typescript
// scripts/validate-environment.ts
async function validateEnvironment(): Promise<void> {
  const config = getConfig();
  const env = process.env.NODE_ENV;

  console.log(`Validating ${env} environment...`);

  // Check API key works
  const client = await getLinearClient();
  const viewer = await client.viewer;
  console.log(`  API Key: Valid (${viewer.email})`);

  // Check team access
  const teams = await client.teams();
  const hasDefaultTeam = teams.nodes.some(t => t.key === config.defaultTeamKey);
  console.log(`  Default Team (${config.defaultTeamKey}): ${hasDefaultTeam ? "Found" : "NOT FOUND"}`);

  // Check webhook secret is set
  console.log(`  Webhook Secret: ${config.webhookSecret ? "Set" : "NOT SET"}`);

  console.log("Environment validation complete!");
}

validateEnvironment().catch(console.error);
```

## Error Handling
| Error | Cause | Solution |
|-------|-------|----------|
| `Wrong environment` | API key mismatch | Verify secrets for correct env |
| `Secret not found` | Missing secret | Add secret to secret manager |
| `Team not found` | Wrong workspace | Check defaultTeamKey setting |
| `Permission denied` | Insufficient scope | Regenerate API key |

## Resources
- [Linear API Authentication](https://developers.linear.app/docs/graphql/authentication)
- [12-Factor App Config](https://12factor.net/config)
- [HashiCorp Vault](https://www.vaultproject.io/docs)

## Next Steps
Set up observability with `linear-observability`.
