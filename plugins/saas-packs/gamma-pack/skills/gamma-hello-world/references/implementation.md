# Implementation Guide

### Step 1: Create Entry File
Create a new file for your hello world example.

### Step 2: Import and Initialize Client
```typescript
import { GammaClient } from '@gamma/sdk';

const gamma = new GammaClient({
  apiKey: process.env.GAMMA_API_KEY,
});
```

### Step 3: Generate Your First Presentation
```typescript
async function main() {
  const presentation = await gamma.presentations.create({
    title: 'Hello Gamma!',
    prompt: 'Create a 3-slide introduction to AI presentations',
    style: 'professional',
  });

  console.log('Presentation created:', presentation.url);
}

main().catch(console.error);
```