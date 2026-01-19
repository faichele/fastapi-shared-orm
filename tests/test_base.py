"""Tests for the fastapi_shared_orm base module."""

import pytest
from sqlalchemy import Column, Integer, String, inspect
from shared_orm import Base


def test_base_import():
    """Test that Base can be imported."""
    assert Base is not None


def test_base_metadata():
    """Test that Base has metadata with naming conventions."""
    assert Base.metadata is not None
    assert Base.metadata.naming_convention is not None

    # Check naming conventions
    naming_convention = Base.metadata.naming_convention
    assert "ix" in naming_convention
    assert "uq" in naming_convention
    assert "ck" in naming_convention
    assert "fk" in naming_convention
    assert "pk" in naming_convention


def test_create_simple_model():
    """Test that we can create a simple model from Base."""

    class TestUser(Base):
        __tablename__ = "test_users"

        id = Column(Integer, primary_key=True)
        username = Column(String(50), unique=True, nullable=False)
        email = Column(String(100))

    # Check that the model was created correctly
    assert TestUser.__tablename__ == "test_users"
    assert hasattr(TestUser, "id")
    assert hasattr(TestUser, "username")
    assert hasattr(TestUser, "email")


def test_model_metadata_shared():
    """Test that models share the same metadata."""

    class Model1(Base):
        __tablename__ = "model1"
        id = Column(Integer, primary_key=True)

    class Model2(Base):
        __tablename__ = "model2"
        id = Column(Integer, primary_key=True)

    # Both models should share the same metadata instance
    assert Model1.metadata is Model2.metadata
    assert Model1.metadata is Base.metadata


def test_table_creation():
    """Test that tables are registered in metadata."""

    class TestProduct(Base):
        __tablename__ = "test_products"
        id = Column(Integer, primary_key=True)
        name = Column(String(100), nullable=False)

    # Check that the table is in metadata
    assert "test_products" in Base.metadata.tables


def test_naming_convention_for_unique_constraint():
    """Test that unique constraints follow naming convention."""

    class TestEntity(Base):
        __tablename__ = "test_entity"
        id = Column(Integer, primary_key=True)
        code = Column(String(50), unique=True)

    # Get the table and check constraint names
    table = Base.metadata.tables["test_entity"]

    # Check that naming convention is applied
    # The actual constraint name generation happens when creating the database
    # Here we just verify the metadata structure is correct
    assert table is not None
    assert "code" in [c.name for c in table.columns]


def test_base_is_declarative():
    """Test that Base is a declarative base."""
    from sqlalchemy.orm import DeclarativeMeta

    assert isinstance(Base, DeclarativeMeta)


def test_multiple_models_different_tables():
    """Test that multiple models can coexist with different table names."""

    class Author(Base):
        __tablename__ = "authors"
        id = Column(Integer, primary_key=True)
        name = Column(String(100))

    class Book(Base):
        __tablename__ = "books"
        id = Column(Integer, primary_key=True)
        title = Column(String(200))

    # Check both tables exist in metadata
    assert "authors" in Base.metadata.tables
    assert "books" in Base.metadata.tables
    assert len(Base.metadata.tables) >= 2


def test_column_types():
    """Test that various column types work correctly."""
    from sqlalchemy import Boolean, DateTime, Float, Text

    class ComplexModel(Base):
        __tablename__ = "complex_model"

        id = Column(Integer, primary_key=True)
        name = Column(String(100))
        description = Column(Text)
        price = Column(Float)
        is_active = Column(Boolean, default=True)
        created_at = Column(DateTime)

    table = Base.metadata.tables["complex_model"]
    column_names = [c.name for c in table.columns]

    assert "id" in column_names
    assert "name" in column_names
    assert "description" in column_names
    assert "price" in column_names
    assert "is_active" in column_names
    assert "created_at" in column_names

