# Implementation Guide

### Step 1: Install SDK
```bash
# Node.js (Track API)
npm install customerio-node

# Node.js (Journeys Track API - recommended)
npm install @customerio/track

# Python
pip install customerio
```

### Step 2: Configure Authentication
```bash
# Set environment variables
export CUSTOMERIO_SITE_ID="your-site-id"
export CUSTOMERIO_API_KEY="your-api-key"

# Or create .env file
cat >> .env << 'EOF'
CUSTOMERIO_SITE_ID=your-site-id
CUSTOMERIO_API_KEY=your-api-key
EOF
```

### Step 3: Verify Connection
```typescript
import { TrackClient, RegionUS } from '@customerio/track';

const client = new TrackClient(
  process.env.CUSTOMERIO_SITE_ID,
  process.env.CUSTOMERIO_API_KEY,
  { region: RegionUS }
);

// Test by identifying a user
await client.identify('test-user', { email: 'test@example.com' });
console.log('Customer.io connection successful');
```