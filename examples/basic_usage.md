# Basic Usage Examples

## Converting Documents

### PDF to Markdown

```bash
# In Claude Code
/markitdown Convert report.pdf to markdown

# With output file
/markitdown Convert report.pdf to markdown and save as report.md

# Direct command
~/.venv/markitdown/bin/markitdown report.pdf -o report.md
```

### Word Documents

```bash
# Convert DOCX
/markitdown Convert document.docx to markdown

# Using Python API
python convert.py document.docx -o document.md
```

### PowerPoint Presentations

```bash
# Convert PPTX
/markitdown Convert presentation.pptx to markdown

# Save to file
/markitdown Convert slides.pptx to markdown and save as slides.md
```

## Converting Media

### Images with OCR

```bash
# Extract text from image
/markitdown Convert screenshot.png to markdown

# Convert and save
/markitdown Convert scanned.jpg to markdown and save as scanned.md
```

### Audio Transcription

```bash
# Transcribe audio file
/markitdown Convert recording.mp3 to markdown

# Transcribe and save
/markitdown Convert interview.wav to markdown and save as transcript.md
```

## Converting Web Content

### YouTube Videos

```bash
# Get video metadata and description
/markitdown Convert https://youtube.com/watch?v=dQw4w9WgXcQ to markdown

# Save to file
/markitdown Convert https://youtube.com/watch?v=xxx to markdown and save as video.md
```

### Web Pages

```bash
# Convert HTML page
/markitdown Convert https://example.com to markdown

# Save page content
/markitdown Convert https://blog.example.com/article to markdown and save as article.md
```

## Using the Python API

```python
from convert import convert_file

# Convert a PDF
markdown_content = convert_file("document.pdf")

# Convert and save to file
markdown_content = convert_file("presentation.pptx", output_path="slides.md")

# Print first 500 characters
print(markdown_content[:500])
```

## Tips

1. **Always specify output files** for batch processing to avoid clutter
2. **Use quotes around URLs** to avoid shell parsing issues
3. **Check the converted output** for complex documents as formatting may vary
4. **Batch process** similar files using glob patterns: `"*.pdf"`
5. **OCR quality** depends on image resolution - use high-quality scans when possible
