"""SQLAlchemy ORM-Core.

Wichtig:
- Hier gibt es bewusst KEINE Engine und KEINE Session.
- Apps sind dafür verantwortlich, Engine/Session (und damit die DB-URL) zu bauen.
- Alle Modelle, die in derselben DB erstellt/migriert werden sollen, erben von
  dieser Base.

Optional:
- Naming Conventions helfen Alembic (Constraints werden stabil benannt).
"""

from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base


NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

metadata = MetaData(naming_convention=NAMING_CONVENTION)

Base = declarative_base(metadata=metadata)
