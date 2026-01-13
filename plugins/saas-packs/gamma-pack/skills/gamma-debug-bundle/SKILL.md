---
name: gamma-debug-bundle
description: |
  Comprehensive debugging toolkit for Gamma integration issues.
  Use when you need detailed diagnostics, request tracing,
  or systematic debugging of Gamma API problems.
  Trigger with phrases like "gamma debug bundle", "gamma diagnostics",
  "gamma trace", "gamma inspect", "gamma detailed logs".
allowed-tools: Read, Write, Edit, Bash, Grep
version: 1.0.0
license: MIT
author: Jeremy Longshore <jeremy@intentsolutions.io>
---

# Gamma Debug Bundle

## Overview
Comprehensive debugging toolkit for systematic troubleshooting of Gamma integration issues.

## Prerequisites
- Active Gamma integration with issues
- Node.js 18+ for debug tools
- Access to application logs

## Instructions

### Step 1: Create Debug Client
```typescript
// debug/gamma-debug.ts
import { GammaClient } from '@gamma/sdk';

interface DebugLog {
  timestamp: string;
  method: string;
  path: string;
  requestBody?: object;
  responseBody?: object;
  duration: number;
  status: number;
  error?: string;
}

const logs: DebugLog[] = [];

export function createDebugClient() {
  const gamma = new GammaClient({
    apiKey: process.env.GAMMA_API_KEY,
    interceptors: {
      request: (config) => {
        config._startTime = Date.now();
        config._id = crypto.randomUUID();
        console.log(`[${config._id}] -> ${config.method} ${config.path}`);
        return config;
      },
      response: (response, config) => {
        const duration = Date.now() - config._startTime;
        console.log(`[${config._id}] <- ${response.status} (${duration}ms)`);

        logs.push({
          timestamp: new Date().toISOString(),
          method: config.method,
          path: config.path,
          requestBody: config.body,
          responseBody: response.data,
          duration,
          status: response.status,
        });

        return response;
      },
      error: (error, config) => {
        const duration = Date.now() - config._startTime;
        console.error(`[${config._id}] !! ${error.message} (${duration}ms)`);

        logs.push({
          timestamp: new Date().toISOString(),
          method: config.method,
          path: config.path,
          requestBody: config.body,
          duration,
          status: error.status || 0,
          error: error.message,
        });

        throw error;
      },
    },
  });

  return { gamma, getLogs: () => [...logs], clearLogs: () => logs.length = 0 };
}
```

### Step 2: Diagnostic Script
```typescript
// debug/diagnose.ts
import { createDebugClient } from './gamma-debug';

async function diagnose() {
  const { gamma, getLogs } = createDebugClient();

  console.log('=== Gamma Diagnostic Report ===\n');

  // Test 1: Authentication
  console.log('1. Testing Authentication...');
  try {
    await gamma.ping();
    console.log('   OK - Authentication working\n');
  } catch (err) {
    console.log(`   FAIL - ${err.message}\n`);
    return;
  }

  // Test 2: API Access
  console.log('2. Testing API Access...');
  try {
    const presentations = await gamma.presentations.list({ limit: 1 });
    console.log(`   OK - Can list presentations (${presentations.length} found)\n`);
  } catch (err) {
    console.log(`   FAIL - ${err.message}\n`);
  }

  // Test 3: Generation Capability
  console.log('3. Testing Generation...');
  try {
    const test = await gamma.presentations.create({
      title: 'Debug Test',
      prompt: 'Single test slide',
      slideCount: 1,
      dryRun: true,
    });
    console.log('   OK - Generation endpoint working\n');
  } catch (err) {
    console.log(`   FAIL - ${err.message}\n`);
  }

  // Test 4: Rate Limits
  console.log('4. Checking Rate Limits...');
  const status = await gamma.rateLimit.status();
  console.log(`   Remaining: ${status.remaining}/${status.limit}`);
  console.log(`   Resets: ${new Date(status.reset * 1000).toISOString()}\n`);

  // Summary
  console.log('=== Request Log ===');
  for (const log of getLogs()) {
    console.log(`${log.method} ${log.path} - ${log.status} (${log.duration}ms)`);
  }
}

diagnose().catch(console.error);
```

### Step 3: Environment Checker
```typescript
// debug/check-env.ts
function checkEnvironment() {
  const checks = [
    { name: 'GAMMA_API_KEY', value: process.env.GAMMA_API_KEY },
    { name: 'NODE_ENV', value: process.env.NODE_ENV },
    { name: 'Node Version', value: process.version },
  ];

  console.log('=== Environment Check ===\n');

  for (const check of checks) {
    const status = check.value ? 'SET' : 'MISSING';
    const display = check.value
      ? check.value.substring(0, 8) + '...'
      : 'NOT SET';
    console.log(`${check.name}: ${status} (${display})`);
  }
}

checkEnvironment();
```

### Step 4: Export Debug Bundle
```typescript
// debug/export-bundle.ts
async function exportDebugBundle() {
  const bundle = {
    timestamp: new Date().toISOString(),
    environment: {
      nodeVersion: process.version,
      platform: process.platform,
      env: process.env.NODE_ENV,
    },
    logs: getLogs(),
    config: {
      apiKeySet: !!process.env.GAMMA_API_KEY,
      timeout: 30000,
    },
  };

  await fs.writeFile(
    'gamma-debug-bundle.json',
    JSON.stringify(bundle, null, 2)
  );

  console.log('Debug bundle exported to gamma-debug-bundle.json');
}
```

## Output
- Debug client with request tracing
- Diagnostic script output
- Environment check report
- Exportable debug bundle

## Resources
- [Gamma Debug Guide](https://gamma.app/docs/debugging)
- [Gamma Support Portal](https://gamma.app/support)

## Next Steps
Proceed to `gamma-rate-limits` for rate limit management.
