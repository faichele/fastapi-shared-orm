.PHONY: help install install-dev test lint format type-check clean build upload

help:
	@echo "Verfügbare Befehle:"
	@echo "  make install       - Installiere das Paket im Development-Modus"
	@echo "  make install-dev   - Installiere mit Development-Dependencies"
	@echo "  make test          - Führe Tests aus"
	@echo "  make test-cov      - Führe Tests mit Coverage-Report aus"
	@echo "  make lint          - Prüfe Code mit ruff"
	@echo "  make format        - Formatiere Code mit black"
	@echo "  make type-check    - Type-Checking mit mypy"
	@echo "  make clean         - Entferne Build-Artefakte"
	@echo "  make build         - Baue das Paket"
	@echo "  make upload        - Lade das Paket zu PyPI hoch"

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

test:
	pytest tests/ -v

test-cov:
	pytest tests/ -v --cov=shared_orm --cov-report=html --cov-report=term-missing

lint:
	ruff check shared_orm tests

lint-fix:
	ruff check --fix shared_orm tests

format:
	black shared_orm tests

type-check:
	mypy shared_orm

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf htmlcov
	rm -rf .coverage
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build: clean
	python -m build

upload: build
	twine upload dist/*

check-all: lint type-check test
	@echo "Alle Checks erfolgreich!"

