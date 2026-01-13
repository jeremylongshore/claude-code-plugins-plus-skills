---
name: clerk-upgrade-migration
license: MIT
allowed-tools: Read, Write, Edit, Bash, Grep
description: Upgrade clerk sdk versions and handle breaking changes. use when upgrading
  clerk packages, migrating to new sdk versions, or handling deprecation warnings.
  trigger with phrases like "upgrade clerk", "clerk migration", "update clerk sdk",
  "clerk br...
---
# Clerk Upgrade & Migration

## Overview
Safely upgrade Clerk SDK versions and handle breaking changes.

## Prerequisites
- Current Clerk integration working
- Git repository with clean working state
- Test environment available

## Instructions

### Step 1: Check Current Version and Available Updates
```bash
# Check current version
npm list @clerk/nextjs

# Check for updates
npm outdated @clerk/nextjs

# View changelog
npm view @clerk/nextjs versions --json | tail -20
```

### Step 2: Review Breaking Changes
```typescript
// Common breaking changes by major version:

// v5 -> v6 Changes:
// - clerkMiddleware() replaces authMiddleware()
// - auth() is now async
// - Removed deprecated hooks
// - New createRouteMatcher() API

// Before (v5)
import { authMiddleware } from '@clerk/nextjs'
export default authMiddleware({
  publicRoutes: ['/']
})

// After (v6)
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'
const isPublicRoute = createRouteMatcher(['/'])
export default clerkMiddleware(async (auth, req) => {
  if (!isPublicRoute(req)) await auth.protect()
})
```

### Step 3: Upgrade Process
```bash
# 1. Create upgrade branch
git checkout -b upgrade-clerk-sdk

# 2. Update package
npm install @clerk/nextjs@latest

# 3. Check for peer dependency issues
npm ls @clerk/nextjs

# 4. Run type checking
npm run typecheck

# 5. Run tests
npm test
```

### Step 4: Handle Common Migration Patterns

#### Middleware Migration (v5 to v6)
```typescript
// OLD: authMiddleware (deprecated)
import { authMiddleware } from '@clerk/nextjs'

export default authMiddleware({
  publicRoutes: ['/', '/sign-in', '/sign-up'],
  ignoredRoutes: ['/api/webhooks(.*)']
})

// NEW: clerkMiddleware
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'

const isPublicRoute = createRouteMatcher([
  '/',
  '/sign-in(.*)',
  '/sign-up(.*)'
])

export default clerkMiddleware(async (auth, request) => {
  if (!isPublicRoute(request)) {
    await auth.protect()
  }
})
```

#### Async Auth Migration
```typescript
// OLD: Synchronous auth
import { auth } from '@clerk/nextjs'

export function GET() {
  const { userId } = auth()  // Synchronous
  // ...
}

// NEW: Async auth
import { auth } from '@clerk/nextjs/server'

export async function GET() {
  const { userId } = await auth()  // Async
  // ...
}
```

#### Hook Updates
```typescript
// OLD: useAuth() changes
const { isSignedIn, isLoaded } = useAuth()

// NEW: Check specific deprecations
// useAuth() still works but some properties changed

// OLD: Deprecated organization hooks
import { useOrganization } from '@clerk/nextjs'
const { membership } = useOrganization()

// NEW: Updated API
import { useOrganization } from '@clerk/nextjs'
const { organization, membership } = useOrganization()
```

### Step 5: Update Import Paths
```typescript
// Server imports (Next.js App Router)
import { auth, currentUser, clerkClient } from '@clerk/nextjs/server'

// Client imports
import { useUser, useAuth, useClerk } from '@clerk/nextjs'

// Component imports
import {
  ClerkProvider,
  SignIn,
  SignUp,
  UserButton,
  SignInButton,
  SignUpButton
} from '@clerk/nextjs'
```

### Step 6: Test Upgrade
```typescript
// tests/clerk-upgrade.test.ts
import { describe, it, expect } from 'vitest'

describe('Clerk Upgrade Validation', () => {
  it('auth() returns userId for authenticated users', async () => {
    // Mock or integration test
  })

  it('middleware protects routes correctly', async () => {
    // Test protected routes return 401/redirect
  })

  it('webhooks still verify correctly', async () => {
    // Test webhook signature verification
  })
})
```

### Step 7: Rollback Plan
```bash
# If upgrade fails, rollback:
git checkout main -- package.json package-lock.json
npm install

# Or restore from specific version
npm install @clerk/nextjs@5.7.1  # Previous version
```

## Version Compatibility Matrix

| @clerk/nextjs | Next.js | Node.js |
|--------------|---------|---------|
| 6.x | 14.x, 15.x | 18.x, 20.x |
| 5.x | 13.x, 14.x | 18.x, 20.x |
| 4.x | 12.x, 13.x | 16.x, 18.x |

## Migration Checklist

- [ ] Backup current package.json
- [ ] Review changelog for breaking changes
- [ ] Update @clerk/nextjs package
- [ ] Update middleware to clerkMiddleware
- [ ] Make auth() calls async
- [ ] Update deprecated hooks
- [ ] Fix import paths
- [ ] Run type checking
- [ ] Run tests
- [ ] Test authentication flows manually
- [ ] Deploy to staging
- [ ] Monitor for errors
- [ ] Deploy to production

## Output
- Updated Clerk SDK
- Migrated breaking changes
- All tests passing
- Production deployment ready

## Error Handling
| Error | Cause | Solution |
|-------|-------|----------|
| Type errors after upgrade | API changes | Check changelog, update types |
| Middleware not executing | Matcher syntax changed | Update matcher regex |
| auth() returns Promise | Now async in v6 | Add await to auth() calls |
| Import errors | Path changes | Update to @clerk/nextjs/server |

## Resources
- [Clerk Changelog](https://clerk.com/changelog)
- [Migration Guides](https://clerk.com/docs/upgrade-guides)
- [GitHub Releases](https://github.com/clerk/javascript/releases)

## Next Steps
After upgrade, review `clerk-ci-integration` for CI/CD updates.
