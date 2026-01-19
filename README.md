# Shared ORM

Gemeinsamer SQLAlchemy ORM-Core für Rideto-Packages und -Anwendungen.

## Überblick

Dieses Paket stellt eine zentrale SQLAlchemy Declarative Base bereit, die von allen Datenbank-Modellen im Rideto-Projekt verwendet werden muss. Dies gewährleistet:

- **Gemeinsame Metadata**: Alle Modelle teilen dieselbe `MetaData`-Instanz
- **Konsistente Naming Conventions**: Automatische Benennung von Constraints (Primary Keys, Foreign Keys, Indexes, etc.)
- **Migrations-Kompatibilität**: Alembic kann alle Modelle erkennen und migrieren
- **Modularität**: Jedes Package kann eigene Modelle definieren, die automatisch Teil der gemeinsamen Datenbank werden

## Quick Start

```python
from shared_orm import Base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

# 1. Definiere dein Modell
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)

# 2. Erstelle Engine und Session (in deiner Hauptanwendung)
engine = create_engine("sqlite:///example.db")
SessionLocal = sessionmaker(bind=engine)

# 3. Erstelle alle Tabellen
Base.metadata.create_all(bind=engine)
```

## Installation

### Mit Make (empfohlen)

```bash
cd packages/fastapi_shared_orm
make install-dev  # Installiert mit Dev-Dependencies
make test         # Führt Tests aus
```

### Als Development-Dependency

Aus dem Rideto-Workspace:

```bash
pip install -e packages/fastapi_shared_orm
```

### Mit Development-Dependencies

```bash
pip install -e "packages/shared_orm[dev]"
```

### Produktiv-Installation

```bash
pip install shared-orm
```

## Verwendung

### Basis-Verwendung

```python
from shared_orm import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
```

### In einem Package

Jedes Package, das Datenbank-Modelle definiert, sollte `shared-orm` als Dependency haben:

```toml
# pyproject.toml des Packages
[project]
dependencies = [
    "shared-orm>=0.1.0",
    "sqlalchemy>=2.0.0",
]
```

### Naming Conventions

Das Paket definiert folgende Naming Conventions für Constraints:

- **Index**: `ix_<column_name>`
- **Unique Constraint**: `uq_<table_name>_<column_name>`
- **Check Constraint**: `ck_<table_name>_<constraint_name>`
- **Foreign Key**: `fk_<table_name>_<column_name>_<referred_table_name>`
- **Primary Key**: `pk_<table_name>`

Diese Konventionen sorgen für stabile und vorhersagbare Namen bei Migrations.

## Architektur-Hinweise

### Was dieses Paket NICHT enthält

- ❌ Keine SQLAlchemy Engine
- ❌ Keine Session/SessionLocal
- ❌ Keine Datenbankverbindungs-URL

### Verantwortlichkeiten

- ✅ **shared_orm**: Stellt die Base-Klasse und Metadata bereit
- ✅ **Anwendung** (z.B. `backend/`): Erstellt Engine, Session und verwaltet DB-Verbindungen
- ✅ **Packages**: Definieren eigene Modelle, die von `Base` erben

### Beispiel: Engine und Session in der Hauptanwendung

```python
# backend/database/base.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from shared_orm import Base

DATABASE_URL = "postgresql://user:password@localhost/dbname"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Alle Tabellen erstellen
Base.metadata.create_all(bind=engine)
```

## Migrations mit Alembic

In `alembic/env.py`:

```python
from shared_orm import Base

# Import aller Modelle, damit Alembic sie findet
from backend.database.models import User, Image, Album
from fastapi_users_auth.models import AuthUser
# ... weitere Modelle

target_metadata = Base.metadata
```

## Development

### Setup

```bash
cd packages/fastapi_shared_orm
pip install -e ".[dev]"
```

### Tests ausführen

```bash
pytest
```

### Code-Formatierung

```bash
black .
ruff check .
```

### Type-Checking

```bash
mypy fastapi_shared_orm
```

## Lizenz

MIT License

## Changelog

### 0.1.0 (2026-01-13)

- Initiale Version
- SQLAlchemy Declarative Base mit Naming Conventions
- Gemeinsame Metadata für alle Modelle

