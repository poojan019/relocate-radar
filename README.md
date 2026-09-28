# RelocateRadar

[![CI](https://github.com/poojan019/relocate-radar/actions/workflows/ci.yml/badge.svg)](https://github.com/poojan019/relocate-radar/actions/workflows/ci.yml)

A search engine for English-speaking tech jobs in Germany, with EU Blue Card salary checks.

> Status: early scaffold. See each app/package README for details.

## Repo layout

| Path                                                | What                                                                  |
| --------------------------------------------------- | --------------------------------------------------------------------- |
| [`packages/hybrid-search`](packages/hybrid-search)  | Standalone library: Postgres full-text + Qdrant vectors, fused by RRF |
| [`apps/crawler`](apps/crawler)                      | Scrapy project that ingests and normalizes job postings               |
| [`apps/api`](apps/api)                              | FastAPI service, with search backed by `hybrid-search`                |
| [`apps/web`](apps/web)                              | Next.js (App Router, TS strict) frontend                              |
| [`eval`](eval)                                      | Search-quality evaluation (nDCG@10, recall@20)                        |
| [`docs/adr`](docs/adr)                              | Architecture Decision Records                                         |

## Quickstart

Prerequisites: Python 3.12, [uv](https://docs.astral.sh/uv/), Node 22 + pnpm, Docker.

```bash
cp .env.example .env
make up            # Postgres + Qdrant via docker compose
make install       # uv sync --all-packages
make web-install   # pnpm install in apps/web

make lint typecheck test   # Python checks
make web-check             # web lint + typecheck + tests
```

CI (`.github/workflows/ci.yml`) runs the same checks on every push and PR to `main`.
