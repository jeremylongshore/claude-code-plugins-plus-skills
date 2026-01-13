# Implementation Guide

### Step 1: Install SDK
```bash
# Next.js
npm install @clerk/nextjs

# React
npm install @clerk/clerk-react

# Express/Node.js
npm install @clerk/express

# Remix
npm install @clerk/remix
```

### Step 2: Configure Environment Variables
```bash
# Create .env.local file
cat >> .env.local << 'EOF'
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=pk_test_...
CLERK_SECRET_KEY=sk_test_...
EOF
```

### Step 3: Add ClerkProvider (Next.js App Router)
```typescript
// app/layout.tsx
import { ClerkProvider } from '@clerk/nextjs'

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <ClerkProvider>
      <html lang="en">
        <body>{children}</body>
      </html>
    </ClerkProvider>
  )
}
```

### Step 4: Add Middleware
```typescript
// middleware.ts
import { clerkMiddleware } from '@clerk/nextjs/server'

export default clerkMiddleware()

export const config = {
  matcher: [
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    '/(api|trpc)(.*)',
  ],
}
```

### Step 5: Verify Connection
```typescript
import { auth } from '@clerk/nextjs/server'

export async function GET() {
  const { userId } = await auth()
  return Response.json({ authenticated: !!userId })
}
```