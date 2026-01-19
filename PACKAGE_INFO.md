# Shared ORM Package - Struktur & Verwendung

## 📦 Package-Struktur

```
shared_orm/
├── __init__.py              # Package-Einstiegspunkt, exportiert Base
├── base.py                  # SQLAlchemy Base und Metadata mit Naming Conventions
├── py.typed                 # PEP 561 Typ-Marker für Type Hints
├── pyproject.toml           # Moderne Python-Package-Konfiguration
├── setup.cfg                # Zusätzliche Setup-Konfiguration
├── requirements.txt         # Produktions-Abhängigkeiten
├── requirements-dev.txt     # Development-Abhängigkeiten
├── README.md                # Hauptdokumentation
├── CHANGELOG.md             # Versionshistorie
├── LICENSE                  # MIT-Lizenz
├── MANIFEST.in              # Package-Metadaten
├── Makefile                 # Build- und Test-Befehle
├── install.sh               # Installations-Skript
├── .gitignore               # Git-Ignore-Regeln
└── tests/
    ├── __init__.py
    └── test_base.py         # Unit-Tests für Base

```

## 🚀 Installation & Verwendung

### Schnellstart

```bash
# In das Package-Verzeichnis wechseln
cd packages/fastapi_shared_orm

# Im Development-Modus installieren
make install-dev

# Tests ausführen
make test

# Code formatieren
make format

# Linting
make lint

# Type-Checking
make type-check
```

### Verwendung in anderen Packages

In der `pyproject.toml` des abhängigen Packages:

```toml
[project]
dependencies = [
    "shared-orm>=0.1.0",
]
```

Dann in Python:

```python
from shared_orm import Base
from sqlalchemy import Column, Integer, String

class MyModel(Base):
    __tablename__ = "my_table"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
```

## 🏗️ Build & Distribution

### Paket bauen

```bash
make build
# oder
python -m build
```

Erzeugt:
- `dist/shared_orm-0.1.0-py3-none-any.whl` (Wheel)
- `dist/shared-orm-0.1.0.tar.gz` (Source Distribution)

### Auf PyPI hochladen (optional)

```bash
make upload
# oder
twine upload dist/*
```

## 🧪 Testing

```bash
# Einfache Tests
make test

# Tests mit Coverage
make test-cov

# Alle Checks
make check-all
```

## 📋 Vorteile dieser Architektur

### 1. **Zentrale Base-Klasse**
- Alle Modelle im gesamten Projekt erben von derselben Base
- Gemeinsame `MetaData` ermöglicht globale Migrations mit Alembic
- Verhindert Probleme mit mehreren MetaData-Instanzen

### 2. **Konsistente Naming Conventions**
- Automatische Benennung von Constraints (PK, FK, Unique, etc.)
- Stabile Namen über verschiedene Datenbank-Backends
- Vereinfacht Debugging und Migrations

### 3. **Modularer Aufbau**
- Package ist unabhängig von konkreten DB-Verbindungen
- Kann in mehreren Projekten wiederverwendet werden
- Klare Trennung von Verantwortlichkeiten

### 4. **Type Safety**
- PEP 561 konform (`py.typed`)
- Vollständige Type-Hint-Unterstützung
- IDE-Autovervollständigung funktioniert optimal

## 🔧 Development-Workflow

### Neue Feature hinzufügen

1. Branch erstellen
2. Code ändern in `base.py` oder neue Module hinzufügen
3. Tests schreiben in `tests/`
4. Tests ausführen: `make test`
5. Code formatieren: `make format`
6. Linting: `make lint`
7. Type-Check: `make type-check`
8. Pull Request erstellen

### Version veröffentlichen

1. Version in `pyproject.toml` erhöhen
2. `CHANGELOG.md` aktualisieren
3. Paket bauen: `make build`
4. Testen der Distribution
5. Auf PyPI hochladen: `make upload`
6. Git-Tag erstellen: `git tag v0.1.0 && git push --tags`

## 📚 Weitere Ressourcen

- [SQLAlchemy Dokumentation](https://docs.sqlalchemy.org/)
- [Alembic Migrations](https://alembic.sqlalchemy.org/)
- [Python Packaging Guide](https://packaging.python.org/)
- [PEP 517 & 518](https://peps.python.org/pep-0517/)

## ❓ Häufige Fragen

**Q: Warum keine Engine/Session in diesem Package?**  
A: Dies ermöglicht Flexibilität. Jede Anwendung kann ihre eigenen DB-Verbindungsparameter definieren.

**Q: Kann ich mehrere Datenbanken verwenden?**  
A: Ja, aber alle Modelle, die von dieser Base erben, gehören zur selben MetaData. Für komplett getrennte DBs bräuchte man separate Bases.

**Q: Wie integriere ich dies mit Alembic?**  
A: In `alembic/env.py` importierst du `Base` aus diesem Package und setzt `target_metadata = Base.metadata`.

**Q: Muss ich dieses Package veröffentlichen?**  
A: Nein, du kannst es nur lokal installieren mit `pip install -e packages/shared_orm`.

