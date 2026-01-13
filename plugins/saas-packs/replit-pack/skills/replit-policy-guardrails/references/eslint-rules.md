# Eslint Rules

## ESLint Rules

### Custom Replit Plugin
```javascript
// eslint-plugin-replit/rules/no-hardcoded-keys.js
module.exports = {
  meta: {
    type: 'problem',
    docs: {
      description: 'Disallow hardcoded Replit API keys',
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
              message: 'Hardcoded Replit API key detected',
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
  plugins: ['replit'],
  rules: {
    'replit/no-hardcoded-keys': 'error',
    'replit/require-error-handling': 'warn',
    'replit/use-typed-client': 'warn',
  },
};
```