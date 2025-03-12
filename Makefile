install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl

check:
	uv run ruff check gendiff

test-coverage:
	uv run pytest --cov-report xml:coverage.xml
