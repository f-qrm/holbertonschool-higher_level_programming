#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database
hbtn_0e_6_usa.

Usage:
    ./9-model_state_filter_a.py <mysql_username> <mysql_password>
    <database_name>

- Connects to a MySQL server on localhost at port 3306.
- Uses SQLAlchemy ORM.
- Imports State and Base from model_state.
- Filters State objects where the name contains the letter 'a'.
- Results are sorted in ascending order by states.id.
- Displays: <state.id>: <state.name>

Example:
    $ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
    1: California
    2: Arizona
    3: Texas
    5: Nevada
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
    states = session.query(State).filter(
        State.name.like("%a%")
        ).order_by(
            State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")
    session.close()
