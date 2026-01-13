# Implementation Guide

### Step 1: Check Current Version
```bash
npm list @perplexity/sdk
npm view @perplexity/sdk version
```

### Step 2: Review Changelog
```bash
open https://github.com/perplexity/sdk/releases
```

### Step 3: Create Upgrade Branch
```bash
git checkout -b upgrade/perplexity-sdk-vX.Y.Z
npm install @perplexity/sdk@latest
npm test
```

### Step 4: Handle Breaking Changes
Update import statements, configuration, and method signatures as needed.