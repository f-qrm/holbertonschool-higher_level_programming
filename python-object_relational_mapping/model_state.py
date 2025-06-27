#!/usr/bin/python3
"""
This module defines the State class and the Base instance
used for SQLAlchemy ORM mapping to the MySQL 'states' table.

Classes:
    State: ORM-mapped class representing a row in the 'states' table.

Attributes:
    Base (declarative_base): Base class for SQLAlchemy class definitions.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

user = sys.argv[1]
passwd = sys.argv[2]
DB_name = sys.argv[3]

Base = declarative_base()


class State(Base):
    """
    Represents a state in the 'states' table of a MySQL database.

    Attributes:
        id (int): The state's unique ID, primary key, auto-incremented
        not null.
        name (str): The name of the state (max 128 characters), not null.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
