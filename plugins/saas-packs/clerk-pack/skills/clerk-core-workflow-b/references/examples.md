# Examples

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