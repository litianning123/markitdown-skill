# MarkItDown Skill for Claude Code

> Convert documents to Markdown using Microsoft's MarkItDown tool

A [Claude Code](https://claude.com/claude-code) skill that converts various document formats to Markdown for AI processing and analysis. Supports PDFs, Office documents, images (OCR), audio transcription, HTML, YouTube URLs, and more.

## Features

- 📄 **Document Conversion**: PDF, DOCX, PPTX, XLSX, XLS, CSV, JSON, XML
- 🌐 **Web Content**: HTML pages, YouTube video metadata
- 🖼️ **Image OCR**: Extract text from PNG, JPG images
- 🎵 **Audio Transcription**: Transcribe WAV, MP3 audio files
- 📦 **Batch Processing**: Convert multiple files at once
- 📚 **Other Formats**: EPUB, ZIP files (iterates contents)

## Prerequisites

This skill requires [MarkItDown](https://github.com/microsoft/markitdown) to be installed:

```bash
# Create virtual environment
python3 -m venv ~/.venv/markitdown

# Install MarkItDown with all format converters
~/.venv/markitdown/bin/pip install "markitdown[all]"
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/markitdown-skill.git
cd markitdown-skill
```

### Install as Claude Code Skill

```bash
# Copy to Claude skills directory
cp -r . ~/.claude/skills/markitdown
```

Or symlink for development:

```bash
ln -s $(pwd) ~/.claude/skills/markitdown
```

## Usage

Once installed, use the skill directly in Claude Code:

### Single File Conversion

```
/markitdown Convert document.pdf to markdown
/markitdown Convert presentation.pptx to markdown
/markitdown Convert image.png to markdown (with OCR)
/markitdown Convert audio.mp3 to markdown (transcribe)
```

### Batch Conversion

```
/markitdown Convert all PDFs in this folder to markdown
/markitdown Convert all documents in ./documents to markdown
```

### URL Conversion

```
/markitdown Convert https://youtube.com/watch?v=xxx to markdown
/markitdown Convert https://example.com to markdown
```

### Save to File

```
/markitdown Convert report.pdf to markdown and save as report.md
```

## Python API

The included `convert.py` script can also be used as a Python module:

```python
from convert import convert_file, batch_convert

# Single file
markdown = convert_file("document.pdf", output_path="output.md")

# Batch conversion
results = batch_convert("*.pdf", output_dir="./converted")
```

### Command Line

```bash
# Basic conversion
python convert.py document.pdf -o output.md

# Batch conversion
python convert.py "*.pdf" --batch --output ./converted

# JSON output
python convert.py "*.docx" --batch --json
```

## Examples

See the `examples/` directory for sample usage:

- `examples/basic_usage.md` - Simple conversion examples
- `examples/batch_processing.md` - Batch conversion workflows
- `examples/advanced.md` - Advanced use cases

## How It Works

The skill leverages Microsoft's [MarkItDown](https://github.com/microsoft/markitdown) tool, which:

- Parses document structure and preserves semantic elements
- Extracts text content while maintaining headings, lists, tables
- Uses OCR for images and speech recognition for audio
- Optimizes output for LLM consumption
- Fetches YouTube metadata and transcripts when available

## Limitations

- Images use OCR/extraction (not full visual understanding)
- Audio transcription quality depends on the speech recognition engine
- YouTube URLs fetch metadata (not full video transcripts unless available)
- For high-fidelity document conversions, consider specialized tools

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Microsoft MarkItDown](https://github.com/microsoft/markitdown) - The underlying conversion tool
- [Claude Code](https://claude.com/claude-code) - The AI development environment

## Support

For issues, questions, or suggestions, please [open an issue](https://github.com/yourusername/markitdown-skill/issues).

---

Made with ❤️ for the Claude Code community
