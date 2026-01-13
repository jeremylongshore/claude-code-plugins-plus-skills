# Examples

### Import Changes
```typescript
// Before (v1.x)
import { Client } from '@firecrawl/sdk';

// After (v2.x)
import { FireCrawlClient } from '@firecrawl/sdk';
```

### Configuration Changes
```typescript
// Before (v1.x)
const client = new Client({ key: 'xxx' });

// After (v2.x)
const client = new FireCrawlClient({
  apiKey: 'xxx',
});
```

### Rollback Procedure
```bash
npm install @firecrawl/sdk@1.x.x --save-exact
```

### Deprecation Handling
```typescript
// Monitor for deprecation warnings in development
if (process.env.NODE_ENV === 'development') {
  process.on('warning', (warning) => {
    if (warning.name === 'DeprecationWarning') {
      console.warn('[FireCrawl]', warning.message);
      // Log to tracking system for proactive updates
    }
  });
}

// Common deprecation patterns to watch for:
// - Renamed methods: client.oldMethod() -> client.newMethod()
// - Changed parameters: { key: 'x' } -> { apiKey: 'x' }
// - Removed features: Check release notes before upgrading
```