#!/usr/bin/python3
"""
Adds a new State object 'Louisiana' to the database hbtn_0e_6_usa
and prints the new state's ID.

Usage:
    ./11-model_state_insert.py <mysql_username> <mysql_password> <database_name>
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
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(f"{new_state.id}")
    session.close()
