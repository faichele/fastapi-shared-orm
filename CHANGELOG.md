# Changelog

All notable changes to the shared-orm package will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-01-13

### Added
- Initial release of shared-orm package
- SQLAlchemy Declarative Base with naming conventions
- Shared MetaData instance for all models
- Support for SQLAlchemy 2.0+
- PEP 561 type hints support (py.typed marker)
- Comprehensive documentation in README.md
- Development dependencies configuration
- pytest, black, ruff, mypy configuration

### Features
- Consistent naming conventions for database constraints:
  - Index: `ix_<column_name>`
  - Unique: `uq_<table_name>_<column_name>`
  - Check: `ck_<table_name>_<constraint_name>`
  - Foreign Key: `fk_<table_name>_<column_name>_<referred_table_name>`
  - Primary Key: `pk_<table_name>`

### Technical Details
- Requires Python 3.10+
- Compatible with SQLAlchemy 2.0+
- No database engine or session management (by design)
- Modular architecture for use across multiple packages

[Unreleased]: https://github.com/your-org/rideto/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/your-org/rideto/releases/tag/v0.1.0

