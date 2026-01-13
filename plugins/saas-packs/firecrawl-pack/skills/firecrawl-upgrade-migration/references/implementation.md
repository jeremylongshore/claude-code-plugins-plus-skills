# Implementation Guide

### Step 1: Check Current Version
```bash
npm list @firecrawl/sdk
npm view @firecrawl/sdk version
```

### Step 2: Review Changelog
```bash
open https://github.com/firecrawl/sdk/releases
```

### Step 3: Create Upgrade Branch
```bash
git checkout -b upgrade/firecrawl-sdk-vX.Y.Z
npm install @firecrawl/sdk@latest
npm test
```

### Step 4: Handle Breaking Changes
Update import statements, configuration, and method signatures as needed.