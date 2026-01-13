# Implementation Guide

### Step 1: Check Current Version
```bash
npm list @windsurf/sdk
npm view @windsurf/sdk version
```

### Step 2: Review Changelog
```bash
open https://github.com/windsurf/sdk/releases
```

### Step 3: Create Upgrade Branch
```bash
git checkout -b upgrade/windsurf-sdk-vX.Y.Z
npm install @windsurf/sdk@latest
npm test
```

### Step 4: Handle Breaking Changes
Update import statements, configuration, and method signatures as needed.