---
name: klingai-video-extension
license: MIT
allowed-tools: Read, Write, Edit, Grep
description: Execute extend video duration using kling ai continuation features. use
  when creating longer videos from shorter clips or building seamless sequences. trigger
  with phrases like 'klingai extend video', 'kling ai video continuation', 'klingai
  longer...
---
# Klingai Video Extension

## Overview

This skill demonstrates extending video duration using Kling AI's continuation features, including seamless extensions, multi-segment generation, and narrative continuation.

## Prerequisites

- Kling AI API key configured
- Existing video or generation job
- Python 3.8+

## Instructions

Follow these steps for video extension:

1. **Get Base Video**: Have initial video ready
2. **Configure Extension**: Set continuation parameters
3. **Generate Extension**: Submit continuation request
4. **Merge Segments**: Combine video parts
5. **Review Continuity**: Check seamless transitions

## Output

Successful execution produces:
- Extended video sequences
- Seamless segment transitions
- Multi-segment concatenation
- Loop-ready videos

## Error Handling

See `{baseDir}/references/errors.md` for comprehensive error handling.

## Examples

See `{baseDir}/references/examples.md` for detailed examples.

## Resources

- [Kling AI Video Extension](https://docs.klingai.com/extend)
- [FFmpeg Documentation](https://ffmpeg.org/documentation.html)
- [Video Concatenation](https://trac.ffmpeg.org/wiki/Concatenate)
