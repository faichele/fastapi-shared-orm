"""SQLAlchemy ORM-Core.

Wichtig:
Important:
- Hier gibt es bewusst KEINE Engine und KEINE Session.
- Engine and Session are deliberately omitted here
- Apps using this module are responsible for creating and configuring Engine and Session themselves.
- All SQLAlchemy Models that are intended to be created in a database must inherit from this Base class.

Optional:
- Naming conventions are provided to help Alembic generate stable constraint names.
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
