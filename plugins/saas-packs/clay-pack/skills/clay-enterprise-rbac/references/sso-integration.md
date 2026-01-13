# Sso Integration

## SSO Integration

### SAML Configuration

```typescript
// Clay SAML setup
const samlConfig = {
  entryPoint: 'https://idp.company.com/saml/sso',
  issuer: 'https://clay.com/saml/metadata',
  cert: process.env.SAML_CERT,
  callbackUrl: 'https://app.yourcompany.com/auth/clay/callback',
};

// Map IdP groups to Clay roles
const groupRoleMapping: Record<string, ClayRole> = {
  'Engineering': ClayRole.Developer,
  'Platform-Admins': ClayRole.Admin,
  'Data-Team': ClayRole.Viewer,
};
```

### OAuth2/OIDC Integration

```typescript
import { OAuth2Client } from '@clay/sdk';

const oauthClient = new OAuth2Client({
  clientId: process.env.CLAY_OAUTH_CLIENT_ID!,
  clientSecret: process.env.CLAY_OAUTH_CLIENT_SECRET!,
  redirectUri: 'https://app.yourcompany.com/auth/clay/callback',
  scopes: ['read', 'write'],
});
```