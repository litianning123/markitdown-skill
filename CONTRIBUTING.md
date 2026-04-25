# Contributing to MarkItDown Skill

Thank you for your interest in contributing to the MarkItDown skill for Claude Code! This document provides guidelines and instructions for contributing.

## How to Contribute

### Reporting Bugs

1. Check existing [issues](https://github.com/yourusername/markitdown-skill/issues) to avoid duplicates
2. Use the issue template and provide:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version, MarkItDown version)
   - Error messages or logs

### Suggesting Features

1. Check existing feature requests
2. Describe the use case clearly
3. Explain why the feature would be useful
4. Consider if it fits the skill's scope

### Submitting Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes with clear, descriptive commit messages
4. Add tests if applicable
5. Ensure code follows existing style
6. Update documentation as needed
7. Submit a pull request with a clear description

## Development Setup

### Prerequisites

```bash
# Clone your fork
git clone https://github.com/yourusername/markitdown-skill.git
cd markitdown-skill

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install MarkItDown
pip install "markitdown[all]"

# Install development tools (optional)
pip install black ruff pytest
```

### Testing Changes

```bash
# Test the conversion script
python convert.py test_document.pdf -o test_output.md

# Test with Claude Code (symlink for development)
ln -s $(pwd) ~/.claude/skills/markitdown-dev
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular
- Write clear, concise comments

### Example

```python
def convert_file(input_path: str, output_path: Optional[str] = None) -> str:
    """
    Convert a file to Markdown using MarkItDown.

    Args:
        input_path: Path to input file or URL
        output_path: Optional path to output file

    Returns:
        The Markdown content as string

    Raises:
        RuntimeError: If conversion fails
    """
    # Implementation here
    pass
```

## Documentation

- Update README.md for user-facing changes
- Add examples to the `examples/` directory
- Update skill.md if functionality changes
- Keep inline comments clear and helpful

## Project Structure

```
markitdown-skill/
├── skill.md              # Claude Code skill definition
├── convert.py            # Python conversion script
├── README.md             # Project documentation
├── LICENSE               # MIT License
├── CONTRIBUTING.md       # This file
├── pyproject.toml        # Package configuration
├── .gitignore           # Git ignore patterns
└── examples/            # Usage examples
    ├── basic_usage.md
    ├── batch_processing.md
    └── advanced.md
```

## Areas for Contribution

We welcome contributions in:

- **Documentation**: Improving examples, adding tutorials
- **Features**: New conversion options, filters, output formats
- **Bug fixes**: Addressing reported issues
- **Tests**: Adding test coverage
- **Performance**: Optimizing conversion speed
- **Integration**: Better Claude Code integration

## Getting Help

- Open an issue for bugs or feature requests
- Check existing documentation and examples
- Review related projects:
  - [MarkItDown](https://github.com/microsoft/markitdown)
  - [Claude Code](https://claude.com/claude-code)

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Code of Conduct

Be respectful, constructive, and inclusive. We're all here to build something useful together.

---

Thank you for contributing! 🎉
