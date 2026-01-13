---
name: clerk-reference-architecture
license: MIT
allowed-tools: Read, Write, Edit, Grep
description: Reference architecture patterns for clerk authentication. use when designing
  application architecture, planning auth flows, or implementing enterprise-grade
  authentication. trigger with phrases like "clerk architecture", "clerk design",
  "clerk sys...
---
# Clerk Reference Architecture

## Overview
Reference architectures for implementing Clerk in various application types.

## Prerequisites
- Understanding of web application architecture
- Familiarity with authentication patterns
- Knowledge of your tech stack

## Architecture 1: Next.js Full-Stack Application

```
+------------------+     +------------------+     +------------------+
|   Next.js App    |     |  Clerk Service   |     |   Database       |
|  (App Router)    |     |                  |     |   (Postgres)     |
+------------------+     +------------------+     +------------------+
        |                        |                        |
        |  ClerkProvider         |                        |
        |  (wraps all pages)     |                        |
        v                        v                        v
+------------------+     +------------------+     +------------------+
|  Middleware      |<--->|  Auth API        |     |  Prisma Client   |
|  (clerkMiddleware)|    |  (JWT verify)    |     |                  |
+------------------+     +------------------+     +------------------+
        |                        |                        |
        v                        v                        v
+------------------+     +------------------+     +------------------+
|  Protected       |     |  Webhooks        |---->|  User Sync       |
|  Server Actions  |     |  (user events)   |     |  (user table)    |
+------------------+     +------------------+     +------------------+
```

### Implementation
```typescript
// app/layout.tsx
import { ClerkProvider } from '@clerk/nextjs'

export default function RootLayout({ children }) {
  return (
    <ClerkProvider>
      <html><body>{children}</body></html>
    </ClerkProvider>
  )
}

// middleware.ts
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'

const isPublicRoute = createRouteMatcher(['/', '/sign-in(.*)', '/sign-up(.*)'])

export default clerkMiddleware(async (auth, req) => {
  if (!isPublicRoute(req)) await auth.protect()
})

// lib/db.ts - User sync via webhooks
import { prisma } from './prisma'

export async function syncUserFromClerk(clerkUser: any) {
  await prisma.user.upsert({
    where: { clerkId: clerkUser.id },
    update: {
      email: clerkUser.email_addresses[0]?.email_address,
      name: `${clerkUser.first_name} ${clerkUser.last_name}`,
      imageUrl: clerkUser.image_url
    },
    create: {
      clerkId: clerkUser.id,
      email: clerkUser.email_addresses[0]?.email_address,
      name: `${clerkUser.first_name} ${clerkUser.last_name}`,
      imageUrl: clerkUser.image_url
    }
  })
}
```

## Architecture 2: Microservices with Shared Auth

```
+------------------+
|   API Gateway    |
|  (JWT Verify)    |
+------------------+
        |
        | Bearer Token
        v
+-------+-------+-------+-------+
|       |       |       |       |
v       v       v       v       v
+-----+ +-----+ +-----+ +-----+ +-----+
|User | |Order| |Pay  | |Inv  | |Notif|
|Svc  | |Svc  | |Svc  | |Svc  | |Svc  |
+-----+ +-----+ +-----+ +-----+ +-----+
   |       |       |       |       |
   v       v       v       v       v
+------------------------------------------+
|              Shared User Store           |
|           (Synced via Webhooks)          |
+------------------------------------------+
```

### Implementation
```typescript
// API Gateway - Verify Clerk JWT
// gateway/src/middleware/auth.ts
import { createClerkClient } from '@clerk/backend'

const clerk = createClerkClient({
  secretKey: process.env.CLERK_SECRET_KEY
})

export async function verifyToken(req: Request): Promise<JWTPayload | null> {
  const token = req.headers.get('authorization')?.replace('Bearer ', '')

  if (!token) return null

  try {
    const { sub: userId } = await clerk.verifyToken(token)
    return { userId }
  } catch {
    return null
  }
}

// Microservice - Trust gateway-verified user
// services/order/src/handlers/create-order.ts
export async function createOrder(req: AuthenticatedRequest) {
  const { userId } = req.auth // Set by gateway

  return await db.order.create({
    data: {
      userId,
      items: req.body.items,
      status: 'pending'
    }
  })
}
```

## Architecture 3: Multi-Tenant SaaS

