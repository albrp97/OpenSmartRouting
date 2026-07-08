.PHONY: check format lint test

# Run the full local quality gate: format check, lint, then tests.
# Fails fast on the first failing step (make stops at the first non-zero exit code).
check: format lint test
	@echo "All checks passed."

format:
	uv run ruff format --check .

lint:
	uv run ruff check .

test:
	uv run pytest
