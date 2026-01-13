# Implementation Guide

### Step 1: Check Current Version
```bash
npm list @fireflies/sdk
npm view @fireflies/sdk version
```

### Step 2: Review Changelog
```bash
open https://github.com/fireflies/sdk/releases
```

### Step 3: Create Upgrade Branch
```bash
git checkout -b upgrade/fireflies-sdk-vX.Y.Z
npm install @fireflies/sdk@latest
npm test
```

### Step 4: Handle Breaking Changes
Update import statements, configuration, and method signatures as needed.