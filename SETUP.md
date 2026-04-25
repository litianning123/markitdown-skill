# Quick Setup Guide

## Ready to Upload to GitHub!

Your MarkItDown skill repository is now ready. Here's how to publish it:

### Step 1: Initialize Git

```bash
cd /Users/tianningli/arena/markitdown-skill
git init
git add .
git commit -m "Initial commit: MarkItDown skill for Claude Code"
```

### Step 2: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `markitdown-skill`
3. Description: `Convert documents to Markdown using Microsoft's MarkItDown tool`
4. Make it **Public**
5. **Don't** initialize with README (we already have one)
6. Click "Create repository"

### Step 3: Push to GitHub

```bash
# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/markitdown-skill.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 4: Update README Links

Edit `README.md` and replace `yourusername` with your actual GitHub username in these lines:
- Line 1: `yourusername/markitdown-skill`
- Line 82: `yourusername/markitdown-skill`
- Line 114: `yourusername/markitdown-skill`

## Repository Structure

```
markitdown-skill/
├── .gitignore              # Git ignore patterns
├── LICENSE                 # MIT License
├── README.md               # Main documentation
├── CONTRIBUTING.md         # Contribution guidelines
├── SETUP.md                # This file
├── pyproject.toml          # Package configuration
├── skill.md                # Claude Code skill definition
├── convert.py              # Python conversion script (executable)
└── examples/               # Usage examples
    ├── advanced.md         # Advanced usage patterns
    ├── basic_usage.md      # Basic conversion examples
    └── batch_processing.md # Batch processing workflows
```

## What's Included

- ✅ Complete skill definition for Claude Code
- ✅ Python conversion script with CLI and API
- ✅ Comprehensive documentation
- ✅ Usage examples (basic, batch, advanced)
- ✅ MIT License
- ✅ Contribution guidelines
- ✅ Python package configuration
- ✅ Proper .gitignore for Python projects

## Next Steps After Publishing

1. **Add topics/tags** on GitHub: `claude-code`, `markdown`, `document-conversion`, `ocr`
2. **Create a release** for version 1.0.0
3. **Share with community** on Reddit, Discord, or Claude Code forums
4. **Consider adding**:
   - GitHub Actions for testing
   - Issues/PR templates
   - A badge showing download count or license

## Installing from GitHub

Once published, others can install your skill with:

```bash
# Clone directly to Claude skills directory
git clone https://github.com/YOUR_USERNAME/markitdown-skill.git ~/.claude/skills/markitdown

# Or download and extract
wget https://github.com/YOUR_USERNAME/markitdown-skill/archive/refs/heads/main.zip
unzip main.zip -d ~/.claude/skills/
mv ~/.claude/skills/markitdown-skill ~/.claude/skills/markitdown
```

---

Happy publishing! 🚀
