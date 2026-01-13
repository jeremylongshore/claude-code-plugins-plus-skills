# Implementation Guide

### Step 1: Create Protected Page
```typescript
// app/dashboard/page.tsx
import { auth, currentUser } from '@clerk/nextjs/server'

export default async function DashboardPage() {
  const { userId } = await auth()
  const user = await currentUser()

  if (!userId) {
    return <div>Please sign in to access this page</div>
  }

  return (
    <div>
      <h1>Hello, {user?.firstName || 'User'}!</h1>
      <p>Your user ID: {userId}</p>
      <p>Email: {user?.emailAddresses[0]?.emailAddress}</p>
    </div>
  )
}
```

### Step 2: Create Protected API Route
```typescript
// app/api/hello/route.ts
import { auth } from '@clerk/nextjs/server'

export async function GET() {
  const { userId } = await auth()

  if (!userId) {
    return Response.json({ error: 'Unauthorized' }, { status: 401 })
  }

  return Response.json({
    message: 'Hello from Clerk!',
    userId,
    timestamp: new Date().toISOString()
  })
}
```

### Step 3: Test Authentication Flow
```typescript
// Client-side test component
'use client'
import { useUser, useAuth } from '@clerk/nextjs'

export function AuthTest() {
  const { user, isLoaded, isSignedIn } = useUser()
  const { getToken } = useAuth()

  if (!isLoaded) return <div>Loading...</div>
  if (!isSignedIn) return <div>Not signed in</div>

  const testAPI = async () => {
    const token = await getToken()
    const res = await fetch('/api/hello', {
      headers: { Authorization: `Bearer ${token}` }
    })
    console.log(await res.json())
  }

  return (
    <div>
      <p>Signed in as: {user.primaryEmailAddress?.emailAddress}</p>
      <button onClick={testAPI}>Test API</button>
    </div>
  )
}
```