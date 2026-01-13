# Architecture 1: Next.Js Full-Stack Application

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