# Examples

### Magic Link Authentication
```typescript
const handleMagicLink = async (email: string) => {
  await signIn.create({
    identifier: email,
    strategy: 'email_link',
    redirectUrl: `${window.location.origin}/verify-magic-link`
  })
}

// app/verify-magic-link/page.tsx
import { EmailLinkComplete } from '@clerk/nextjs'

export default function VerifyMagicLink() {
  return <EmailLinkComplete />
}
```