# Implementation Guide

### Step 1: Check Current Version
```bash
npm list @coderabbit/sdk
npm view @coderabbit/sdk version
```

### Step 2: Review Changelog
```bash
open https://github.com/coderabbit/sdk/releases
```

### Step 3: Create Upgrade Branch
```bash
git checkout -b upgrade/coderabbit-sdk-vX.Y.Z
npm install @coderabbit/sdk@latest
npm test
```

### Step 4: Handle Breaking Changes
Update import statements, configuration, and method signatures as needed.