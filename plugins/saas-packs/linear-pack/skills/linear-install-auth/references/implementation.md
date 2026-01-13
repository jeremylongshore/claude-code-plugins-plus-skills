# Implementation Guide

### Step 1: Install SDK
```bash
# npm
npm install @linear/sdk

# pnpm
pnpm add @linear/sdk

# yarn
yarn add @linear/sdk
```

### Step 2: Generate API Key
1. Go to Linear Settings > API > Personal API keys
2. Click "Create key"
3. Copy the generated key (shown only once)

### Step 3: Configure Authentication
```bash
# Set environment variable
export LINEAR_API_KEY="lin_api_xxxxxxxxxxxx"

# Or create .env file
echo 'LINEAR_API_KEY=lin_api_xxxxxxxxxxxx' >> .env
```

### Step 4: Verify Connection
```typescript
import { LinearClient } from "@linear/sdk";

const client = new LinearClient({ apiKey: process.env.LINEAR_API_KEY });
const me = await client.viewer;
console.log(`Authenticated as: ${me.name} (${me.email})`);
```