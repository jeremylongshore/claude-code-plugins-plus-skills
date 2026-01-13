---
name: lindy-multi-env-setup
description: |
  Configure Lindy AI across development, staging, and production environments.
  Use when setting up multi-environment deployments, configuring per-environment secrets,
  or implementing environment-specific Lindy configurations.
  Trigger with phrases like "lindy environments", "lindy staging",
  "lindy dev prod", "lindy environment setup", "lindy config by env".
allowed-tools: Read, Write, Edit, Bash
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Lindy Multi Env Setup

## Overview
Configure Lindy AI across development, staging, and production environments.

## Prerequisites
- Separate Lindy API keys per environment
- Secret management solution (Vault, AWS Secrets Manager, etc.)
- CI/CD pipeline with environment variables
- Environment detection in application

## Instructions

### Step 1: Create Environment Configuration
```typescript
// config/lindy.ts
interface LindyConfig {
  apiKey: string;
  environment: 'development' | 'staging' | 'production';
  baseUrl?: string;
  timeout: number;
  retries: number;
}

const configs: Record<string, LindyConfig> = {
  development: {
    apiKey: process.env.LINDY_DEV_API_KEY!,
    environment: 'development',
    timeout: 60000,
    retries: 1,
  },
  staging: {
    apiKey: process.env.LINDY_STAGING_API_KEY!,
    environment: 'staging',
    timeout: 45000,
    retries: 2,
  },
  production: {
    apiKey: process.env.LINDY_PROD_API_KEY!,
    environment: 'production',
    timeout: 30000,
    retries: 3,
  },
};

export function getLindyConfig(): LindyConfig {
  const env = process.env.NODE_ENV || 'development';
  return configs[env] || configs.development;
}
```

### Step 2: Implement Environment Detection
```typescript
// lib/lindy-client.ts
import { Lindy } from '@lindy-ai/sdk';
import { getLindyConfig } from '../config/lindy';

let client: Lindy | null = null;

export function getLindyClient(): Lindy {
  if (!client) {
    const config = getLindyConfig();

    // Validate environment
    if (config.environment === 'production') {
      if (!config.apiKey.startsWith('lnd_prod_')) {
        throw new Error('Production requires production API key');
      }
    }

    client = new Lindy({
      apiKey: config.apiKey,
      timeout: config.timeout,
      retries: config.retries,
    });
  }

  return client;
}
```

### Step 3: Configure Secrets by Environment
```yaml
# AWS Secrets Manager structure
secrets/
├── lindy/development
│   └── api_key: lnd_dev_xxx
├── lindy/staging
│   └── api_key: lnd_stg_xxx
└── lindy/production
    └── api_key: lnd_prod_xxx
```

```typescript
// secrets/lindy.ts
import { SecretsManager } from '@aws-sdk/client-secrets-manager';

export async function getLindyApiKey(env: string): Promise<string> {
  const client = new SecretsManager({ region: 'us-east-1' });

  const response = await client.getSecretValue({
    SecretId: `lindy/${env}`,
  });

  const secret = JSON.parse(response.SecretString!);
  return secret.api_key;
}
```

### Step 4: Environment-Specific Agents
```typescript
// agents/config.ts
interface AgentMapping {
  development: string;
  staging: string;
  production: string;
}

const agentMappings: Record<string, AgentMapping> = {
  support: {
    development: 'agt_dev_support',
    staging: 'agt_stg_support',
    production: 'agt_prod_support',
  },
  sales: {
    development: 'agt_dev_sales',
    staging: 'agt_stg_sales',
    production: 'agt_prod_sales',
  },
};

export function getAgentId(agentName: string): string {
  const env = process.env.NODE_ENV || 'development';
  const mapping = agentMappings[agentName];

  if (!mapping) {
    throw new Error(`Unknown agent: ${agentName}`);
  }

  return mapping[env as keyof AgentMapping];
}
```

### Step 5: Add Environment Guards
```typescript
// guards/production.ts
export function requireProduction(): void {
  if (process.env.NODE_ENV !== 'production') {
    throw new Error('This operation requires production environment');
  }
}

export function preventProduction(): void {
  if (process.env.NODE_ENV === 'production') {
    throw new Error('This operation is not allowed in production');
  }
}

// Usage
async function dangerousOperation() {
  preventProduction();
  // ... destructive test operation
}

async function productionOnlyOperation() {
  requireProduction();
  // ... production-only logic
}
```

## Output
- Multi-environment configuration
- Environment detection logic
- Secure secret management
- Environment-specific agents
- Production safeguards

## Error Handling
| Issue | Cause | Solution |
|-------|-------|----------|
| Wrong key for env | Config error | Validate key prefix |
| Secret not found | Not provisioned | Create in secrets manager |
| Agent not found | Wrong environment | Check agent mapping |

## Examples

### Complete Environment Setup
```typescript
// index.ts
import { getLindyClient } from './lib/lindy-client';
import { getAgentId } from './agents/config';

async function main() {
  const lindy = getLindyClient();
  const agentId = getAgentId('support');

  console.log(`Environment: ${process.env.NODE_ENV}`);
  console.log(`Agent: ${agentId}`);

  const result = await lindy.agents.run(agentId, {
    input: 'Test message',
  });

  console.log('Response:', result.output);
}

main().catch(console.error);
```

## Resources
- [Lindy Environments Guide](https://docs.lindy.ai/environments)
- [12-Factor App Config](https://12factor.net/config)
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)

## Next Steps
Proceed to `lindy-observability` for monitoring setup.
