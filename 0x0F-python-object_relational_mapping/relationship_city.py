#!/usr/bin/python3
"""
Contains the class definition of City, inheriting from Base.

This module defines the City class, which represents cities in a database
and inherits from the SQLAlchemy declarative Base.

Classes:
    City: A SQLAlchemy mapped class representing cities.

Attributes:
    __tablename__ (str): The name of the database table ('cities').
    id (Column): Primary key column for city ID.
    name (Column): Column for city name, with a maximum length of 128 characters.
    state_id (Column): Foreign key column linking to the 'states' table.

Dependencies:
    Base (Base): SQLAlchemy declarative base for class mapping, imported from relationship_state.
"""
from relationship_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """inherits from Base"""
    __tablename__ = "cities"
    id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        unique=True,
        autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
