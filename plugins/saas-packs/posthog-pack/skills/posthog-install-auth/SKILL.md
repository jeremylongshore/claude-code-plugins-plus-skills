---
allowed-tools: Read, Write, Edit, Bash, Grep
license: MIT
description: Install and configure posthog sdk/cli authentication. use when setting
  up a new posthog integration, configuring api keys, or initializing posthog in your
  project. trigger with phrases like "install posthog", "setup posthog", "posthog
  auth", "conf...
name: posthog-install-auth
---
# PostHog Install & Auth

This skill provides automated assistance for posthog install auth tasks.

## Overview
Set up PostHog SDK/CLI and configure authentication credentials.

## Prerequisites
- Node.js 18+ or Python 3.10+
- Package manager (npm, pnpm, or pip)
- PostHog account with API access
- API key from PostHog dashboard

## Instructions

### Step 1: Install SDK
```bash
# Node.js
npm install @posthog/sdk

# Python
pip install posthog
```

### Step 2: Configure Authentication
```bash
# Set environment variable
export POSTHOG_API_KEY="your-api-key"

# Or create .env file
echo 'POSTHOG_API_KEY=your-api-key' >> .env
```

### Step 3: Verify Connection
```typescript
// Test connection code here
```

## Output
- Installed SDK package in node_modules or site-packages
- Environment variable or .env file with API key
- Successful connection verification output

## Error Handling
| Error | Cause | Solution |
|-------|-------|----------|
| Invalid API Key | Incorrect or expired key | Verify key in PostHog dashboard |
| Rate Limited | Exceeded quota | Check quota at https://docs.posthog.com |
| Network Error | Firewall blocking | Ensure outbound HTTPS allowed |
| Module Not Found | Installation failed | Run `npm install` or `pip install` again |

## Examples

### TypeScript Setup
```typescript
import { PostHogClient } from '@posthog/sdk';

const client = new PostHogClient({
  apiKey: process.env.POSTHOG_API_KEY,
});
```

### Python Setup
```python
from posthog import PostHogClient

client = PostHogClient(
    api_key=os.environ.get('POSTHOG_API_KEY')
)
```

## Resources
- [PostHog Documentation](https://docs.posthog.com)
- [PostHog Dashboard](https://api.posthog.com)
- [PostHog Status](https://status.posthog.com)

## Next Steps
After successful auth, proceed to `posthog-hello-world` for your first API call.