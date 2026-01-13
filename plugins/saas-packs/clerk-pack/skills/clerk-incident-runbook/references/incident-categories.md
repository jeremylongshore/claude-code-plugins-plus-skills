# Incident Categories

## Incident Categories

### Category 1: Complete Auth Outage
**Symptoms:** All users unable to sign in, middleware returning errors

**Immediate Actions:**
```bash
# 1. Check Clerk status
curl -s https://status.clerk.com/api/v1/status | jq

# 2. Check your endpoint
curl -I https://yourapp.com/api/health/clerk

# 3. Check environment variables
vercel env ls | grep CLERK
```

**Mitigation Steps:**
```typescript
// Emergency bypass mode (use with caution)
// middleware.ts
import { clerkMiddleware } from '@clerk/nextjs/server'
import { NextResponse } from 'next/server'

const EMERGENCY_BYPASS = process.env.CLERK_EMERGENCY_BYPASS === 'true'

export default clerkMiddleware(async (auth, request) => {
  if (EMERGENCY_BYPASS) {
    // Log for audit
    console.warn('[EMERGENCY] Auth bypass active', {
      path: request.nextUrl.pathname,
      timestamp: new Date().toISOString()
    })
    return NextResponse.next()
  }

  // Normal auth flow
  await auth.protect()
})
```

### Category 2: Webhook Processing Failure
**Symptoms:** User data out of sync, missing user records

**Diagnosis:**
```bash
# Check webhook endpoint
curl -X POST https://yourapp.com/api/webhooks/clerk \
  -H "Content-Type: application/json" \
  -d '{"type":"ping"}' \
  -w "\n%{http_code}"

# Check Clerk dashboard for failed webhooks
# Dashboard > Webhooks > Failed Deliveries
```

**Recovery:**
```typescript
// scripts/resync-users.ts
import { clerkClient } from '@clerk/nextjs/server'
import { db } from '../lib/db'

async function resyncAllUsers() {
  const client = await clerkClient()
  let offset = 0
  const limit = 100

  while (true) {
    const { data: users, totalCount } = await client.users.getUserList({
      limit,
      offset
    })

    for (const user of users) {
      await db.user.upsert({
        where: { clerkId: user.id },
        update: {
          email: user.emailAddresses[0]?.emailAddress,
          firstName: user.firstName,
          lastName: user.lastName,
          updatedAt: new Date()
        },
        create: {
          clerkId: user.id,
          email: user.emailAddresses[0]?.emailAddress,
          firstName: user.firstName,
          lastName: user.lastName
        }
      })
    }

    console.log(`Synced ${offset + users.length} of ${totalCount} users`)
    offset += limit

    if (offset >= totalCount) break
  }

  console.log('Resync complete')
}

resyncAllUsers()
```

### Category 3: Security Incident
**Symptoms:** Unauthorized access detected, suspicious sessions

**Immediate Actions:**
```typescript
// scripts/emergency-session-revoke.ts
import { clerkClient } from '@clerk/nextjs/server'

async function revokeUserSessions(userId: string) {
  const client = await clerkClient()

  // Get all active sessions
  const sessions = await client.sessions.getSessionList({
    userId,
    status: 'active'
  })

  // Revoke all sessions
  for (const session of sessions.data) {
    await client.sessions.revokeSession(session.id)
    console.log(`Revoked session: ${session.id}`)
  }

  console.log(`Revoked ${sessions.data.length} sessions for user ${userId}`)
}

// Revoke all sessions for compromised user
revokeUserSessions('user_xxx')
```

```typescript
// scripts/emergency-lockout.ts
import { clerkClient } from '@clerk/nextjs/server'

async function lockoutUser(userId: string) {
  const client = await clerkClient()

  // Ban user (prevents new sign-ins)
  await client.users.banUser(userId)

  // Revoke all sessions
  const sessions = await client.sessions.getSessionList({
    userId,
    status: 'active'
  })

  for (const session of sessions.data) {
    await client.sessions.revokeSession(session.id)
  }

  console.log(`User ${userId} locked out and all sessions revoked`)
}
```

### Category 4: Performance Degradation
**Symptoms:** Slow sign-in, high latency, timeouts

**Diagnosis:**
```typescript
// scripts/diagnose-performance.ts
async function diagnosePerformance() {
  const results = {
    authCheck: 0,
    getUserList: 0,
    currentUser: 0
  }

  // Measure auth check
  const authStart = performance.now()
  await auth()
  results.authCheck = performance.now() - authStart

  // Measure API call
  const apiStart = performance.now()
  const client = await clerkClient()
  await client.users.getUserList({ limit: 1 })
  results.getUserList = performance.now() - apiStart

  // Measure currentUser
  const userStart = performance.now()
  await currentUser()
  results.currentUser = performance.now() - userStart

  console.log('Performance Diagnosis:', results)

  // Check for issues
  if (results.authCheck > 100) {
    console.warn('Auth check slow - check middleware configuration')
  }
  if (results.getUserList > 500) {
    console.warn('API slow - check Clerk status or network')
  }

  return results
}
```