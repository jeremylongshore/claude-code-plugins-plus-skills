# Eslint Rules

## ESLint Rules

### Custom Windsurf Plugin
```javascript
// eslint-plugin-windsurf/rules/no-hardcoded-keys.js
module.exports = {
  meta: {
    type: 'problem',
    docs: {
      description: 'Disallow hardcoded Windsurf API keys',
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
              message: 'Hardcoded Windsurf API key detected',
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
  plugins: ['windsurf'],
  rules: {
    'windsurf/no-hardcoded-keys': 'error',
    'windsurf/require-error-handling': 'warn',
    'windsurf/use-typed-client': 'warn',
  },
};
```