# Environment Configuration

## Environment Configuration

```typescript
// src/config/environments.ts
interface EnvironmentConfig {
  apollo: {
    apiKey: string;
    rateLimit: number;
    timeout: number;
  };
  features: {
    enrichment: boolean;
    sequences: boolean;
  };
}

const configs: Record<string, EnvironmentConfig> = {
  development: {
    apollo: {
      apiKey: process.env.APOLLO_API_KEY_DEV!,
      rateLimit: 10,
      timeout: 30000,
    },
    features: {
      enrichment: true,
      sequences: false,
    },
  },
  staging: {
    apollo: {
      apiKey: process.env.APOLLO_API_KEY_STAGING!,
      rateLimit: 50,
      timeout: 30000,
    },
    features: {
      enrichment: true,
      sequences: true,
    },
  },
  production: {
    apollo: {
      apiKey: process.env.APOLLO_API_KEY!,
      rateLimit: 90,
      timeout: 30000,
    },
    features: {
      enrichment: true,
      sequences: true,
    },
  },
};

export function getConfig(): EnvironmentConfig {
  const env = process.env.NODE_ENV || 'development';
  return configs[env] || configs.development;
}
```