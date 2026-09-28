# RelocateRadar
 
Search engine for English-speaking tech jobs in Germany, with EU Blue Card salary checks.
This is a portfolio project: code quality, tests, and documented decisions matter as much as features.
 
## Repo layout (monorepo)
 
- `packages/hybrid-search/` — standalone Python library: hybrid search over PostgreSQL full-text + Qdrant vectors
  (reciprocal rank fusion, pluggable embedders). Published to PyPI later. MUST NOT import anything from `apps/`.
- `apps/crawler/` — Scrapy project. Ingests job postings, normalizes them, writes to Postgres.
- `apps/api/` — FastAPI service. Search endpoint uses `packages/hybrid-search`.
- `apps/web/` — Next.js (App Router, TypeScript strict) frontend.
- `eval/` — search-quality evaluation: labeled queries, nDCG@10 / recall@20, compares keyword vs vector vs hybrid.
- `docs/adr/` — Architecture Decision Records (one short markdown file per significant decision).
- `docker-compose.yml` — Postgres + Qdrant for local development.
## Conventions
 
- Python 3.12, `uv` for dependencies, `ruff` for lint/format, `mypy --strict` on `packages/`, `pytest` for tests.
- TypeScript strict mode, `vitest` for tests, Zod for runtime validation of API responses.
- Every feature ships with tests. Library code aims for high coverage; keep tests fast and offline.
- Conventional commits (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`).
- When making a non-obvious design choice, add an ADR in `docs/adr/NNNN-title.md` (context, decision, consequences).
- Keep READMEs current: each app/package has its own README with setup + usage.
## Crawling rules
 
- Prefer official APIs and feeds (e.g. Arbeitnow's public API) over HTML scraping.
- Respect robots.txt, identify with a clear User-Agent, rate-limit politely (AutoThrottle on).
- Store job metadata and a link to the original posting; do not republish full descriptions.
- Tests use recorded fixtures in `apps/crawler/tests/fixtures/` — never hit live sites in tests.
## Domain notes
 
- Blue Card check: flag jobs whose stated minimum gross annual salary meets the current threshold.
  Keep the threshold in config (per year), never hardcoded in logic — it changes every January.
- Salary text is messy (ranges, monthly vs yearly, "k", EUR/€). Parsing lives in one tested module.
## Working style for Claude
 
- For larger tasks, propose a plan first; keep changes scoped to the task asked.
- Run lint + tests before finishing; report anything that could not be verified.
- Cloud sessions have restricted network access: don't assume job sites are reachable; use fixtures.
 