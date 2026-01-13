---
name: clerk-cost-tuning
license: MIT
allowed-tools: Read, Write, Edit, Grep
description: Optimize Clerk costs and understand pricing. Use when planning budget,
  reducing costs, or understanding Clerk pricing model. Trigger with phrases like
  "clerk cost", "clerk pricing", "reduce clerk cost", "clerk billing", "clerk budget".
---
# Clerk Cost Tuning

## Overview
Understand Clerk pricing and optimize costs for your application.

## Prerequisites
- Clerk account active
- Understanding of MAU (Monthly Active Users)
- Application usage patterns known

## Clerk Pricing Model

### Pricing Tiers (as of 2024)

| Tier | MAU Included | Price | Features |
|------|--------------|-------|----------|
| Free | 10,000 | $0 | Basic auth, 5 social providers |
| Pro | 10,000 | $25/mo | Custom domain, priority support |
| Enterprise | Custom | Custom | SSO, SLA, dedicated support |

### Per-User Pricing (after included MAU)
- Pro: ~$0.02 per MAU above 10,000

### What Counts as MAU?
- Any user who signs in during the month
- Active session = counted
- Multiple sign-ins = counted once

## Cost Optimization Strategies

### Strategy 1: Reduce Unnecessary Sessions
```typescript
// lib/session-optimization.ts
import { auth } from '@clerk/nextjs/server'

// Use session efficiently - avoid creating multiple sessions
export async function getOrCreateSession() {
  const { userId, sessionId } = await auth()

  // Prefer existing session over creating new ones
  if (sessionId) {
    return { userId, sessionId, isNew: false }
  }

  // Only create session when absolutely needed
  return { userId, sessionId: null, isNew: true }
}

// Configure session lifetime appropriately
// Clerk Dashboard > Configure > Sessions
// Longer sessions = fewer re-authentications
```

### Strategy 2: Implement Guest Users
```typescript
// lib/guest-users.ts
// Use guest mode for non-essential features to reduce MAU

export function useGuestOrAuth() {
  const { userId, isLoaded, isSignedIn } = useUser()

  // Allow limited functionality without sign-in
  const guestId = useMemo(() => {
    if (typeof window === 'undefined') return null
    let id = localStorage.getItem('guest_id')
    if (!id) {
      id = crypto.randomUUID()
      localStorage.setItem('guest_id', id)
    }
    return id
  }, [])

  return {
    userId: isSignedIn ? userId : null,
    guestId: !isSignedIn ? guestId : null,
    isGuest: !isSignedIn && !!guestId,
    isLoaded
  }
}

// Use guest ID for features that don't require auth
export async function savePreference(key: string, value: any) {
  const { userId, guestId } = useGuestOrAuth()

  if (userId) {
    // Authenticated - save to user profile
    await saveToUserProfile(userId, key, value)
  } else if (guestId) {
    // Guest - save to localStorage (no Clerk MAU cost)
    localStorage.setItem(`pref_${key}`, JSON.stringify(value))
  }
}
```

### Strategy 3: Defer Authentication
```typescript
// Delay requiring sign-in until necessary
'use client'
import { useUser, SignInButton } from '@clerk/nextjs'

export function FeatureGate({ children, requiresAuth = false }) {
  const { isSignedIn, isLoaded } = useUser()

  // If feature doesn't require auth, show it
  if (!requiresAuth) {
    return children
  }

  if (!isLoaded) {
    return <Skeleton />
  }

  if (!isSignedIn) {
    return (
      <div className="p-4 border rounded">
        <p>Sign in to access this feature</p>
        <SignInButton mode="modal">
          <button className="btn">Sign In</button>
        </SignInButton>
      </div>
    )
  }

  return children
}

// Usage - only count MAU when user accesses premium features
function App() {
  return (
    <div>
      {/* Free features - no sign-in required */}
      <PublicContent />

      {/* Premium features - sign-in required */}
      <FeatureGate requiresAuth>
        <PremiumContent />
      </FeatureGate>
    </div>
  )
}
```

