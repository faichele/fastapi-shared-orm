"""Gemeinsamer ORM-Core für alle Apps/Packages.

Dieses Paket stellt die SQLAlchemy-Declarative-Base (und damit eine gemeinsame
`MetaData`) bereit. Alle SQLAlchemy-Modelle (App-Modelle wie auch Package-Modelle)
MÜSSEN von dieser Base erben, wenn sie in dieselbe Datenbank/Migrations-Welt
gehören.
"""

from .base import Base

__all__ = ["Base"]

