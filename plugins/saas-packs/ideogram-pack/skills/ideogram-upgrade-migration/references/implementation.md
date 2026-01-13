# Implementation Guide

### Step 1: Check Current Version
```bash
npm list @ideogram/sdk
npm view @ideogram/sdk version
```

### Step 2: Review Changelog
```bash
open https://github.com/ideogram/sdk/releases
```

### Step 3: Create Upgrade Branch
```bash
git checkout -b upgrade/ideogram-sdk-vX.Y.Z
npm install @ideogram/sdk@latest
npm test
```

### Step 4: Handle Breaking Changes
Update import statements, configuration, and method signatures as needed.