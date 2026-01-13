# Implementation Guide

### Step 1: Check Current Version
```bash
npm list @vastai/sdk
npm view @vastai/sdk version
```

### Step 2: Review Changelog
```bash
open https://github.com/vastai/sdk/releases
```

### Step 3: Create Upgrade Branch
```bash
git checkout -b upgrade/vastai-sdk-vX.Y.Z
npm install @vastai/sdk@latest
npm test
```

### Step 4: Handle Breaking Changes
Update import statements, configuration, and method signatures as needed.