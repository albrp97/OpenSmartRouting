.PHONY: check format lint types deadcode test

# Run the full local quality gate: format check, lint, type check, dead code, then tests.
# Fails fast on the first failing step (make stops at the first non-zero exit code).
check: format lint types deadcode test
	@echo "All checks passed."

format:
	uv run ruff format --check .

lint:
	uv run ruff check .

types:
	uv run mypy

deadcode:
	uv run vulture src tests

test:
	uv run pytest --cov=opensmartrouting --cov-report=term-missing
