# Sso Integration

## SSO Integration

### SAML Configuration

```typescript
// CodeRabbit SAML setup
const samlConfig = {
  entryPoint: 'https://idp.company.com/saml/sso',
  issuer: 'https://coderabbit.com/saml/metadata',
  cert: process.env.SAML_CERT,
  callbackUrl: 'https://app.yourcompany.com/auth/coderabbit/callback',
};

// Map IdP groups to CodeRabbit roles
const groupRoleMapping: Record<string, CodeRabbitRole> = {
  'Engineering': CodeRabbitRole.Developer,
  'Platform-Admins': CodeRabbitRole.Admin,
  'Data-Team': CodeRabbitRole.Viewer,
};
```

### OAuth2/OIDC Integration

```typescript
import { OAuth2Client } from '@coderabbit/sdk';

const oauthClient = new OAuth2Client({
  clientId: process.env.CODERABBIT_OAUTH_CLIENT_ID!,
  clientSecret: process.env.CODERABBIT_OAUTH_CLIENT_SECRET!,
  redirectUri: 'https://app.yourcompany.com/auth/coderabbit/callback',
  scopes: ['read', 'write'],
});
```