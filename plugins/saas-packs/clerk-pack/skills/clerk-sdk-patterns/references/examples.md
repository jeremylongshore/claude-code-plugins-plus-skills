# Examples

### Complete Protected Page Pattern
```typescript
// app/dashboard/page.tsx
import { auth, currentUser } from '@clerk/nextjs/server'
import { redirect } from 'next/navigation'

export default async function DashboardPage() {
  const { userId } = await auth()

  if (!userId) {
    redirect('/sign-in')
  }

  const user = await currentUser()

  return (
    <main>
      <h1>Dashboard</h1>
      <UserProfile user={user} />
      <DashboardContent userId={userId} />
    </main>
  )
}
```

### Typed User Metadata
```typescript
// types/clerk.d.ts
interface UserPublicMetadata {
  tier: 'free' | 'pro' | 'enterprise'
  onboarded: boolean
}

interface UserPrivateMetadata {
  stripeCustomerId?: string
}

// Usage
const user = await currentUser()
const tier = user?.publicMetadata?.tier ?? 'free'
```