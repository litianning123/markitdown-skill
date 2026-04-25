---
name: markitdown
description: Convert documents to Markdown using Microsoft's MarkItDown tool. Supports PDF, DOCX, PPTX, XLSX, images (OCR), audio transcription, HTML, YouTube URLs, EPUB, and more.
---

# MarkItDown

Convert various document formats to Markdown for AI processing and analysis.

## What This Skill Does

- Convert documents to Markdown format
- Extract text from images using OCR
- Transcribe audio files
- Fetch YouTube transcripts
- Batch convert multiple files
- Preserve document structure (headings, lists, tables, links)

## Supported Formats

- **Documents:** PDF, DOCX, PPTX, XLSX, XLS, CSV, JSON, XML
- **Web:** HTML, YouTube URLs
- **Media:** Images (PNG, JPG - with OCR), Audio (WAV, MP3 - transcription)
- **Other:** EPUB, ZIP files (iterates contents)

## Prerequisites

MarkItDown is installed in `~/.venv/markitdown/` with all format converters enabled.

## Usage

### Single File Conversion

```
Convert document.pdf to markdown
Convert this PowerPoint: presentation.pptx
Convert image.png to markdown (with OCR)
Convert audio.mp3 to markdown (transcribe)
```

### Batch Conversion

```
Convert all PDFs in this folder to markdown
Convert all documents in ./documents to markdown
```

### URL Conversion

```
Convert this YouTube URL to markdown: https://youtube.com/watch?v=xxx
Convert https://example.com to markdown
```

### With Output File

```
Convert report.pdf to markdown and save as report.md
Convert document.docx to output.md
```

## Output

- Markdown text is displayed in the conversation
- Can be saved to a file for later use
- Preserves document structure and formatting
- Images are described using AI vision or OCR

## Examples

```bash
# Basic conversion
~/.venv/markitdown/bin/markitdown document.pdf -o output.md

# Convert from stdin
cat document.docx | ~/.venv/markitdown/bin/markitdown

# Convert YouTube
~/.venv/markitdown/bin/markitdown "https://youtube.com/watch?v=xxx" > video.md
```

## Notes

- Images use OCR/extraction for text content
- Audio files are transcribed using speech recognition
- YouTube videos fetch available transcripts
- Output is optimized for LLM consumption
- For high-fidelity conversions, consider other tools
