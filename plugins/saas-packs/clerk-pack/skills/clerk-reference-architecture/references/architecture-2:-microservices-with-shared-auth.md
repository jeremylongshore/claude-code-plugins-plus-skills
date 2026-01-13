# Architecture 2: Microservices With Shared Auth

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