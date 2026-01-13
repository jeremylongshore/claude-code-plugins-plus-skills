# Architecture 3: Multi-Tenant Saas

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