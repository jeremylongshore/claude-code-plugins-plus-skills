# Eslint Rules

## ESLint Rules

### Custom Exa Plugin
```javascript
// eslint-plugin-exa/rules/no-hardcoded-keys.js
module.exports = {
  meta: {
    type: 'problem',
    docs: {
      description: 'Disallow hardcoded Exa API keys',
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
              message: 'Hardcoded Exa API key detected',
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
  plugins: ['exa'],
  rules: {
    'exa/no-hardcoded-keys': 'error',
    'exa/require-error-handling': 'warn',
    'exa/use-typed-client': 'warn',
  },
};
```