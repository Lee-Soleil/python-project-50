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

lint:
	uv run ruff check gendiff

test-coverage:
	poetry run pytest --cov --cov-report xml

