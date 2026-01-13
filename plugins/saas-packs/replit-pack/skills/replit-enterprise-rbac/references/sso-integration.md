# Sso Integration

## SSO Integration

### SAML Configuration

```typescript
// Replit SAML setup
const samlConfig = {
  entryPoint: 'https://idp.company.com/saml/sso',
  issuer: 'https://replit.com/saml/metadata',
  cert: process.env.SAML_CERT,
  callbackUrl: 'https://app.yourcompany.com/auth/replit/callback',
};

// Map IdP groups to Replit roles
const groupRoleMapping: Record<string, ReplitRole> = {
  'Engineering': ReplitRole.Developer,
  'Platform-Admins': ReplitRole.Admin,
  'Data-Team': ReplitRole.Viewer,
};
```

### OAuth2/OIDC Integration

```typescript
import { OAuth2Client } from '@replit/sdk';

const oauthClient = new OAuth2Client({
  clientId: process.env.REPLIT_OAUTH_CLIENT_ID!,
  clientSecret: process.env.REPLIT_OAUTH_CLIENT_SECRET!,
  redirectUri: 'https://app.yourcompany.com/auth/replit/callback',
  scopes: ['read', 'write'],
});
```