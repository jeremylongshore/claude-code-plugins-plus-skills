# Data Protection

## Data Protection

### PII Handling
```typescript
// src/lib/apollo/pii-handler.ts
const PII_FIELDS = ['email', 'phone', 'personal_email', 'mobile_phone'];

function redactPII(data: any, fields: string[] = PII_FIELDS): any {
  if (!data) return data;

  if (Array.isArray(data)) {
    return data.map((item) => redactPII(item, fields));
  }

  if (typeof data === 'object') {
    const result: any = {};
    for (const [key, value] of Object.entries(data)) {
      if (fields.includes(key) && typeof value === 'string') {
        result[key] = redactForLogging(value);
      } else {
        result[key] = redactPII(value, fields);
      }
    }
    return result;
  }

  return data;
}

function redactForLogging(value: string): string {
  if (value.includes('@')) {
    // Email: show first 2 chars and domain
    const [local, domain] = value.split('@');
    return `${local.substring(0, 2)}***@${domain}`;
  }
  // Phone: show last 4 digits
  return `***-***-${value.slice(-4)}`;
}

// Usage in logging
console.log('Contact data:', redactPII(contactData));
```

### Secure Logging
```typescript
// src/lib/apollo/secure-logger.ts
import pino from 'pino';

const logger = pino({
  redact: {
    paths: [
      'api_key',
      'apiKey',
      '*.api_key',
      '*.email',
      '*.phone',
      'headers.authorization',
    ],
    censor: '[REDACTED]',
  },
});

// Apollo request interceptor with secure logging
apolloClient.interceptors.request.use((config) => {
  logger.info({
    type: 'apollo_request',
    method: config.method,
    url: config.url,
    // Don't log full request body
    bodyKeys: config.data ? Object.keys(config.data) : [],
  });
  return config;
});
```

### Data Retention
```typescript
// src/lib/apollo/data-retention.ts
interface CacheConfig {
  ttlMinutes: number;
  maxEntries: number;
}

class SecureCache {
  private cache = new Map<string, { data: any; expiresAt: number }>();
  private config: CacheConfig;

  constructor(config: CacheConfig) {
    this.config = config;
    // Cleanup expired entries every minute
    setInterval(() => this.cleanup(), 60000);
  }

  set(key: string, data: any): void {
    // Enforce max entries
    if (this.cache.size >= this.config.maxEntries) {
      const oldest = [...this.cache.entries()].sort(
        (a, b) => a[1].expiresAt - b[1].expiresAt
      )[0];
      if (oldest) this.cache.delete(oldest[0]);
    }

    this.cache.set(key, {
      data,
      expiresAt: Date.now() + this.config.ttlMinutes * 60 * 1000,
    });
  }

  get(key: string): any | null {
    const entry = this.cache.get(key);
    if (!entry) return null;
    if (Date.now() > entry.expiresAt) {
      this.cache.delete(key);
      return null;
    }
    return entry.data;
  }

  private cleanup(): void {
    const now = Date.now();
    for (const [key, entry] of this.cache.entries()) {
      if (now > entry.expiresAt) {
        this.cache.delete(key);
      }
    }
  }

  clear(): void {
    this.cache.clear();
  }
}

// Short TTL for sensitive data
export const apolloCache = new SecureCache({
  ttlMinutes: 15,
  maxEntries: 1000,
});
```