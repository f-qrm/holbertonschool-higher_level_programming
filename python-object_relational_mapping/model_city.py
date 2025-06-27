#!/usr/bin/python3
"""
Defines the City class for SQLAlchemy ORM mapping to the 'cities' table.

Classes:
    City: Inherits from Base (defined in model_state).
          Represents a city with id, name, and state_id attributes.

Attributes:
    __tablename__ (str): Name of the MySQL table to map (cities).
    id (int): Primary key, auto-incremented, non-nullable.
    name (str): Name of the city, max 128 characters, non-nullable.
    state_id (int): Foreign key referencing State.id, non-nullable.

Note:
    - Base is imported from model_state.
    - This model is used in scripts interacting with the hbtn_0e_14_usa
    database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
Base = declarative_base()


class City(Base):
    """
    Represents a city mapped to the 'cities' table in the database.

    Attributes:
        id (int): The primary key for the city, auto-incremented and not
        nullable.
        name (str): The name of the city, max length 128 characters, not
        nullable.
        state_id (int): Foreign key referencing the id of the associated
        State, not nullable.

    Notes:
        - Inherits from Base, imported from model_state.
        - Used to link cities to their respective states in the
        hbtn_0e_14_usa database.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, foreign_key=True, nullable=False)
