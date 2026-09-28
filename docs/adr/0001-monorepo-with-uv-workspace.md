# 0001. Monorepo with a uv workspace

- **Status:** Accepted
- **Date:** 2026-09-28

## Context

RelocateRadar has several parts: a reusable search library, a crawler, an API, a frontend, and
an evaluation harness. They change together while the project is young. We also want the search
library to be publishable to PyPI on its own.

## Decision

- Keep one repository. The Python code is a single **uv workspace** with members
  `packages/hybrid-search`, `apps/api`, and `apps/crawler`, sharing one `uv.lock` and one virtualenv.
- Each Python member is its own installable project (`src/` layout, hatchling build backend), so
  it can be built and published independently.
- `packages/hybrid-search` has **no dependency on anything in `apps/`**. Dependencies only point
  from apps to packages. It is the only code held to `mypy --strict` in CI.
- Lint, format, and test config (ruff, pytest, mypy) lives once in the root `pyproject.toml`.
- `apps/web` is a separate pnpm project. It is not part of the uv workspace.
- CI runs one job for Python and one for the web app. Tests are offline, so CI does not need
  Postgres or Qdrant services.

## Consequences

- One `uv sync --all-packages` gives a working dev environment for all Python code.
- Cross-package changes (for example, a library API change plus the API app update) land in one
  commit.
- A single lockfile means all Python members share dependency versions. That is fine at this
  scale, but a conflict between the crawler's and the API's dependencies would have to be
  resolved workspace-wide.
- The "library never imports apps" rule is enforced by convention and review for now. Adding an
  import-linter check to CI is a possible follow-up.
