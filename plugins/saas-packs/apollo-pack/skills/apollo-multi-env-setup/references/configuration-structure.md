# Configuration Structure

## Configuration Structure

```typescript
// src/config/apollo/environments.ts
import { z } from 'zod';

const EnvironmentConfigSchema = z.object({
  apiKey: z.string().min(1),
  baseUrl: z.string().url().default('https://api.apollo.io/v1'),
  rateLimit: z.number().positive(),
  timeout: z.number().positive().default(30000),
  cacheEnabled: z.boolean().default(true),
  cacheTtl: z.number().positive().default(300),
  features: z.object({
    search: z.boolean().default(true),
    enrichment: z.boolean().default(true),
    sequences: z.boolean().default(false),
    webhooks: z.boolean().default(false),
  }),
  logging: z.object({
    level: z.enum(['debug', 'info', 'warn', 'error']),
    redactPII: z.boolean().default(true),
  }),
});

type EnvironmentConfig = z.infer<typeof EnvironmentConfigSchema>;

const configs: Record<string, EnvironmentConfig> = {
  development: {
    apiKey: process.env.APOLLO_API_KEY_DEV || '',
    baseUrl: 'https://api.apollo.io/v1',
    rateLimit: 10,
    timeout: 30000,
    cacheEnabled: true,
    cacheTtl: 60, // Short cache in dev
    features: {
      search: true,
      enrichment: true,
      sequences: false, // Disabled in dev
      webhooks: false,
    },
    logging: {
      level: 'debug',
      redactPII: false, // Show full data in dev
    },
  },

  staging: {
    apiKey: process.env.APOLLO_API_KEY_STAGING || '',
    baseUrl: 'https://api.apollo.io/v1',
    rateLimit: 50,
    timeout: 30000,
    cacheEnabled: true,
    cacheTtl: 300,
    features: {
      search: true,
      enrichment: true,
      sequences: true,
      webhooks: true,
    },
    logging: {
      level: 'info',
      redactPII: true,
    },
  },

  production: {
    apiKey: process.env.APOLLO_API_KEY || '',
    baseUrl: 'https://api.apollo.io/v1',
    rateLimit: 90, // Buffer below 100
    timeout: 30000,
    cacheEnabled: true,
    cacheTtl: 900, // 15 min in prod
    features: {
      search: true,
      enrichment: true,
      sequences: true,
      webhooks: true,
    },
    logging: {
      level: 'warn',
      redactPII: true,
    },
  },
};

export function getConfig(): EnvironmentConfig {
  const env = process.env.NODE_ENV || 'development';
  const config = configs[env];

  if (!config) {
    throw new Error(`Unknown environment: ${env}`);
  }

  // Validate configuration
  const result = EnvironmentConfigSchema.safeParse(config);
  if (!result.success) {
    throw new Error(`Invalid Apollo config for ${env}: ${result.error.message}`);
  }

  return result.data;
}

export function validateEnvironment(): void {
  const config = getConfig();

  if (!config.apiKey) {
    throw new Error('Apollo API key is required');
  }

  console.log(`Apollo configured for ${process.env.NODE_ENV || 'development'}`);
  console.log(`  Rate limit: ${config.rateLimit}/min`);
  console.log(`  Features: ${Object.entries(config.features).filter(([,v]) => v).map(([k]) => k).join(', ')}`);
}
```