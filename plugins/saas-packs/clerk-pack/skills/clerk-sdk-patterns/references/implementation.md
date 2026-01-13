# Implementation Guide

### Pattern 1: Server-Side Authentication
```typescript
// app/api/protected/route.ts
import { auth, currentUser } from '@clerk/nextjs/server'

export async function GET() {
  // Quick auth check
  const { userId, sessionId, orgId } = await auth()

  if (!userId) {
    return Response.json({ error: 'Unauthorized' }, { status: 401 })
  }

  // Full user data when needed
  const user = await currentUser()

  return Response.json({
    userId,
    sessionId,
    orgId,
    email: user?.primaryEmailAddress?.emailAddress
  })
}
```

### Pattern 2: Client-Side Hooks
```typescript
'use client'
import { useUser, useAuth, useClerk, useSession } from '@clerk/nextjs'

export function AuthenticatedComponent() {
  // User data and loading state
  const { user, isLoaded, isSignedIn } = useUser()

  // Auth utilities
  const { userId, getToken, signOut } = useAuth()

  // Full Clerk instance
  const clerk = useClerk()

  // Session info
  const { session } = useSession()

  // Get JWT token for API calls
  const callExternalAPI = async () => {
    const token = await getToken({ template: 'supabase' }) // or custom template
    const res = await fetch('https://api.example.com', {
      headers: { Authorization: `Bearer ${token}` }
    })
  }

  if (!isLoaded) return <div>Loading...</div>
  if (!isSignedIn) return <div>Please sign in</div>

  return <div>Welcome, {user.firstName}</div>
}
```

### Pattern 3: Protected Routes with Middleware
```typescript
// middleware.ts
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'

const isPublicRoute = createRouteMatcher([
  '/',
  '/sign-in(.*)',
  '/sign-up(.*)',
  '/api/webhooks(.*)'
])

const isProtectedRoute = createRouteMatcher([
  '/dashboard(.*)',
  '/api/protected(.*)'
])

export default clerkMiddleware(async (auth, request) => {
  if (isProtectedRoute(request)) {
    await auth.protect()
  }
})

export const config = {
  matcher: ['/((?!.*\\..*|_next).*)', '/', '/(api|trpc)(.*)']
}
```

### Pattern 4: Organization-Aware Queries
```typescript
import { auth } from '@clerk/nextjs/server'

export async function GET() {
  const { userId, orgId, orgRole } = await auth()

  // Check organization membership
  if (!orgId) {
    return Response.json({ error: 'No organization selected' }, { status: 400 })
  }

  // Check role-based access
  if (orgRole !== 'org:admin') {
    return Response.json({ error: 'Admin access required' }, { status: 403 })
  }

  // Query with organization scope
  const data = await db.query.resources.findMany({
    where: eq(resources.organizationId, orgId)
  })

  return Response.json(data)
}
```

### Pattern 5: Custom JWT Templates
```typescript
// Use custom JWT claims for external services
const { getToken } = useAuth()

// Standard Clerk token
const clerkToken = await getToken()

// Custom template for Supabase
const supabaseToken = await getToken({ template: 'supabase' })

// Custom template for Hasura
const hasuraToken = await getToken({ template: 'hasura' })
```