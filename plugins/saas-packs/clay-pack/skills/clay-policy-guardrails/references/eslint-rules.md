# Eslint Rules

## ESLint Rules

### Custom Clay Plugin
```javascript
// eslint-plugin-clay/rules/no-hardcoded-keys.js
module.exports = {
  meta: {
    type: 'problem',
    docs: {
      description: 'Disallow hardcoded Clay API keys',
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
              message: 'Hardcoded Clay API key detected',
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
  plugins: ['clay'],
  rules: {
    'clay/no-hardcoded-keys': 'error',
    'clay/require-error-handling': 'warn',
    'clay/use-typed-client': 'warn',
  },
};
```