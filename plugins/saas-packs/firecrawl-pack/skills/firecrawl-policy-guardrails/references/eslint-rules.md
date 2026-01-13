# Eslint Rules

## ESLint Rules

### Custom FireCrawl Plugin
```javascript
// eslint-plugin-firecrawl/rules/no-hardcoded-keys.js
module.exports = {
  meta: {
    type: 'problem',
    docs: {
      description: 'Disallow hardcoded FireCrawl API keys',
    },
    fixable: 'code',
  },
  create(context) {
    return {
      Literal(node) {
        if (typeof node.value === 'string') {
          if (node.value.match(/^sk_(live|test)_[a-zA-Z0-9]{24,}/)) {
            context.report({
              node,
              message: 'Hardcoded FireCrawl API key detected',
            });
          }
        }
      },
    };
  },
};
```

### ESLint Configuration
```javascript
// .eslintrc.js
module.exports = {
  plugins: ['firecrawl'],
  rules: {
    'firecrawl/no-hardcoded-keys': 'error',
    'firecrawl/require-error-handling': 'warn',
    'firecrawl/use-typed-client': 'warn',
  },
};
```