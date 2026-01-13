# Sso Integration

## SSO Integration

### SAML Configuration

```typescript
// Perplexity SAML setup
const samlConfig = {
  entryPoint: 'https://idp.company.com/saml/sso',
  issuer: 'https://perplexity.com/saml/metadata',
  cert: process.env.SAML_CERT,
  callbackUrl: 'https://app.yourcompany.com/auth/perplexity/callback',
};

// Map IdP groups to Perplexity roles
const groupRoleMapping: Record<string, PerplexityRole> = {
  'Engineering': PerplexityRole.Developer,
  'Platform-Admins': PerplexityRole.Admin,
  'Data-Team': PerplexityRole.Viewer,
};
```

### OAuth2/OIDC Integration

```typescript
import { OAuth2Client } from '@perplexity/sdk';

const oauthClient = new OAuth2Client({
  clientId: process.env.PERPLEXITY_OAUTH_CLIENT_ID!,
  clientSecret: process.env.PERPLEXITY_OAUTH_CLIENT_SECRET!,
  redirectUri: 'https://app.yourcompany.com/auth/perplexity/callback',
  scopes: ['read', 'write'],
});
```