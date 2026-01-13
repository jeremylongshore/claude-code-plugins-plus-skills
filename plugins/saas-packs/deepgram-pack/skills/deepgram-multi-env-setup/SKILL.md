---
name: deepgram-multi-env-setup
license: MIT
allowed-tools: Read, Write, Edit, Bash
description: Configure Deepgram multi-environment setup for dev, staging, and production.
  Use when setting up environment-specific configurations, managing multiple Deepgram
  projects, or implementing environment isolation. Trigger with phrases like "deepgram
  e...
---
# Deepgram Multi-Environment Setup

## Overview
Configure isolated Deepgram environments for development, staging, and production with proper configuration management.

## Prerequisites
- Access to Deepgram Console
- Multiple Deepgram projects (recommended)
- Environment management system
- Secret management solution

## Environment Strategy

| Environment | Purpose | API Key Scope | Model | Rate Limits |
|-------------|---------|---------------|-------|-------------|
| Development | Local testing | Dev project | base | Low |
| Staging | Pre-prod testing | Staging project | nova-2 | Medium |
| Production | Live traffic | Prod project | nova-2 | High |

## Instructions

### Step 1: Create Deepgram Projects
Create separate projects in Deepgram Console for each environment.

### Step 2: Configure API Keys
Generate environment-specific API keys with appropriate scopes.

### Step 3: Implement Config Management
Create configuration system for environment switching.

### Step 4: Set Up Secret Management
Securely store and access API keys per environment.

## Examples

### Environment Configuration
```typescript
// config/deepgram.ts
interface DeepgramConfig {
  apiKey: string;
  projectId: string;
  model: string;
  features: {
    diarization: boolean;
    smartFormat: boolean;
    punctuate: boolean;
  };
  limits: {
    maxConcurrent: number;
    maxDurationMinutes: number;
  };
  callbacks: {
    baseUrl: string;
  };
}

const configs: Record<string, DeepgramConfig> = {
  development: {
    apiKey: process.env.DEEPGRAM_API_KEY_DEV!,
    projectId: process.env.DEEPGRAM_PROJECT_ID_DEV!,
    model: 'base',
    features: {
      diarization: false,
      smartFormat: true,
      punctuate: true,
    },
    limits: {
      maxConcurrent: 5,
      maxDurationMinutes: 10,
    },
    callbacks: {
      baseUrl: 'http://localhost:3000',
    },
  },
  staging: {
    apiKey: process.env.DEEPGRAM_API_KEY_STAGING!,
    projectId: process.env.DEEPGRAM_PROJECT_ID_STAGING!,
    model: 'nova-2',
    features: {
      diarization: true,
      smartFormat: true,
      punctuate: true,
    },
    limits: {
      maxConcurrent: 20,
      maxDurationMinutes: 60,
    },
    callbacks: {
      baseUrl: 'https://staging.example.com',
    },
  },
  production: {
    apiKey: process.env.DEEPGRAM_API_KEY_PRODUCTION!,
    projectId: process.env.DEEPGRAM_PROJECT_ID_PRODUCTION!,
    model: 'nova-2',
    features: {
      diarization: true,
      smartFormat: true,
      punctuate: true,
    },
    limits: {
      maxConcurrent: 100,
      maxDurationMinutes: 180,
    },
    callbacks: {
      baseUrl: 'https://api.example.com',
    },
  },
};

export function getConfig(): DeepgramConfig {
  const env = process.env.NODE_ENV || 'development';
  const config = configs[env];

  if (!config) {
    throw new Error(`Unknown environment: ${env}`);
  }

  if (!config.apiKey) {
    throw new Error(`DEEPGRAM_API_KEY not set for ${env}`);
  }

  return config;
}
```