### Strategy 4: Reduce API Calls
```typescript
// lib/batched-clerk.ts
import { clerkClient } from '@clerk/nextjs/server'

// Batch user lookups to reduce API calls
export async function batchGetUsers(userIds: string[]) {
  if (userIds.length === 0) return []

  const client = await clerkClient()

  // Single API call instead of multiple getUser calls
  const { data: users } = await client.users.getUserList({
    userId: userIds,
    limit: 100
  })

  return users
}

// Cache organization data
const orgCache = new Map<string, any>()

export async function getOrganization(orgId: string) {
  if (orgCache.has(orgId)) {
    return orgCache.get(orgId)
  }

  const client = await clerkClient()
  const org = await client.organizations.getOrganization({ organizationId: orgId })

  orgCache.set(orgId, org)
  return org
}
```

### Strategy 5: Monitor and Alert
```typescript
// lib/cost-monitoring.ts
import { clerkClient } from '@clerk/nextjs/server'

export async function getMonthlyUsageEstimate() {
  const client = await clerkClient()

  // Get unique users this month
  const startOfMonth = new Date()
  startOfMonth.setDate(1)
  startOfMonth.setHours(0, 0, 0, 0)

  const { totalCount } = await client.users.getUserList({
    limit: 1,
    // Note: You may need to track this yourself
  })

  // Estimate cost
  const includedMAU = 10000 // Pro tier
  const extraUsers = Math.max(0, totalCount - includedMAU)
  const estimatedCost = 25 + (extraUsers * 0.02)

  return {
    totalUsers: totalCount,
    includedMAU,
    extraUsers,
    estimatedCost,
    percentageUsed: (totalCount / includedMAU) * 100
  }
}

// Alert when approaching limits
export async function checkUsageAlerts() {
  const usage = await getMonthlyUsageEstimate()

  if (usage.percentageUsed > 80) {
    await sendAlert(`Clerk usage at ${usage.percentageUsed}% of included MAU`)
  }
}
```

## Cost Reduction Checklist

- [ ] Review session lifetime settings (longer = fewer re-auths)
- [ ] Implement guest mode for non-essential features
- [ ] Defer authentication until necessary
- [ ] Batch API calls
- [ ] Cache user/org data aggressively
- [ ] Monitor MAU usage regularly
- [ ] Remove inactive users periodically
- [ ] Use webhooks instead of polling

## Pricing Calculator

```typescript
// Calculate monthly cost
function estimateMonthlyCost(
  tier: 'free' | 'pro' | 'enterprise',
  expectedMAU: number
): number {
  switch (tier) {
    case 'free':
      return expectedMAU <= 10000 ? 0 : Infinity // Upgrade required
    case 'pro':
      const includedMAU = 10000
      const basePrice = 25
      const extraUsers = Math.max(0, expectedMAU - includedMAU)
      return basePrice + (extraUsers * 0.02)
    case 'enterprise':
      return -1 // Contact sales
  }
}

// Examples
console.log(estimateMonthlyCost('pro', 5000))   // $25
console.log(estimateMonthlyCost('pro', 20000))  // $225
console.log(estimateMonthlyCost('pro', 100000)) // $1825
```

## Output
- Pricing model understood
- Cost optimization strategies implemented
- Usage monitoring configured
- Budget alerts set up

## Error Handling
| Issue | Cause | Solution |
|-------|-------|----------|
| Unexpected bill | MAU spike | Implement usage monitoring |
| Feature limitations | Free tier limits | Upgrade to Pro |
| API limits | Heavy usage | Implement caching |

## Resources
- [Clerk Pricing](https://clerk.com/pricing)
- [Usage Dashboard](https://dashboard.clerk.com/usage)
- [Fair Use Policy](https://clerk.com/docs/deployments/fair-use-policy)

## Next Steps
Proceed to `clerk-reference-architecture` for architecture patterns.
