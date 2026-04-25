# Advanced Usage Examples

## Custom Processing Workflows

### Convert and Post-Process

```python
from convert import convert_file
import re

def clean_markdown(content: str) -> str:
    """Clean and normalize markdown content."""
    # Remove excessive blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    # Fix common formatting issues
    content = content.replace('** **', '')
    return content.strip()

# Convert and clean
raw_markdown = convert_file("document.pdf")
cleaned_markdown = clean_markdown(raw_markdown)

with open("cleaned_output.md", "w") as f:
    f.write(cleaned_markdown)
```

### Extract Specific Sections

```python
from convert import convert_file
import re

def extract_section(content: str, section_title: str) -> str:
    """Extract a specific section from markdown."""
    pattern = rf'## {section_title}(.*?)(?=## |\Z)'
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else ""

# Get only the introduction section
full_doc = convert_file("report.pdf")
intro = extract_section(full_doc, "Introduction")
print(intro)
```

## Integration with Other Tools

### Combine with Pandoc

```bash
# Convert PDF to Markdown, then to HTML
~/.venv/markitdown/bin/markitdown document.pdf | pandoc -f markdown -o output.html

# Convert to DOCX via Markdown
~/.venv/markitdown/bin/markitdown presentation.pptx | pandoc -f markdown -o document.docx
```

### Use with Obsidian

```python
from convert import batch_convert
from pathlib import Path
import shutil

# Convert documents to Obsidian vault
def convert_to_vault(source_files, vault_path):
    for file in source_files:
        markdown = convert_file(file)
        output_name = Path(file).stem + ".md"
        output_path = Path(vault_path) / output_name

        # Add Obsidian metadata
        with open(output_path, 'w') as f:
            f.write(f"---\nsource: {file}\nconverted: {date}\n---\n\n")
            f.write(markdown)

# Usage
convert_to_vault(["*.pdf"], "~/Documents/ObsidianVault")
```

### Feed to LLMs

```python
from convert import convert_file
import anthropic

def summarize_document(file_path: str) -> str:
    """Summarize a document using Claude."""
    # Convert to markdown
    markdown = convert_file(file_path)

    # Create prompt with first 4000 tokens (approx)
    prompt = f"""Please summarize the following document:

{markdown[:15000]}

Provide a concise summary in 3-5 bullet points."""

    # Call Claude API (requires anthropic package)
    client = anthropic.Anthropic()
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text

# Usage
summary = summarize_document("report.pdf")
print(summary)
```

## Error Handling and Recovery

### Retry Logic

```python
from convert import convert_file
import time

def convert_with_retry(input_path: str, max_retries: int = 3) -> str:
    """Convert with retry logic for unreliable sources."""
    for attempt in range(max_retries):
        try:
            return convert_file(input_path)
        except RuntimeError as e:
            if attempt == max_retries - 1:
                raise
            print(f"Attempt {attempt + 1} failed, retrying...")
            time.sleep(2 ** attempt)  # Exponential backoff

# Usage
content = convert_with_retry("https://flaky-site.com/document")
```

### Validation

```python
from convert import convert_file
import re

def validate_markdown(content: str) -> dict:
    """Validate markdown content quality."""
    issues = []

    # Check for empty content
    if not content.strip():
        issues.append("Empty content")

    # Check for encoding issues
    if '' in content or '?' in content:
        issues.append("Possible encoding issues")

    # Check for broken markdown links
    broken_links = re.findall(r'\[([^\]]+)\]\(\)', content)
    if broken_links:
        issues.append(f"Empty links: {broken_links[:5]}")

    # Estimate quality (basic heuristics)
    word_count = len(content.split())
    has_structure = bool(re.search(r'^#+\s', content, re.MULTILINE))

    return {
        "valid": len(issues) == 0,
        "issues": issues,
        "word_count": word_count,
        "has_structure": has_structure
    }

# Usage
markdown = convert_file("document.pdf")
validation = validate_markdown(markdown)
if not validation["valid"]:
    print(f"Warnings: {validation['issues']}")
```

## Performance Optimization

### Parallel Processing

```python
from convert import convert_file
from concurrent.futures import ThreadPoolExecutor
import os

def batch_convert_parallel(files, output_dir, max_workers=4):
    """Convert multiple files in parallel."""
    os.makedirs(output_dir, exist_ok=True)

    def convert_one(file_path):
        try:
            out_name = os.path.splitext(os.path.basename(file_path))[0] + ".md"
            out_path = os.path.join(output_dir, out_name)
            content = convert_file(file_path, out_path)
            return (file_path, True, out_path)
        except Exception as e:
            return (file_path, False, str(e))

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(convert_one, files))

    return results

# Usage
import glob
pdf_files = glob.glob("*.pdf")
results = batch_convert_parallel(pdf_files, "./converted")

for source, success, result in results:
    if success:
        print(f"✓ {source} → {result}")
    else:
        print(f"✗ {source}: {result}")
```

### Memory-Efficient Processing

```python
from convert import convert_file
import os

def convert_streaming(input_path, output_path, chunk_size=10000):
    """Process large files in chunks to reduce memory usage."""
    # For very large files, consider streaming approach
    # This is a placeholder for future enhancement
    content = convert_file(input_path)

    with open(output_path, 'w') as f:
        # Write in chunks if needed
        f.write(content)

    return output_path
```

## Troubleshooting

### Common Issues

**MarkItDown not found:**
```bash
# Ensure MarkItDown is installed
~/.venv/markitdown/bin/pip install "markitdown[all]"
```

**Permission denied:**
```bash
# Make script executable
chmod +x convert.py
```

**Encoding issues:**
```python
# Specify encoding when reading/writing
with open("output.md", 'w', encoding='utf-8') as f:
    f.write(markdown_content)
```

### Debug Mode

```python
import logging
from convert import convert_file

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

try:
    content = convert_file("problematic.pdf")
except Exception as e:
    logging.error(f"Conversion failed: {e}", exc_info=True)
```

## Tips and Best Practices

1. **Always validate** converted content before using in production
2. **Handle errors** gracefully in automated workflows
3. **Use batch processing** for multiple files
4. **Monitor quality** of OCR and transcription results
5. **Cache results** to avoid re-converting unchanged files
6. **Clean up** temporary files after processing
7. **Document custom** processing steps for reproducibility
