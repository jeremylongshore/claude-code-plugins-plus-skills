# Api Key Security

## API Key Security

### Never Hardcode Keys
```typescript
// BAD - Never do this
const apiKey = 'sk_live_abc123...';

// GOOD - Use environment variables
const apiKey = process.env.APOLLO_API_KEY;

// BETTER - Validate on startup
if (!process.env.APOLLO_API_KEY) {
  throw new Error('APOLLO_API_KEY environment variable is required');
}
```

### Secure Storage
```bash
# .env file (never commit!)
APOLLO_API_KEY=your-api-key-here

# .gitignore (always include!)
.env
.env.local
.env.*.local
*.key
```

### Key Rotation
```typescript
// src/lib/apollo/key-rotation.ts
interface KeyConfig {
  primary: string;
  secondary?: string;
  rotateAt?: Date;
}

class ApiKeyManager {
  private config: KeyConfig;

  constructor() {
    this.config = {
      primary: process.env.APOLLO_API_KEY!,
      secondary: process.env.APOLLO_API_KEY_SECONDARY,
      rotateAt: process.env.APOLLO_KEY_ROTATE_AT
        ? new Date(process.env.APOLLO_KEY_ROTATE_AT)
        : undefined,
    };
  }

  getActiveKey(): string {
    if (this.config.rotateAt && new Date() > this.config.rotateAt) {
      if (this.config.secondary) {
        return this.config.secondary;
      }
      console.warn('Key rotation date passed but no secondary key available');
    }
    return this.config.primary;
  }

  async testKey(key: string): Promise<boolean> {
    try {
      const response = await axios.get('https://api.apollo.io/v1/auth/health', {
        params: { api_key: key },
      });
      return response.status === 200;
    } catch {
      return false;
    }
  }

  async rotateKeys(): Promise<void> {
    if (!this.config.secondary) {
      throw new Error('No secondary key configured for rotation');
    }

    // Verify secondary key works
    const isValid = await this.testKey(this.config.secondary);
    if (!isValid) {
      throw new Error('Secondary key is invalid');
    }

    // Swap keys
    console.log('Rotating API keys...');
    this.config.primary = this.config.secondary;
    this.config.secondary = undefined;
    // TODO: Persist to secure storage
  }
}
```