```
+------------------+     +------------------+
|   Tenant A       |     |   Tenant B       |
|   (Org: acme)    |     |   (Org: globex)  |
+------------------+     +------------------+
        |                        |
        v                        v
+------------------------------------------+
|           Clerk Organizations            |
|  - Member management                     |
|  - Role-based permissions                |
|  - SSO per organization                  |
+------------------------------------------+
        |
        v
+------------------------------------------+
|           Application Layer              |
|  - Organization context in all queries   |
|  - Data isolation by orgId               |
+------------------------------------------+
        |
        v
+------------------------------------------+
|           Database (Multi-tenant)        |
|  - All tables have organizationId        |
|  - RLS policies enforce isolation        |
+------------------------------------------+
```

### Implementation
```typescript
// middleware.ts - Organization context
import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'

export default clerkMiddleware(async (auth, req) => {
  const { userId, orgId, orgRole } = await auth()

  if (!userId) {
    return auth.redirectToSignIn()
  }

  // Require organization for app routes
  if (req.nextUrl.pathname.startsWith('/app') && !orgId) {
    return Response.redirect(new URL('/select-organization', req.url))
  }
})

// lib/db-context.ts - Tenant-scoped queries
import { auth } from '@clerk/nextjs/server'
import { prisma } from './prisma'

export async function getTenantPrisma() {
  const { orgId } = await auth()

  if (!orgId) {
    throw new Error('Organization context required')
  }

  // Return prisma client with tenant filter
  return prisma.$extends({
    query: {
      $allOperations({ operation, args, query }) {
        // Inject orgId into all queries
        if ('where' in args) {
          args.where = { ...args.where, organizationId: orgId }
        }
        if ('data' in args) {
          args.data = { ...args.data, organizationId: orgId }
        }
        return query(args)
      }
    }
  })
}
```

## Architecture 4: Mobile + Web with Shared Backend

```
+-------------+  +-------------+  +-------------+
|   Web App   |  |  iOS App    |  | Android App |
| (Next.js)   |  | (Swift)     |  | (Kotlin)    |
+-------------+  +-------------+  +-------------+
       |               |               |
       v               v               v
+------------------------------------------+
|            Clerk SDKs                    |
| - @clerk/nextjs                          |
| - clerk-expo (React Native)              |
| - Native SDKs                            |
+------------------------------------------+
       |               |               |
       +-------+-------+-------+-------+
               |
               v
+------------------------------------------+
|         Shared API Backend               |
|  - Verify JWT from any platform          |
|  - Consistent user model                 |
+------------------------------------------+
```

### Implementation
```typescript
// Backend API - Platform-agnostic auth
// api/src/middleware/verify-clerk.ts
import { createClerkClient } from '@clerk/backend'

const clerk = createClerkClient({
  secretKey: process.env.CLERK_SECRET_KEY
})

export async function verifyRequest(req: Request) {
  const token = req.headers.get('authorization')?.replace('Bearer ', '')

  if (!token) {
    throw new Error('No token provided')
  }

  // Works with tokens from any Clerk SDK
  const { sub: userId, metadata } = await clerk.verifyToken(token)

  return {
    userId,
    platform: metadata?.platform || 'unknown'
  }
}
```

## Architecture Decision Matrix

| Use Case | Architecture | Key Components |
|----------|--------------|----------------|
| Simple SaaS | Full-stack Next.js | ClerkProvider, Middleware |
| Microservices | API Gateway + Services | JWT verification, User sync |
| Multi-tenant | Organization-based | Org context, RLS |
| Mobile + Web | Shared backend | Platform-agnostic JWT |
| Enterprise | SSO + RBAC | SAML/OIDC, Roles |

## Output
- Architecture pattern selected
- Component diagram defined
- Implementation patterns ready
- Data flow documented

## Best Practices

1. **Always sync users to local database** - Don't rely solely on Clerk API
2. **Use webhooks for real-time sync** - Don't poll for changes
3. **Implement organization context early** - Retrofitting is painful
4. **Cache aggressively** - Reduce Clerk API calls
5. **Plan for SSO** - Enterprise customers will need it

## Resources
- [Clerk Architecture Guide](https://clerk.com/docs/architecture)
- [Multi-tenant Patterns](https://clerk.com/docs/organizations/overview)
- [Backend Integration](https://clerk.com/docs/backend-requests/overview)

## Next Steps
Proceed to `clerk-multi-env-setup` for multi-environment configuration.
