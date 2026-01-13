# Examples

### Environment Switching
```typescript
// lib/clerk.ts
export const clerkConfig = {
  publishableKey: process.env.NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY!,
  signInUrl: process.env.NEXT_PUBLIC_CLERK_SIGN_IN_URL || '/sign-in',
  signUpUrl: process.env.NEXT_PUBLIC_CLERK_SIGN_UP_URL || '/sign-up',
}

// Validate configuration
if (!clerkConfig.publishableKey.startsWith('pk_')) {
  throw new Error('Invalid Clerk publishable key')
}
```

### Local Webhook Testing
```bash
# Use ngrok or similar for webhook testing
npx ngrok http 3000

# Update webhook URL in Clerk dashboard to ngrok URL
# https://abc123.ngrok.io/api/webhooks/clerk
```