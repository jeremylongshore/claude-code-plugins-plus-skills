---
name: vastai-install-auth
description: |
  Install and configure vast.ai sdk/cli authentication. use when setting up a new vast.ai integration, configuring api keys, or initializing vast.ai in your project. trigger with phrases like "install vastai", "setup vastai", "vastai auth", "configu...
allowed-tools: Read, Write, Edit, Bash(cmd:*), Grep
version: 1.0.0
author: Jeremy Longshore <jeremy@intentsolutions.io>
license: MIT
---
# Vast.ai Install & Auth

This skill provides automated assistance for vastai install auth tasks.

## Overview
Set up Vast.ai SDK/CLI and configure authentication credentials.

## Prerequisites
- Node.js 18+ or Python 3.10+
- Package manager (npm, pnpm, or pip)
- Vast.ai account with API access
- API key from Vast.ai dashboard

## Instructions

### Step 1: Install SDK
```bash
# Node.js
npm install @vastai/sdk

# Python
pip install vastai
```

### Step 2: Configure Authentication
```bash
# Set environment variable
export VASTAI_API_KEY="your-api-key"

# Or create .env file
echo 'VASTAI_API_KEY=your-api-key' >> .env
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
| Invalid API Key | Incorrect or expired key | Verify key in Vast.ai dashboard |
| Rate Limited | Exceeded quota | Check quota at https://docs.vastai.com |
| Network Error | Firewall blocking | Ensure outbound HTTPS allowed |
| Module Not Found | Installation failed | Run `npm install` or `pip install` again |

## Examples

### TypeScript Setup
```typescript
import { Vast.aiClient } from '@vastai/sdk';

const client = new Vast.aiClient({
  apiKey: process.env.VASTAI_API_KEY,
});
```

### Python Setup
```python
from vastai import Vast.aiClient

client = Vast.aiClient(
    api_key=os.environ.get('VASTAI_API_KEY')
)
```

## Resources
- [Vast.ai Documentation](https://docs.vastai.com)
- [Vast.ai Dashboard](https://api.vastai.com)
- [Vast.ai Status](https://status.vastai.com)

## Next Steps
After successful auth, proceed to `vastai-hello-world` for your first API call.