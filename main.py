"""url2md — Clean URL to Markdown converter for LLMs.

Free web tool + API. Paste a URL, get clean markdown optimized for context windows.
Strips ads, nav, boilerplate. Returns token count estimates.
"""

import os
import time
import hashlib
from collections import defaultdict
from urllib.parse import urlparse

import requests
import readability
import html2text
from bs4 import BeautifulSoup
from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse

app = FastAPI(title="url2md", version="1.0.0")

# Rate limiting: 30 requests per IP per hour
RATE_LIMIT = 30
RATE_WINDOW = 3600
rate_limits = defaultdict(list)


def check_rate_limit(ip: str):
    now = time.time()
    rate_limits[ip] = [t for t in rate_limits[ip] if now - t < RATE_WINDOW]
    if len(rate_limits[ip]) >= RATE_LIMIT:
        raise HTTPException(429, "Rate limit exceeded. 30 requests/hour on free tier.")
    rate_limits[ip].append(now)


def estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 chars per token for English."""
    return max(1, len(text) // 4)


def url_to_markdown(url: str, max_chars: int = 500_000) -> dict:
    """Fetch URL, extract main content, convert to markdown."""
    # Validate URL
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise HTTPException(400, "Only http and https URLs are supported.")

    # Fetch
    try:
        resp = requests.get(
            url,
            timeout=15,
            headers={
                "User-Agent": "url2md/1.0 (URL to Markdown converter; +https://url2md.com)",
                "Accept": "text/html,application/xhtml+xml",
            },
        )
        resp.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(502, f"Failed to fetch URL: {e}")

    content_type = resp.headers.get("content-type", "")
    if "text/html" not in content_type:
        raise HTTPException(400, f"Expected HTML, got {content_type}")

    # Extract main content with readability
    html = resp.text
    try:
        doc = readability.Document(html)
        title = doc.title()
        summary_html = doc.summary()
    except Exception:
        # Fallback to full page if readability fails
        title = BeautifulSoup(html, "html.parser").title
        title = title.string if title else parsed.netloc
        summary_html = html

    # Convert to markdown
    h2t = html2text.HTML2Text()
    h2t.body_width = 0  # No line wrapping
    h2t.ignore_images = False
    h2t.ignore_links = False
    h2t.protect_links = True
    h2t.wrap_links = False
    markdown = h2t.handle(summary_html)

    # Clean up
    lines = markdown.split("\n")
    cleaned = []
    for line in lines:
        stripped = line.strip()
        # Remove empty link lines and excessive blank lines
        if stripped and stripped not in ("[]", "[ ]()", "![]()"):
            cleaned.append(line)

    markdown = "\n".join(cleaned)

    # Collapse triple+ newlines
    while "\n\n\n" in markdown:
        markdown = markdown.replace("\n\n\n", "\n\n")

    # Truncate if needed
    truncated = False
    if len(markdown) > max_chars:
        markdown = markdown[:max_chars] + "\n\n[... truncated at {} chars]".format(max_chars)
        truncated = True

    return {
        "url": url,
        "title": title,
        "markdown": markdown,
        "char_count": len(markdown),
        "token_estimate": estimate_tokens(markdown),
        "line_count": markdown.count("\n") + 1,
        "truncated": truncated,
    }


@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/index.html") as f:
        return f.read()


@app.post("/api/convert")
async def convert(request: Request):
    """Convert a URL to clean markdown."""
    ip = request.client.host if request.client else "unknown"
    check_rate_limit(ip)

    data = await request.json()
    url = data.get("url", "").strip()
    if not url:
        raise HTTPException(400, "Missing 'url' field.")
    max_chars = min(int(data.get("max_chars", 100_000)), 500_000)

    return url_to_markdown(url, max_chars)


@app.get("/api/convert")
async def convert_get(request: Request, url: str = "", max_chars: int = 100_000):
    """GET endpoint for easy curl usage."""
    ip = request.client.host if request.client else "unknown"
    check_rate_limit(ip)

    if not url:
        raise HTTPException(400, "Missing 'url' query parameter.")
    max_chars = min(max_chars, 500_000)

    return url_to_markdown(url, max_chars)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
