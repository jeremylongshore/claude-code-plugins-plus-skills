# Eslint Rules

## ESLint Rules

### Custom Retell AI Plugin
```javascript
// eslint-plugin-retellai/rules/no-hardcoded-keys.js
module.exports = {
  meta: {
    type: 'problem',
    docs: {
      description: 'Disallow hardcoded Retell AI API keys',
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
              message: 'Hardcoded Retell AI API key detected',
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
  plugins: ['retellai'],
  rules: {
    'retellai/no-hardcoded-keys': 'error',
    'retellai/require-error-handling': 'warn',
    'retellai/use-typed-client': 'warn',
  },
};
```