#!/usr/bin/python3
"""
Contains the class definition of State and the declaration of Base.

This module defines the State class and initializes the Base instance
for SQLAlchemy's declarative base.

Classes:
    State: A SQLAlchemy mapped class representing states in a database.

Attributes:
    __tablename__ (str): The name of the database table ('states').
    id (Column): Primary key column for state ID.
    name (Column): Column for state name, with a maximum length of 128 characters.

Instance:
    Base (Base): SQLAlchemy declarative base for class mapping.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """inherits from base, links to mysql table states"""
    __tablename__ = 'states'
    id = Column(
        Integer,
        unique=True,
        nullable=False,
        autoincrement=True,
        primary_key=True)
    name = Column(String(128), nullable=False)