### Environment-Aware Client Factory
```typescript
// lib/deepgram-factory.ts
import { createClient, DeepgramClient } from '@deepgram/sdk';
import { getConfig } from '../config/deepgram';

let clients: Map<string, DeepgramClient> = new Map();

export function getDeepgramClient(): DeepgramClient {
  const config = getConfig();
  const env = process.env.NODE_ENV || 'development';

  if (!clients.has(env)) {
    clients.set(env, createClient(config.apiKey));
  }

  return clients.get(env)!;
}

export function resetClients(): void {
  clients.clear();
}

// Transcribe with environment-specific settings
export async function transcribe(audioUrl: string) {
  const client = getDeepgramClient();
  const config = getConfig();

  const { result, error } = await client.listen.prerecorded.transcribeUrl(
    { url: audioUrl },
    {
      model: config.model,
      smart_format: config.features.smartFormat,
      punctuate: config.features.punctuate,
      diarize: config.features.diarization,
    }
  );

  if (error) throw error;
  return result;
}
```

### Docker Compose Multi-Environment
```yaml
# docker-compose.yml
version: '3.8'

x-common: &common
  build: .
  restart: unless-stopped

services:
  app-dev:
    <<: *common
    container_name: deepgram-dev
    environment:
      - NODE_ENV=development
      - DEEPGRAM_API_KEY=${DEEPGRAM_API_KEY_DEV}
      - DEEPGRAM_PROJECT_ID=${DEEPGRAM_PROJECT_ID_DEV}
    ports:
      - "3000:3000"
    profiles:
      - development

  app-staging:
    <<: *common
    container_name: deepgram-staging
    environment:
      - NODE_ENV=staging
      - DEEPGRAM_API_KEY=${DEEPGRAM_API_KEY_STAGING}
      - DEEPGRAM_PROJECT_ID=${DEEPGRAM_PROJECT_ID_STAGING}
    ports:
      - "3001:3000"
    profiles:
      - staging

  app-production:
    <<: *common
    container_name: deepgram-prod
    environment:
      - NODE_ENV=production
      - DEEPGRAM_API_KEY=${DEEPGRAM_API_KEY_PRODUCTION}
      - DEEPGRAM_PROJECT_ID=${DEEPGRAM_PROJECT_ID_PRODUCTION}
    ports:
      - "3002:3000"
    deploy:
      replicas: 3
    profiles:
      - production
```

### Kubernetes ConfigMaps and Secrets
```yaml
# k8s/base/configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: deepgram-config
data:
  MODEL: "nova-2"
  SMART_FORMAT: "true"
  PUNCTUATE: "true"
---
# k8s/overlays/development/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - ../../base
configMapGenerator:
  - name: deepgram-config
    behavior: merge
    literals:
      - NODE_ENV=development
      - MODEL=base
      - MAX_CONCURRENT=5
secretGenerator:
  - name: deepgram-secrets
    literals:
      - API_KEY=${DEEPGRAM_API_KEY_DEV}
---
# k8s/overlays/staging/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - ../../base
configMapGenerator:
  - name: deepgram-config
    behavior: merge
    literals:
      - NODE_ENV=staging
      - MAX_CONCURRENT=20
secretGenerator:
  - name: deepgram-secrets
    literals:
      - API_KEY=${DEEPGRAM_API_KEY_STAGING}
---
# k8s/overlays/production/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - ../../base
configMapGenerator:
  - name: deepgram-config
    behavior: merge
    literals:
      - NODE_ENV=production
      - MAX_CONCURRENT=100
secretGenerator:
  - name: deepgram-secrets
    literals:
      - API_KEY=${DEEPGRAM_API_KEY_PRODUCTION}
```

