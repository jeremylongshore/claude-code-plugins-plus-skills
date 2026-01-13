# Implementation Guide

### Step 1: Check Current Version
```bash
npm list @groq/sdk
npm view @groq/sdk version
```

### Step 2: Review Changelog
```bash
open https://github.com/groq/sdk/releases
```

### Step 3: Create Upgrade Branch
```bash
git checkout -b upgrade/groq-sdk-vX.Y.Z
npm install @groq/sdk@latest
npm test
```

### Step 4: Handle Breaking Changes
Update import statements, configuration, and method signatures as needed.