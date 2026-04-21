# url2md Launch Content

## Reddit Post — r/LocalLLaMA

**Title:** I got tired of copy-pasting messy HTML into LLMs, so I built a URL→Markdown converter

**Body:**

Every day I'm pasting doc pages and blog posts into Claude or Cursor, and every day I'm cleaning up garbage — nav bars, cookie consent banners, "related articles" sidebars, tracking scripts that somehow escaped the copy.

So I built [url2md](https://github.com/MrDwarf7/url-to-md). Paste a URL, get clean markdown. That's it.

What it actually does:
- Uses the same readability algorithm as Firefox Reader View (mozilla/readability)
- Converts to markdown with proper headings, links, code blocks
- Shows you the token count before you paste into your context window
- Free API — 30 requests/hour, no signup, just curl it

```bash
curl "https://url2md.com/api/convert?url=https://your-article-url.com"
```

Returns `{markdown, token_estimate, char_count}`. 33K chars from a typical long-form article — about 8.5K tokens. Now you know before you paste.

It's open source, MIT licensed, self-hostable in one command. I built this because I needed it. Sharing because maybe you do too.

[GitHub](https://github.com/MrDwarf7/url-to-md) · [Web tool](https://url2md.com)

---

## Reddit Post — r/ClaudeAI

**Title:** url2md — free tool that converts any URL to clean markdown with token counts

**Body:**

Posting this here because I built it for exactly this workflow — pasting web content into Claude.

The problem: you find a good article, select all, copy, paste into Claude. You get the article text mixed with nav menus, cookie banners, "you might also like" sections, and a bunch of invisible HTML artifacts. Half your context window eaten by junk.

url2md fixes that. Give it a URL, get back just the article body as clean markdown. Plus a token estimate so you know if it fits in your remaining context.

No signup. No API key. No "free trial." Just a tool.

[GitHub](https://github.com/MrDwarf7/url-to-md)

---

## Reddit Post — r/webdev

**Title:** Built a free URL→Markdown API for feeding clean content to LLMs

**Body:**

Quick side project I shipped this weekend. If you're building anything that needs to pull web content into an LLM context window — RAG pipeline, AI coding tool integration, content analysis — you've probably hit the same annoyance I did: raw HTML is garbage for language models.

[url2md](https://github.com/MrDwarf7/url-to-md) takes a URL and returns clean markdown. Uses readability extraction (same algo as reader mode in browsers), converts to proper markdown with token counts.

Free API, no signup needed. Self-hostable with Docker in about 30 seconds.

Would love feedback on edge cases — I know certain SPA-heavy sites will probably break. Open issues on GitHub if you hit any.

---

## Hacker News — Show HN

**Title:** Show HN: url2md – Free URL to Markdown API for LLM context windows

**Body:**

I built url2md because I was tired of copy-pasting web pages into Claude and losing half my context window to navigation menus and cookie banners.

It takes a URL, runs readability extraction, and returns clean markdown with a token estimate. Free API, no signup required. 30 requests/hour per IP.

Technical details:
- Readability via mozilla/readability (same as Firefox Reader View)
- html2text for HTML→Markdown conversion
- FastAPI backend, ~150 lines of Python
- Rate limiting built in, no Redis needed
- Docker-ready, deployable anywhere

Open source, MIT licensed: https://github.com/MrDwarf7/url-to-md

---

## X/Twitter Thread

**Tweet 1:**
Just shipped url2md — a free URL→Markdown converter built for LLM workflows.

Paste any URL, get clean markdown. Strips the junk. Shows token counts.

No signup. No API key. Just curl it.

https://github.com/MrDwarf7/url-to-md

**Tweet 2:**
The problem it solves:

You find a great doc page. Copy it into Claude. Half your context window is now nav bars, cookie banners, and "related articles."

url2md runs readability extraction + converts to clean markdown. 33K chars from a typical article → ~8.5K tokens.

**Tweet 3:**
The API is dead simple:

curl "url2md.com/api/convert?url=https://example.com"

Returns {markdown, token_estimate, char_count}.

30 requests/hour free. Self-hostable with Docker. MIT license.

Built this in a weekend because I needed it. Sharing because you probably do too.
