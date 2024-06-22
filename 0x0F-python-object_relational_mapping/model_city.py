#!/usr/bin/python3
"""
Defines the City class, mapped to the 'cities' table in the database.

Attributes:
    id (int): Unique identifier for each city, auto-incremented.
    name (str): Name of the city, maximum length of 128 characters.
    state_id (int): Foreign key referencing the 'id' column of the 'states' table.

This class inherits from SQLAlchemy's Base class, which is a declarative base
that allows SQLAlchemy to map classes to tables in the database.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

from model_state import Base, State


class City(Base):
    """inherits from Base"""
    __tablename__ = "cities"
    id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        unique=True,
        autoincrement=True)
    name = Column(String(128), nullable=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
