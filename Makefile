install:
	uv sync

gendiff:
	uv run gendiff

build:
	uv build

publish:
	poetry publish --dry-run

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl

lint:
	poetry run flake8 gendiff

test-coverage:
	poetry run pytest --cov --cov-report xml
