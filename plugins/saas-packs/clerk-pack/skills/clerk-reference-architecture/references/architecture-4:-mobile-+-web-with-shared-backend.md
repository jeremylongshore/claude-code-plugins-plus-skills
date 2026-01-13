# Architecture 4: Mobile + Web With Shared Backend

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