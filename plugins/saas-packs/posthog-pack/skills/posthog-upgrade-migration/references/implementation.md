# Implementation Guide

### Step 1: Check Current Version
```bash
npm list @posthog/sdk
npm view @posthog/sdk version
```

### Step 2: Review Changelog
```bash
open https://github.com/posthog/sdk/releases
```

### Step 3: Create Upgrade Branch
```bash
git checkout -b upgrade/posthog-sdk-vX.Y.Z
npm install @posthog/sdk@latest
npm test
```

### Step 4: Handle Breaking Changes
Update import statements, configuration, and method signatures as needed.