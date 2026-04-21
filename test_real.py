#!/usr/bin/env python3
"""Test url2md with a real article."""
import json
import sys
sys.path.insert(0, ".")
from main import url_to_markdown

# Test with a real article
result = url_to_markdown("https://blog.pragmaticengineer.com/software-engineering-salaries-in-the-netherlands-and-europe/")
print(f"Title: {result['title']}")
print(f"Chars: {result['char_count']:,}")
print(f"Tokens: {result['token_estimate']:,}")
print(f"Lines: {result['line_count']}")
print(f"\n--- First 800 chars ---")
print(result["markdown"][:800])
