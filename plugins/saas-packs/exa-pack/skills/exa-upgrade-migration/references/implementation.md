# Implementation Guide

### Step 1: Check Current Version
```bash
npm list @exa/sdk
npm view @exa/sdk version
```

### Step 2: Review Changelog
```bash
open https://github.com/exa/sdk/releases
```

### Step 3: Create Upgrade Branch
```bash
git checkout -b upgrade/exa-sdk-vX.Y.Z
npm install @exa/sdk@latest
npm test
```

### Step 4: Handle Breaking Changes
Update import statements, configuration, and method signatures as needed.