# Sso Integration

## SSO Integration

### SAML Configuration

```typescript
// PostHog SAML setup
const samlConfig = {
  entryPoint: 'https://idp.company.com/saml/sso',
  issuer: 'https://posthog.com/saml/metadata',
  cert: process.env.SAML_CERT,
  callbackUrl: 'https://app.yourcompany.com/auth/posthog/callback',
};

// Map IdP groups to PostHog roles
const groupRoleMapping: Record<string, PostHogRole> = {
  'Engineering': PostHogRole.Developer,
  'Platform-Admins': PostHogRole.Admin,
  'Data-Team': PostHogRole.Viewer,
};
```

### OAuth2/OIDC Integration

```typescript
import { OAuth2Client } from '@posthog/sdk';

const oauthClient = new OAuth2Client({
  clientId: process.env.POSTHOG_OAUTH_CLIENT_ID!,
  clientSecret: process.env.POSTHOG_OAUTH_CLIENT_SECRET!,
  redirectUri: 'https://app.yourcompany.com/auth/posthog/callback',
  scopes: ['read', 'write'],
});
```