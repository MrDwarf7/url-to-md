# url2md

Any URL → clean markdown for LLMs.

Strips ads, navigation, cookie banners, and boilerplate. Returns the actual content — formatted as clean markdown with token count estimates.

Built for developers who paste web content into Claude, Cursor, Copilot, or any AI coding tool.

## Use It

**Web:** [url2md.com](https://url2md.com) — paste a URL, get markdown. No signup.

**API:**
```bash
# GET
curl "https://url2md.com/api/convert?url=https://example.com/article"

# POST
curl -X POST https://url2md.com/api/convert \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com/article"}'
```

**Response:**
```json
{
  "url": "https://example.com/article",
  "title": "Article Title",
  "markdown": "# Article Title\n\nContent here...",
  "char_count": 4521,
  "token_estimate": 1130,
  "line_count": 87,
  "truncated": false
}
```

Rate limit: 30 requests/hour per IP. No API key needed.

## Run Locally

```bash
pip install -r requirements.txt
python main.py
# Open http://localhost:8000
```

## What It Does

1. Fetches the URL with a clean user-agent
2. Runs readability extraction (same algorithm Firefox Reader View uses)
3. Converts HTML → markdown with html2text
4. Strips empty elements, collapses whitespace
5. Counts tokens (rough estimate: chars ÷ 4)

No tracking. No accounts. No "sign up to unlock." Just a tool.

## Why

Every developer using AI coding tools hits this problem daily. You find a doc page, a blog post, a Stack Overflow answer — you need it in your LLM's context window. Copy-pasting HTML gives you garbage. This gives you clean markdown.

## License

MIT
