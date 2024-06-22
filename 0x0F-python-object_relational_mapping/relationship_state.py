#!/usr/bin/python3
"""
Contains the class definition of State and an instance Base = declarative_base().

This module defines the State class, representing states in a database and
inherits from the SQLAlchemy declarative Base. It also establishes a
relationship with the City class.

Classes:
    State: A SQLAlchemy mapped class representing states.

Attributes:
    __tablename__ (str): The name of the database table ('states').
    id (Column): Primary key column for state ID.
    name (Column): Column for state name, with a maximum length of 128 characters.
    cities (relationship): One-to-many relationship with City objects, representing cities in the state.

Dependencies:
    Base (Base): SQLAlchemy declarative base for class mapping, imported from sqlalchemy.ext.declarative.
    relationship (relationship): SQLAlchemy relationship function, imported from sqlalchemy.orm.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

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
    cities = relationship('City', cascade='all, delete', backref='state')
