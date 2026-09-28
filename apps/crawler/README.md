# relocate-crawler

Scrapy project that ingests job postings, normalizes them, and writes them to Postgres.

> Status: scaffold only. It has polite settings and no spiders yet.

## Crawling rules

- Prefer official APIs/feeds (e.g. Arbeitnow's public API) over HTML scraping.
- Respect `robots.txt`, identify with a clear User-Agent, keep AutoThrottle on.
- Store metadata and a link to the original posting. Do not republish full descriptions.
- Tests use recorded fixtures in `tests/fixtures/` and never hit live sites.

## Usage

From `apps/crawler/`:

```bash
uv run scrapy list          # list spiders
uv run scrapy crawl <name>  # run one
```

## Test

From the repo root:

```bash
uv run pytest apps/crawler
```
