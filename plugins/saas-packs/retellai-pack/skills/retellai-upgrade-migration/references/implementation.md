# Implementation Guide

### Step 1: Check Current Version
```bash
npm list @retellai/sdk
npm view @retellai/sdk version
```

### Step 2: Review Changelog
```bash
open https://github.com/retellai/sdk/releases
```

### Step 3: Create Upgrade Branch
```bash
git checkout -b upgrade/retellai-sdk-vX.Y.Z
npm install @retellai/sdk@latest
npm test
```

### Step 4: Handle Breaking Changes
Update import statements, configuration, and method signatures as needed.