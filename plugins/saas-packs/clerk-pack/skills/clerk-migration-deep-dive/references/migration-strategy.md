# Migration Strategy

## Migration Strategy

### Phase 1: Preparation
```markdown
- [ ] Audit current user base
- [ ] Document all authentication flows
- [ ] Plan data mapping
- [ ] Set up Clerk development instance
- [ ] Create migration scripts
- [ ] Test with sample users
```

### Phase 2: Parallel Running
```typescript
// middleware.ts - Support both auth systems during migration
import { clerkMiddleware } from '@clerk/nextjs/server'
import { legacyAuth } from './legacy-auth'

export default async function middleware(request: NextRequest) {
  // Check Clerk first
  const clerkAuth = await clerkMiddleware(request)
  if (clerkAuth.userId) {
    return clerkAuth
  }

  // Fall back to legacy auth during migration
  const legacySession = await legacyAuth(request)
  if (legacySession) {
    // Log for migration tracking
    console.log('Legacy auth used:', legacySession.userId)
    return legacySession
  }

  return NextResponse.redirect('/sign-in')
}
```

### Phase 3: User Migration
```typescript
// Migrate users on first Clerk login
export async function POST(request: Request) {
  const { email, legacyToken } = await request.json()

  // Verify with legacy system
  const legacyUser = await verifyLegacyToken(legacyToken)
  if (!legacyUser) {
    return Response.json({ error: 'Invalid legacy token' }, { status: 401 })
  }

  // Check if already migrated
  const client = await clerkClient()
  const { data: existingUsers } = await client.users.getUserList({
    emailAddress: [email]
  })

  if (existingUsers.length > 0) {
    return Response.json({ migrated: true, userId: existingUsers[0].id })
  }

  // Create in Clerk
  const clerkUser = await client.users.createUser({
    emailAddress: [email],
    firstName: legacyUser.firstName,
    lastName: legacyUser.lastName,
    publicMetadata: {
      migrated_from: 'legacy',
      legacy_id: legacyUser.id
    }
  })

  return Response.json({ migrated: true, userId: clerkUser.id })
}
```

### Phase 4: Cutover
```markdown
- [ ] Disable new registrations on legacy system
- [ ] Migrate remaining users
- [ ] Update DNS/redirects
- [ ] Remove legacy auth code
- [ ] Decommission legacy system
```