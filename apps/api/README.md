# relocate-api

FastAPI service for RelocateRadar. The search endpoint will be backed by
[`packages/hybrid-search`](../../packages/hybrid-search).

> Status: scaffold only. It exposes `GET /health`.

## Run locally

From the repo root:

```bash
uv sync --all-packages
uv run uvicorn relocate_api.main:app --reload
# -> http://localhost:8000/health, docs at http://localhost:8000/docs
```

## Test

```bash
uv run pytest apps/api
```
