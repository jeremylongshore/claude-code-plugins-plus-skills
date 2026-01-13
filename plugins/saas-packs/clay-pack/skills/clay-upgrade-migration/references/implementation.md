# Implementation Guide

### Step 1: Check Current Version
```bash
npm list @clay/sdk
npm view @clay/sdk version
```

### Step 2: Review Changelog
```bash
open https://github.com/clay/sdk/releases
```

### Step 3: Create Upgrade Branch
```bash
git checkout -b upgrade/clay-sdk-vX.Y.Z
npm install @clay/sdk@latest
npm test
```

### Step 4: Handle Breaking Changes
Update import statements, configuration, and method signatures as needed.