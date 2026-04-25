# Batch Processing Examples

## Converting Multiple Files

### All PDFs in a Directory

```bash
# Using Claude Code
/markitdown Convert all PDFs in ./documents to markdown

# Using Python script
python convert.py "./documents/*.pdf" --batch --output ./converted

# JSON output for automation
python convert.py "*.pdf" --batch --json > results.json
```

### All Office Documents

```bash
# Convert all Word documents
python convert.py "*.docx" --batch --output ./markdown

# Convert all PowerPoint files
python convert.py "*.pptx" --batch --output ./slides

# Convert all Excel files
python convert.py "*.xlsx" --batch --output ./sheets
```

### Mixed Document Types

```bash
# Convert PDF, DOCX, and PPTX files
python convert.py "*.{pdf,docx,pptx}" --batch --output ./all_markdown

# Using find for more complex patterns
find ./source -name "*.pdf" -exec python convert.py {} --output ./converted \;
```

## Batch Processing with Python

```python
from convert import batch_convert
import json

# Convert all PDFs
results = batch_convert("./documents/*.pdf", output_dir="./converted")

# Print summary
for file, result in results.items():
    if result["success"]:
        print(f"✓ {file} → {result['output']}")
    else:
        print(f"✗ {file}: {result['error']}")

# Save results to JSON
with open("conversion_results.json", "w") as f:
    json.dump(results, f, indent=2)
```

## Organizing Converted Files

### By Document Type

```bash
# Create separate directories for each type
python convert.py "*.pdf" --batch --output ./markdown/pdfs
python convert.py "*.docx" --batch --output ./markdown/docs
python convert.py "*.pptx" --batch --output ./markdown/slides
```

### With Date Stamps

```python
from convert import batch_convert
from datetime import datetime

date_str = datetime.now().strftime("%Y%m%d")
output_dir = f"./converted/{date_str}"

results = batch_convert("*.pdf", output_dir=output_dir)
```

### Preserving Directory Structure

```python
import os
from pathlib import Path
from convert import convert_file

def batch_convert_preserve(source_dir, output_dir):
    """Convert files while preserving directory structure."""
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith(('.pdf', '.docx', '.pptx')):
                source_path = os.path.join(root, file)
                rel_path = os.path.relpath(source_path, source_dir)
                output_path = os.path.join(output_dir, os.path.splitext(rel_path)[0] + ".md")

                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                try:
                    convert_file(source_path, output_path)
                    print(f"✓ {source_path} → {output_path}")
                except Exception as e:
                    print(f"✗ {source_path}: {e}")

# Usage
batch_convert_preserve("./source_documents", "./converted_markdown")
```

## Error Handling

```python
from convert import batch_convert

# Convert with detailed error reporting
results = batch_convert("*.pdf", output_dir="./converted")

success_count = sum(1 for r in results.values() if r["success"])
error_count = len(results) - success_count

print(f"\nConversion Summary:")
print(f"  Success: {success_count}")
print(f"  Errors: {error_count}")

if error_count > 0:
    print("\nFailed files:")
    for file, result in results.items():
        if not result["success"]:
            print(f"  - {file}: {result['error']}")
```

## Performance Tips

1. **Limit concurrency** when processing many files to avoid memory issues
2. **Use SSD storage** for faster I/O during batch operations
3. **Monitor progress** with JSON output for large batches
4. **Handle errors gracefully** to continue processing despite individual failures
5. **Clean up** temporary files after successful conversions
