# hybrid-search

Standalone Python library for hybrid search: PostgreSQL full-text search + Qdrant vector search,
merged with reciprocal rank fusion (RRF), with pluggable embedders.

> Status: scaffold only. The public API lands in upcoming commits.

## Design constraints

- **No imports from `apps/`.** The package is meant to be published to PyPI independently.
- Fully typed (`py.typed`), checked with `mypy --strict`.
- Tests are fast and offline (no running Postgres/Qdrant required).

## Development

From the repo root:

```bash
uv sync --all-packages
uv run pytest packages/hybrid-search
uv run mypy packages/hybrid-search/src packages/hybrid-search/tests
```
