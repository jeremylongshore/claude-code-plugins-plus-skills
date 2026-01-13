# Examples

### Using with React Hooks
```typescript
'use client'
import { useUser, useClerk } from '@clerk/nextjs'

export function UserProfile() {
  const { user } = useUser()
  const { signOut } = useClerk()

  return (
    <div>
      <img src={user?.imageUrl} alt="Profile" />
      <h2>{user?.fullName}</h2>
      <button onClick={() => signOut()}>Sign Out</button>
    </div>
  )
}
```

### Express.js Example
```typescript
import { clerkMiddleware, requireAuth } from '@clerk/express'

app.use(clerkMiddleware())

app.get('/api/protected', requireAuth(), (req, res) => {
  res.json({
    message: 'Hello!',
    userId: req.auth.userId
  })
})
```