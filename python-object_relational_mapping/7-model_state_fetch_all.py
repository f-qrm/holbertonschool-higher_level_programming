#!/usr/bin/python3
"""
This script connects to a MySQL database using SQLAlchemy and
lists all State objects from the database sorted by their id.

Usage:
    ./7-model_state_fetch_all.py <mysql_username> <mysql_password>
    <database_name>

Arguments:
    mysql_username    MySQL username
    mysql_password    MySQL password
    database_name     Name of the database to connect to

The script imports the State and Base classes from model_state,
connects to the MySQL server running on localhost at port 3306,
retrieves all states ordered by their id, and prints each state's
id and name in the format:
    <state.id>: <state.name>
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()
