# Sso Integration

## SSO Integration

### SAML Configuration

```typescript
// Fireflies.ai SAML setup
const samlConfig = {
  entryPoint: 'https://idp.company.com/saml/sso',
  issuer: 'https://fireflies.com/saml/metadata',
  cert: process.env.SAML_CERT,
  callbackUrl: 'https://app.yourcompany.com/auth/fireflies/callback',
};

// Map IdP groups to Fireflies.ai roles
const groupRoleMapping: Record<string, Fireflies.aiRole> = {
  'Engineering': Fireflies.aiRole.Developer,
  'Platform-Admins': Fireflies.aiRole.Admin,
  'Data-Team': Fireflies.aiRole.Viewer,
};
```

### OAuth2/OIDC Integration

```typescript
import { OAuth2Client } from '@fireflies/sdk';

const oauthClient = new OAuth2Client({
  clientId: process.env.FIREFLIES_OAUTH_CLIENT_ID!,
  clientSecret: process.env.FIREFLIES_OAUTH_CLIENT_SECRET!,
  redirectUri: 'https://app.yourcompany.com/auth/fireflies/callback',
  scopes: ['read', 'write'],
});
```