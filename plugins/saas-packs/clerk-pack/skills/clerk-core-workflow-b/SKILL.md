---
name: clerk-core-workflow-b
license: MIT
allowed-tools: Read, Write, Edit, Grep
description: Implement session management and middleware with clerk. use when managing
  user sessions, configuring route protection, or implementing token refresh logic.
  trigger with phrases like "clerk session", "clerk middleware", "clerk route protection",
  "c...
---
# Clerk Core Workflow B: Session & Middleware

## Overview
Manage user sessions, protect routes with middleware, and handle JWT tokens.

## Prerequisites
- Clerk SDK installed and configured
- Authentication flows implemented
- Understanding of Next.js middleware

## Instructions

### Step 1: Advanced Middleware Configuration
```typescript
// middleware.ts
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'
import { NextResponse } from 'next/server'

const isPublicRoute = createRouteMatcher([
  '/',
  '/sign-in(.*)',
  '/sign-up(.*)',
  '/api/webhooks(.*)',
  '/api/public(.*)'
])

const isAdminRoute = createRouteMatcher(['/admin(.*)'])
const isAPIRoute = createRouteMatcher(['/api/(.*)'])

export default clerkMiddleware(async (auth, request) => {
  const { userId, orgRole, sessionClaims } = await auth()

  // Allow public routes
  if (isPublicRoute(request)) {
    return NextResponse.next()
  }

  // Require authentication for all other routes
  if (!userId) {
    const signInUrl = new URL('/sign-in', request.url)
    signInUrl.searchParams.set('redirect_url', request.url)
    return NextResponse.redirect(signInUrl)
  }

  // Admin route protection
  if (isAdminRoute(request)) {
    if (orgRole !== 'org:admin') {
      return NextResponse.redirect(new URL('/unauthorized', request.url))
    }
  }

  // Add custom headers for API routes
  if (isAPIRoute(request)) {
    const response = NextResponse.next()
    response.headers.set('x-user-id', userId)
    return response
  }

  return NextResponse.next()
})

export const config = {
  matcher: ['/((?!_next|[^?]*\\.(?:html?|css|js|jpe?g|webp|png|gif|svg|ttf|woff2?|ico)).*)', '/']
}
```

### Step 2: Session Management
```typescript
'use client'
import { useSession, useAuth } from '@clerk/nextjs'

export function SessionManager() {
  const { session, isLoaded } = useSession()
  const { signOut } = useAuth()

  if (!isLoaded) return <div>Loading session...</div>
  if (!session) return <div>No active session</div>

  const handleSignOutAll = async () => {
    // Sign out from all devices
    await signOut({ sessionId: 'all' })
  }

  const handleSignOutCurrent = async () => {
    // Sign out from current session only
    await signOut()
  }

  return (
    <div>
      <h2>Session Info</h2>
      <p>Session ID: {session.id}</p>
      <p>Created: {new Date(session.createdAt).toLocaleString()}</p>
      <p>Last Active: {new Date(session.lastActiveAt).toLocaleString()}</p>
      <p>Expires: {new Date(session.expireAt).toLocaleString()}</p>

      <div className="space-x-2">
        <button onClick={handleSignOutCurrent}>Sign Out</button>
        <button onClick={handleSignOutAll}>Sign Out All Devices</button>
      </div>
    </div>
  )
}
```

### Step 3: Token Management
```typescript
'use client'
import { useAuth } from '@clerk/nextjs'

export function useClerkToken() {
  const { getToken, isLoaded, isSignedIn } = useAuth()

  const fetchWithAuth = async (url: string, options: RequestInit = {}) => {
    if (!isLoaded || !isSignedIn) {
      throw new Error('Not authenticated')
    }

    const token = await getToken()

    return fetch(url, {
      ...options,
      headers: {
        ...options.headers,
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    })
  }

  const fetchWithCustomTemplate = async (url: string, template: string) => {
    const token = await getToken({ template })

    return fetch(url, {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
  }

  return { fetchWithAuth, fetchWithCustomTemplate, getToken }
}
```

### Step 4: Server-Side Session Validation
```typescript
// app/api/protected/route.ts
import { auth } from '@clerk/nextjs/server'
import { headers } from 'next/headers'

export async function GET() {
  const { userId, sessionId, sessionClaims } = await auth()

  if (!userId) {
    return Response.json({ error: 'Unauthorized' }, { status: 401 })
  }

  // Access session claims
  const email = sessionClaims?.email as string
  const role = sessionClaims?.metadata?.role as string

  // Validate session freshness
  const sessionAge = Date.now() - (sessionClaims?.iat ?? 0) * 1000
  const maxAge = 60 * 60 * 1000 // 1 hour

  if (sessionAge > maxAge) {
    return Response.json({ error: 'Session expired' }, { status: 401 })
  }

  return Response.json({
    userId,
    sessionId,
    email,
    role
  })
}
```

### Step 5: Multi-Session Support
```typescript
'use client'
import { useSessionList, useSession } from '@clerk/nextjs'

export function SessionList() {
  const { sessions, isLoaded, setActive } = useSessionList()
  const { session: currentSession } = useSession()

  if (!isLoaded) return <div>Loading sessions...</div>

  return (
    <div>
      <h2>Active Sessions</h2>
      <ul>
        {sessions?.map((session) => (
          <li key={session.id}>
            <span>{session.id}</span>
            <span>{session.id === currentSession?.id ? ' (current)' : ''}</span>
            <button onClick={() => setActive({ session: session.id })}>
              Switch
            </button>
            <button onClick={() => session.remove()}>
              Revoke
            </button>
          </li>
        ))}
      </ul>
    </div>
  )
}
```

## Output
- Protected routes with middleware
- Session management UI
- Token refresh handling
- Multi-session support

## Error Handling
| Error | Cause | Solution |
|-------|-------|----------|
| Session not found | Expired or revoked | Redirect to sign-in |
| Token expired | JWT lifetime exceeded | Call getToken() for fresh token |
| Middleware loop | Incorrect matcher | Check matcher regex excludes static files |
| Headers already sent | Response already started | Check middleware order |

## Examples

### Rate-Limited Middleware
```typescript
import { clerkMiddleware } from '@clerk/nextjs/server'
import { Ratelimit } from '@upstash/ratelimit'
import { Redis } from '@upstash/redis'

const ratelimit = new Ratelimit({
  redis: Redis.fromEnv(),
  limiter: Ratelimit.slidingWindow(10, '10 s')
})

export default clerkMiddleware(async (auth, request) => {
  const { userId } = await auth()

  if (userId) {
    const { success } = await ratelimit.limit(userId)
    if (!success) {
      return Response.json({ error: 'Rate limited' }, { status: 429 })
    }
  }
})
```

## Resources
- [Middleware Guide](https://clerk.com/docs/references/nextjs/clerk-middleware)
- [Session Management](https://clerk.com/docs/authentication/configuration/session-options)
- [JWT Templates](https://clerk.com/docs/backend-requests/making/jwt-templates)

## Next Steps
Proceed to `clerk-common-errors` for troubleshooting common issues.
