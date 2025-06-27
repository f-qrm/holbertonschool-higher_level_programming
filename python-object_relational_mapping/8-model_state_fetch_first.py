#!/usr/bin/python3
"""
This script connects to a MySQL database using SQLAlchemy and
prints the first State object sorted by id from the 'states' table.

Usage:
    ./8-model_state_fetch_first.py <mysql_username> <mysql_password>
    <database_name>

If no states are found in the database, it prints "Nothing".

Requirements:
- Uses SQLAlchemy ORM
- Imports State and Base from model_state
- Connects to a local MySQL server on port 3306
- Does not execute code when imported

Example:
    $ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
    1: California
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
    states = session.query(State).order_by(State.id).first()
    if states:
        print(f"{states.id}: {states.name}")
    else:
        print("Nothing")
    session.close()
