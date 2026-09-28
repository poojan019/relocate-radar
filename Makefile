.PHONY: install lint format typecheck test web-install web-check up down check

install:
	uv sync --all-packages

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff check --fix .
	uv run ruff format .

typecheck:
	uv run mypy packages/hybrid-search/src packages/hybrid-search/tests

test:
	uv run pytest

web-install:
	cd apps/web && pnpm install --frozen-lockfile

web-check:
	cd apps/web && pnpm lint && pnpm typecheck && pnpm test

check: lint typecheck test web-check

up:
	docker compose up -d --wait

down:
	docker compose down
