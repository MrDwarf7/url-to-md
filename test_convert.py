#!/usr/bin/env python3
"""Test url2md conversion."""
import json
import sys
sys.path.insert(0, ".")
from main import url_to_markdown

result = url_to_markdown("https://example.com")
print(json.dumps(result, indent=2))
print(f"\n--- Markdown preview (first 500 chars) ---")
print(result["markdown"][:500])