### Environment Validation Script
```typescript
// scripts/validate-env.ts
import { createClient } from '@deepgram/sdk';

interface EnvValidation {
  environment: string;
  valid: boolean;
  apiKeyValid: boolean;
  projectAccess: boolean;
  features: string[];
  errors: string[];
}

async function validateEnvironment(
  name: string,
  apiKey: string,
  projectId: string
): Promise<EnvValidation> {
  const result: EnvValidation = {
    environment: name,
    valid: false,
    apiKeyValid: false,
    projectAccess: false,
    features: [],
    errors: [],
  };

  if (!apiKey) {
    result.errors.push('API key not set');
    return result;
  }

  try {
    const client = createClient(apiKey);

    // Test API key validity
    const { result: projectsResult, error: projectsError } =
      await client.manage.getProjects();

    if (projectsError) {
      result.errors.push(`API key error: ${projectsError.message}`);
      return result;
    }

    result.apiKeyValid = true;

    // Check project access
    const project = projectsResult.projects.find(p => p.project_id === projectId);
    if (!project) {
      result.errors.push(`Project ${projectId} not accessible`);
    } else {
      result.projectAccess = true;
    }

    // Test transcription capability
    const { error: transcribeError } = await client.listen.prerecorded.transcribeUrl(
      { url: 'https://static.deepgram.com/examples/nasa-podcast.wav' },
      { model: 'nova-2' }
    );

    if (!transcribeError) {
      result.features.push('transcription');
    }

    result.valid = result.apiKeyValid && result.projectAccess;
  } catch (error) {
    result.errors.push(error instanceof Error ? error.message : 'Unknown error');
  }

  return result;
}

async function main() {
  const environments = [
    {
      name: 'development',
      apiKey: process.env.DEEPGRAM_API_KEY_DEV!,
      projectId: process.env.DEEPGRAM_PROJECT_ID_DEV!,
    },
    {
      name: 'staging',
      apiKey: process.env.DEEPGRAM_API_KEY_STAGING!,
      projectId: process.env.DEEPGRAM_PROJECT_ID_STAGING!,
    },
    {
      name: 'production',
      apiKey: process.env.DEEPGRAM_API_KEY_PRODUCTION!,
      projectId: process.env.DEEPGRAM_PROJECT_ID_PRODUCTION!,
    },
  ];

  console.log('Validating Deepgram environments...\n');

  for (const env of environments) {
    const result = await validateEnvironment(env.name, env.apiKey, env.projectId);

    console.log(`${env.name.toUpperCase()}`);
    console.log(`  Valid: ${result.valid ? 'YES' : 'NO'}`);
    console.log(`  API Key: ${result.apiKeyValid ? 'OK' : 'INVALID'}`);
    console.log(`  Project Access: ${result.projectAccess ? 'OK' : 'DENIED'}`);

    if (result.features.length > 0) {
      console.log(`  Features: ${result.features.join(', ')}`);
    }

    if (result.errors.length > 0) {
      console.log(`  Errors:`);
      result.errors.forEach(e => console.log(`    - ${e}`));
    }

    console.log();
  }
}

main().catch(console.error);
```

### Terraform Multi-Environment
```hcl
# terraform/modules/deepgram/main.tf
variable "environment" {
  type = string
}

variable "deepgram_api_key" {
  type      = string
  sensitive = true
}

variable "config" {
  type = object({
    model          = string
    max_concurrent = number
  })
}

# Store API key in secret manager
resource "aws_secretsmanager_secret" "deepgram_api_key" {
  name = "deepgram/${var.environment}/api-key"
}

resource "aws_secretsmanager_secret_version" "deepgram_api_key" {
  secret_id     = aws_secretsmanager_secret.deepgram_api_key.id
  secret_string = var.deepgram_api_key
}

# terraform/environments/production/main.tf
module "deepgram" {
  source = "../../modules/deepgram"

  environment      = "production"
  deepgram_api_key = var.deepgram_api_key_production

  config = {
    model          = "nova-2"
    max_concurrent = 100
  }
}
```

## Resources
- [Deepgram Projects](https://developers.deepgram.com/docs/projects)
- [API Key Management](https://developers.deepgram.com/docs/api-key-management)
- [Environment Best Practices](https://developers.deepgram.com/docs/environments)

## Next Steps
Proceed to `deepgram-observability` for monitoring setup.
