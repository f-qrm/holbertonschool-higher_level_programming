#!/usr/bin/python3
"""
Searches for the first State object with a specific name from the
database hbtn_0e_6_usa.

Usage:
    ./10-model_state_my_get.py <mysql_username> <mysql_password>
    <database_name> <state_name>

- Connects to a MySQL server on localhost at port 3306.
- Uses SQLAlchemy ORM.
- Imports State and Base from model_state.
- Filters State objects where the name matches the provided argument.
- If found, prints the state's id.
- If not found, prints "Not found".

Example:
    $ ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
    3
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
    states = session.query(State).filter(State.name == sys.argv[4]).first()
    if states:
        print(f"{states.id}")
    else:
        print("Not found")
    session.close()
