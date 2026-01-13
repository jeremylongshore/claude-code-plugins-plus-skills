# Sso Integration

## SSO Integration

### SAML Configuration

```typescript
// Vast.ai SAML setup
const samlConfig = {
  entryPoint: 'https://idp.company.com/saml/sso',
  issuer: 'https://vastai.com/saml/metadata',
  cert: process.env.SAML_CERT,
  callbackUrl: 'https://app.yourcompany.com/auth/vastai/callback',
};

// Map IdP groups to Vast.ai roles
const groupRoleMapping: Record<string, Vast.aiRole> = {
  'Engineering': Vast.aiRole.Developer,
  'Platform-Admins': Vast.aiRole.Admin,
  'Data-Team': Vast.aiRole.Viewer,
};
```

### OAuth2/OIDC Integration

```typescript
import { OAuth2Client } from '@vastai/sdk';

const oauthClient = new OAuth2Client({
  clientId: process.env.VASTAI_OAUTH_CLIENT_ID!,
  clientSecret: process.env.VASTAI_OAUTH_CLIENT_SECRET!,
  redirectUri: 'https://app.yourcompany.com/auth/vastai/callback',
  scopes: ['read', 'write'],
});
```