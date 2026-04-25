#!/usr/bin/env python3
"""
MarkItDown conversion script for Claude Code skill.
Handles document conversion to Markdown format.
"""

import sys
import subprocess
import pathlib
import argparse
from typing import Optional

MARKITDOWN_BIN = pathlib.Path.home() / ".venv" / "markitdown" / "bin" / "markitdown"


def convert_file(input_path: str, output_path: Optional[str] = None) -> str:
    """
    Convert a file to Markdown using MarkItDown.

    Args:
        input_path: Path to input file or URL
        output_path: Optional path to output file

    Returns:
        The Markdown content as string
    """
    cmd = [str(MARKITDOWN_BIN), input_path]

    if output_path:
        cmd.extend(["-o", output_path])
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"MarkItDown error: {result.stderr}")
        # Read the output file
        with open(output_path, 'r') as f:
            return f.read()
    else:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"MarkItDown error: {result.stderr}")
        return result.stdout


def batch_convert(pattern: str, output_dir: Optional[str] = None) -> dict:
    """
    Convert multiple files matching a pattern.

    Args:
        pattern: Glob pattern for files
        output_dir: Optional output directory

    Returns:
        Dictionary with results for each file
    """
    import glob

    files = glob.glob(pattern)
    if not files:
        raise ValueError(f"No files found matching pattern: {pattern}")

    results = {}
    for file_path in files:
        try:
            input_path = pathlib.Path(file_path)
            if output_dir:
                out_path = pathlib.Path(output_dir) / f"{input_path.stem}.md"
                out_path.parent.mkdir(parents=True, exist_ok=True)
            else:
                out_path = input_path.with_suffix('.md')

            content = convert_file(str(input_path), str(out_path))
            results[file_path] = {
                "success": True,
                "output": str(out_path),
                "preview": content[:500] + "..." if len(content) > 500 else content
            }
        except Exception as e:
            results[file_path] = {
                "success": False,
                "error": str(e)
            }

    return results


def main():
    parser = argparse.ArgumentParser(description="Convert documents to Markdown")
    parser.add_argument("input", help="Input file, URL, or glob pattern")
    parser.add_argument("-o", "--output", help="Output file or directory")
    parser.add_argument("--batch", action="store_true", help="Batch convert multiple files")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    try:
        if args.batch or '*' in args.input:
            results = batch_convert(args.input, args.output)
            if args.json:
                import json
                print(json.dumps(results, indent=2))
            else:
                for file, result in results.items():
                    if result["success"]:
                        print(f"✓ {file} → {result['output']}")
                    else:
                        print(f"✗ {file}: {result['error']}")
        else:
            content = convert_file(args.input, args.output)
            if not args.output:
                print(content)
            else:
                print(f"Converted {args.input} → {args.output}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
