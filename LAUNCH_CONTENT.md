# url2md Launch Content

## Reddit Post — r/LocalLLaMA

**Title:** I got tired of pasting garbage HTML into LLMs, so I built a URL→Markdown converter

**Body:**

Every morning I'd find a good doc page, copy the whole thing, paste it into Claude. Half my context window — gone. Not to the actual content. To a cookie banner, a nav menu, three sidebar widgets, and whatever else the page decided to load.

So I built [url2md](https://github.com/MrDwarf7/url-to-md). You give it a URL. It gives you back clean markdown. That's the whole product.

What it actually does:
- Runs readability extraction — same algo as Firefox Reader View, so it knows what's the article and what's junk
- Converts to markdown with proper headings, links, code blocks intact
- Gives you a token count upfront. A typical long article runs about 33K chars, roughly 8.5K tokens. Now you know before you paste.
- Free API. 30 requests per hour, no signup, no API key. Just curl it.

```bash
curl "https://url2md.com/api/convert?url=https://your-article-url.com"
```

Returns `{markdown, token_estimate, char_count}`. JSON. Done.

I open-sourced it because I'm tired of every useful tool locking basic features behind a login wall. MIT license, self-hostable with Docker in about 30 seconds.

[GitHub](https://github.com/MrDwarf7/url-to-md)

---

## Reddit Post — r/ClaudeAI

**Title:** url2md — URL to clean markdown with token counts (free, no signup)

**Body:**

Built this for my own workflow and figured others hit the same wall.

The problem: you find a useful article, select all, copy, paste into Claude. What you get is the article text mixed with navigation, cookie consent popups, "you might also like" sections, and a pile of invisible HTML artifacts. Half your context eaten by stuff that has nothing to do with what you're trying to learn.

url2md strips all of that. Give it a URL, get back just the article as clean markdown. It also shows you the token estimate so you can see if it fits in your remaining context window.

No signup. No API key. No "free tier with upgrade pressure." Just a tool.

[GitHub](https://github.com/MrDwarf7/url-to-md)

---

## Reddit Post — r/webdev

**Title:** Free URL→Markdown API for feeding clean content to LLMs

**Body:**

Shipped this over the weekend. If you're building anything that pulls web content into an LLM — RAG pipeline, AI coding tool integration, content analysis — you've probably hit the same wall: raw HTML is terrible for language models.

[url2md](https://github.com/MrDwarf7/url-to-md) takes a URL and returns clean markdown. Uses readability extraction (same algo as browser reader modes), converts to proper markdown with token counts.

Free API, no signup. Self-host with Docker in 30 seconds.

If you hit edge cases — especially SPA-heavy sites — open an issue on GitHub. I know some will break and I want to fix them.

---

## Hacker News — Show HN

**Title:** Show HN: url2md – Free URL-to-Markdown API for LLM context windows

**Body:**

I was pasting web pages into Claude and losing half my context window to cookie banners and nav menus. Built url2md to fix that.

It takes a URL, runs mozilla/readability for extraction, converts to clean markdown via html2text, and returns a token estimate. Free API, no signup, 30 req/hour per IP.

Tech stack:
- FastAPI, ~150 lines of Python
- Rate limiting built in, no Redis needed
- Docker-ready, deployable anywhere
- MIT licensed

I know the readability extraction will choke on some SPAs. That's on the roadmap. For now it handles blogs, docs, and news sites well.

GitHub: https://github.com/MrDwarf7/url-to-md

---

## X/Twitter Thread

**Tweet 1:**
I was sick of pasting web pages into Claude and watching half my context window disappear into cookie banners.

So I built url2md. URL in, clean markdown out. Free API, no signup.

https://github.com/MrDwarf7/url-to-md

**Tweet 2:**
Here's what it does under the hood:

- mozilla/readability (same as Firefox Reader View) strips the junk
- html2text converts to clean markdown
- Token count included — 33K chars from a typical article, about 8.5K tokens

You know exactly what you're pasting before you paste it.

**Tweet 3:**
The API is one curl command:

curl "url2md.com/api/convert?url=https://example.com"

30 requests/hour free. No API key. MIT license. Docker self-host in 30 seconds.

Built it because I needed it. Sharing because maybe you do too.
