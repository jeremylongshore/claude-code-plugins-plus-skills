# Sso Integration

## SSO Integration

### SAML Configuration

```typescript
// Instantly SAML setup
const samlConfig = {
  entryPoint: 'https://idp.company.com/saml/sso',
  issuer: 'https://instantly.com/saml/metadata',
  cert: process.env.SAML_CERT,
  callbackUrl: 'https://app.yourcompany.com/auth/instantly/callback',
};

// Map IdP groups to Instantly roles
const groupRoleMapping: Record<string, InstantlyRole> = {
  'Engineering': InstantlyRole.Developer,
  'Platform-Admins': InstantlyRole.Admin,
  'Data-Team': InstantlyRole.Viewer,
};
```

### OAuth2/OIDC Integration

```typescript
import { OAuth2Client } from '@instantly/sdk';

const oauthClient = new OAuth2Client({
  clientId: process.env.INSTANTLY_OAUTH_CLIENT_ID!,
  clientSecret: process.env.INSTANTLY_OAUTH_CLIENT_SECRET!,
  redirectUri: 'https://app.yourcompany.com/auth/instantly/callback',
  scopes: ['read', 'write'],
});
```