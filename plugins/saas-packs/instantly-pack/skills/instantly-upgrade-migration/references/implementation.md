# Implementation Guide

### Step 1: Check Current Version
```bash
npm list @instantly/sdk
npm view @instantly/sdk version
```

### Step 2: Review Changelog
```bash
open https://github.com/instantly/sdk/releases
```

### Step 3: Create Upgrade Branch
```bash
git checkout -b upgrade/instantly-sdk-vX.Y.Z
npm install @instantly/sdk@latest
npm test
```

### Step 4: Handle Breaking Changes
Update import statements, configuration, and method signatures as needed.