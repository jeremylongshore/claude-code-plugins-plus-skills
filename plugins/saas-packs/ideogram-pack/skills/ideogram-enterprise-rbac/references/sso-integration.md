# Sso Integration

## SSO Integration

### SAML Configuration

```typescript
// Ideogram SAML setup
const samlConfig = {
  entryPoint: 'https://idp.company.com/saml/sso',
  issuer: 'https://ideogram.com/saml/metadata',
  cert: process.env.SAML_CERT,
  callbackUrl: 'https://app.yourcompany.com/auth/ideogram/callback',
};

// Map IdP groups to Ideogram roles
const groupRoleMapping: Record<string, IdeogramRole> = {
  'Engineering': IdeogramRole.Developer,
  'Platform-Admins': IdeogramRole.Admin,
  'Data-Team': IdeogramRole.Viewer,
};
```

### OAuth2/OIDC Integration

```typescript
import { OAuth2Client } from '@ideogram/sdk';

const oauthClient = new OAuth2Client({
  clientId: process.env.IDEOGRAM_OAUTH_CLIENT_ID!,
  clientSecret: process.env.IDEOGRAM_OAUTH_CLIENT_SECRET!,
  redirectUri: 'https://app.yourcompany.com/auth/ideogram/callback',
  scopes: ['read', 'write'],
});
```