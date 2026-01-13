# Implementation Guide

### Step 1: Retrieve and Edit Presentation
```typescript
import { GammaClient } from '@gamma/sdk';

const gamma = new GammaClient({ apiKey: process.env.GAMMA_API_KEY });

async function editPresentation(presentationId: string) {
  // Retrieve existing presentation
  const presentation = await gamma.presentations.get(presentationId);

  // Update title and style
  const updated = await gamma.presentations.update(presentationId, {
    title: 'Updated: ' + presentation.title,
    style: 'modern',
  });

  return updated;
}
```

### Step 2: Slide-Level Editing
```typescript
async function editSlide(presentationId: string, slideIndex: number, content: object) {
  const presentation = await gamma.presentations.get(presentationId);

  // Update specific slide
  const updatedSlide = await gamma.slides.update(
    presentationId,
    slideIndex,
    {
      title: content.title,
      content: content.body,
      layout: content.layout || 'content',
    }
  );

  return updatedSlide;
}

async function addSlide(presentationId: string, position: number, content: object) {
  return gamma.slides.insert(presentationId, position, {
    title: content.title,
    content: content.body,
    generateImage: content.imagePrompt,
  });
}

async function deleteSlide(presentationId: string, slideIndex: number) {
  return gamma.slides.delete(presentationId, slideIndex);
}
```

### Step 3: Export to Various Formats
```typescript
type ExportFormat = 'pdf' | 'pptx' | 'png' | 'html';

async function exportPresentation(
  presentationId: string,
  format: ExportFormat,
  options: object = {}
) {
  const exportJob = await gamma.exports.create(presentationId, {
    format,
    quality: options.quality || 'high',
    includeNotes: options.includeNotes ?? true,
    ...options,
  });

  // Wait for export to complete
  const result = await gamma.exports.wait(exportJob.id, {
    timeout: 60000,
    pollInterval: 2000,
  });

  return result.downloadUrl;
}

// Usage examples
const pdfUrl = await exportPresentation('pres-123', 'pdf');
const pptxUrl = await exportPresentation('pres-123', 'pptx', { includeNotes: false });
const pngUrl = await exportPresentation('pres-123', 'png', { slideIndex: 0 }); // First slide only
```

### Step 4: Asset Management
```typescript
async function uploadAsset(presentationId: string, filePath: string) {
  const fileBuffer = await fs.readFile(filePath);

  const asset = await gamma.assets.upload(presentationId, {
    file: fileBuffer,
    filename: path.basename(filePath),
    type: 'image',
  });

  return asset.url;
}

async function listAssets(presentationId: string) {
  return gamma.assets.list(presentationId);
}
```