# Eslint Rules

## ESLint Rules

### Custom Perplexity Plugin
```javascript
// eslint-plugin-perplexity/rules/no-hardcoded-keys.js
module.exports = {
  meta: {
    type: 'problem',
    docs: {
      description: 'Disallow hardcoded Perplexity API keys',
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
              message: 'Hardcoded Perplexity API key detected',
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
  plugins: ['perplexity'],
  rules: {
    'perplexity/no-hardcoded-keys': 'error',
    'perplexity/require-error-handling': 'warn',
    'perplexity/use-typed-client': 'warn',
  },
};
```