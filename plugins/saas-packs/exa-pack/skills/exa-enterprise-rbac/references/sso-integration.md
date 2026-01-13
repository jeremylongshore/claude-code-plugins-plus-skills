# Sso Integration

## SSO Integration

### SAML Configuration

```typescript
// Exa SAML setup
const samlConfig = {
  entryPoint: 'https://idp.company.com/saml/sso',
  issuer: 'https://exa.com/saml/metadata',
  cert: process.env.SAML_CERT,
  callbackUrl: 'https://app.yourcompany.com/auth/exa/callback',
};

// Map IdP groups to Exa roles
const groupRoleMapping: Record<string, ExaRole> = {
  'Engineering': ExaRole.Developer,
  'Platform-Admins': ExaRole.Admin,
  'Data-Team': ExaRole.Viewer,
};
```

### OAuth2/OIDC Integration

```typescript
import { OAuth2Client } from '@exa/sdk';

const oauthClient = new OAuth2Client({
  clientId: process.env.EXA_OAUTH_CLIENT_ID!,
  clientSecret: process.env.EXA_OAUTH_CLIENT_SECRET!,
  redirectUri: 'https://app.yourcompany.com/auth/exa/callback',
  scopes: ['read', 'write'],
});
```