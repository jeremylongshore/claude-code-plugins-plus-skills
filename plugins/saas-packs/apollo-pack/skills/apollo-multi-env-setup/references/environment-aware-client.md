# Environment-Aware Client

## Environment-Aware Client

```typescript
// src/lib/apollo/env-client.ts
import { getConfig } from '../../config/apollo/environments';

class EnvironmentAwareApolloClient {
  private config = getConfig();

  async request<T>(options: RequestOptions): Promise<T> {
    // Check feature flag
    if (!this.isFeatureEnabled(options.feature)) {
      throw new Error(`Feature ${options.feature} is disabled in ${process.env.NODE_ENV}`);
    }

    // Apply environment-specific rate limiting
    await this.rateLimiter.acquire();

    // Make request with environment config
    const response = await axios({
      ...options,
      baseURL: this.config.baseUrl,
      timeout: this.config.timeout,
      params: {
        ...options.params,
        api_key: this.config.apiKey,
      },
    });

    // Log based on environment
    this.log('info', `Apollo ${options.method} ${options.url}`, {
      status: response.status,
      duration: response.headers['x-response-time'],
    });

    return response.data;
  }

  private isFeatureEnabled(feature: string): boolean {
    return this.config.features[feature as keyof typeof this.config.features] ?? true;
  }

  private log(level: string, message: string, meta?: object): void {
    if (this.shouldLog(level)) {
      const sanitized = this.config.logging.redactPII
        ? this.redactPII(meta)
        : meta;
      console[level as 'log'](`[Apollo] ${message}`, sanitized);
    }
  }

  private shouldLog(level: string): boolean {
    const levels = ['debug', 'info', 'warn', 'error'];
    return levels.indexOf(level) >= levels.indexOf(this.config.logging.level);
  }
}
```