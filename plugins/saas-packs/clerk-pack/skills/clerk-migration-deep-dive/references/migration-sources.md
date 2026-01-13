# Migration Sources

## Migration Sources

### 1. Auth0 to Clerk

#### Step 1: Export Users from Auth0
```bash
# Using Auth0 Management API
curl -X GET "https://YOUR_DOMAIN.auth0.com/api/v2/users" \
  -H "Authorization: Bearer YOUR_MGMT_TOKEN" \
  -H "Content-Type: application/json" \
  > auth0-users.json
```

#### Step 2: Transform User Data
```typescript
// scripts/transform-auth0-users.ts
interface Auth0User {
  user_id: string
  email: string
  email_verified: boolean
  name: string
  given_name?: string
  family_name?: string
  picture?: string
  created_at: string
  last_login?: string
}

interface ClerkImportUser {
  external_id: string
  email_addresses: Array<{
    email_address: string
    verified: boolean
  }>
  first_name?: string
  last_name?: string
  image_url?: string
  created_at: string
  public_metadata?: Record<string, any>
}

function transformAuth0ToClerk(auth0User: Auth0User): ClerkImportUser {
  return {
    external_id: auth0User.user_id,
    email_addresses: [{
      email_address: auth0User.email,
      verified: auth0User.email_verified
    }],
    first_name: auth0User.given_name,
    last_name: auth0User.family_name,
    image_url: auth0User.picture,
    created_at: auth0User.created_at,
    public_metadata: {
      migrated_from: 'auth0',
      migrated_at: new Date().toISOString()
    }
  }
}
```

#### Step 3: Import to Clerk
```typescript
// scripts/import-to-clerk.ts
import { clerkClient } from '@clerk/nextjs/server'

async function importUsers(users: ClerkImportUser[]) {
  const client = await clerkClient()
  const results = { success: 0, failed: 0, errors: [] as string[] }

  for (const user of users) {
    try {
      await client.users.createUser({
        externalId: user.external_id,
        emailAddress: [user.email_addresses[0].email_address],
        firstName: user.first_name,
        lastName: user.last_name,
        publicMetadata: user.public_metadata,
        skipPasswordRequirement: true // User will set password on first login
      })
      results.success++
    } catch (error: any) {
      results.failed++
      results.errors.push(`${user.external_id}: ${error.message}`)
    }

    // Rate limiting
    await new Promise(r => setTimeout(r, 100))
  }

  return results
}
```

### 2. Firebase Auth to Clerk

#### Step 1: Export from Firebase
```typescript
// scripts/export-firebase-users.ts
import * as admin from 'firebase-admin'

admin.initializeApp({
  credential: admin.credential.cert(require('./service-account.json'))
})

async function exportFirebaseUsers() {
  const users: admin.auth.UserRecord[] = []
  let nextPageToken: string | undefined

  do {
    const result = await admin.auth().listUsers(1000, nextPageToken)
    users.push(...result.users)
    nextPageToken = result.pageToken
  } while (nextPageToken)

  return users
}
```

#### Step 2: Transform and Import
```typescript
// scripts/migrate-firebase-to-clerk.ts
import { clerkClient } from '@clerk/nextjs/server'

interface FirebaseUser {
  uid: string
  email?: string
  emailVerified: boolean
  displayName?: string
  photoURL?: string
  phoneNumber?: string
  disabled: boolean
  metadata: {
    creationTime: string
    lastSignInTime: string
  }
  providerData: Array<{
    providerId: string
    uid: string
  }>
}

async function migrateFirebaseUsers(firebaseUsers: FirebaseUser[]) {
  const client = await clerkClient()

  for (const fbUser of firebaseUsers) {
    if (fbUser.disabled || !fbUser.email) continue

    try {
      await client.users.createUser({
        externalId: fbUser.uid,
        emailAddress: [fbUser.email],
        firstName: fbUser.displayName?.split(' ')[0],
        lastName: fbUser.displayName?.split(' ').slice(1).join(' '),
        publicMetadata: {
          migrated_from: 'firebase',
          firebase_uid: fbUser.uid,
          providers: fbUser.providerData.map(p => p.providerId)
        },
        skipPasswordRequirement: true
      })
    } catch (error) {
      console.error(`Failed to migrate ${fbUser.uid}:`, error)
    }
  }
}
```

### 3. NextAuth.js to Clerk

#### Step 1: Database Migration
```typescript
// scripts/migrate-nextauth-db.ts
// Assuming Prisma with NextAuth schema

async function migrateNextAuthUsers() {
  // Get all users from NextAuth database
  const nextAuthUsers = await prisma.user.findMany({
    include: {
      accounts: true,
      sessions: true
    }
  })

  const client = await clerkClient()

  for (const user of nextAuthUsers) {
    try {
      // Create user in Clerk
      const clerkUser = await client.users.createUser({
        externalId: user.id,
        emailAddress: user.email ? [user.email] : [],
        firstName: user.name?.split(' ')[0],
        lastName: user.name?.split(' ').slice(1).join(' '),
        publicMetadata: {
          migrated_from: 'nextauth',
          nextauth_id: user.id
        },
        skipPasswordRequirement: true
      })

      // Update local database with new Clerk ID
      await prisma.user.update({
        where: { id: user.id },
        data: { clerkId: clerkUser.id }
      })
    } catch (error) {
      console.error(`Failed to migrate ${user.id}:`, error)
    }
  }
}
```

#### Step 2: Update Application Code
```typescript
// BEFORE: NextAuth
import { getSession } from 'next-auth/react'

export async function getServerSideProps(context) {
  const session = await getSession(context)
  if (!session) {
    return { redirect: { destination: '/login' } }
  }
  return { props: { user: session.user } }
}

// AFTER: Clerk
import { auth } from '@clerk/nextjs/server'

export async function getServerSideProps() {
  const { userId } = await auth()
  if (!userId) {
    return { redirect: { destination: '/sign-in' } }
  }
  const user = await currentUser()
  return { props: { user } }
}
```

### 4. Supabase Auth to Clerk

#### Step 1: Export Supabase Users
```typescript
// scripts/export-supabase-users.ts
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  process.env.SUPABASE_URL!,
  process.env.SUPABASE_SERVICE_KEY! // Service key for admin access
)

async function exportSupabaseUsers() {
  const { data: { users }, error } = await supabase.auth.admin.listUsers()

  if (error) throw error

  return users
}
```

#### Step 2: Migrate to Clerk
```typescript
// scripts/migrate-supabase-to-clerk.ts
async function migrateSupabaseUsers() {
  const supabaseUsers = await exportSupabaseUsers()
  const client = await clerkClient()

  for (const sbUser of supabaseUsers) {
    try {
      await client.users.createUser({
        externalId: sbUser.id,
        emailAddress: sbUser.email ? [sbUser.email] : [],
        phoneNumber: sbUser.phone ? [sbUser.phone] : [],
        publicMetadata: {
          migrated_from: 'supabase',
          supabase_id: sbUser.id,
          user_metadata: sbUser.user_metadata
        },
        skipPasswordRequirement: true
      })
    } catch (error) {
      console.error(`Failed to migrate ${sbUser.id}:`, error)
    }
  }
}
```