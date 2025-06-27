#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.

Usage:
    ./13-model_state_delete_a.py <mysql_username> <mysql_password>
    <database_name>

- Connects to a MySQL server running on localhost at port 3306.
- Uses SQLAlchemy ORM.
- Imports State and Base from model_state.
- Filters State objects where name contains 'a'.
- Deletes them from the session.
- Commits the changes to apply deletion in the database.

Example:
    $ ./13-model_state_delete_a.py root root hbtn_0e_6_usa
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
        session.delete(state)
    session.commit()
    session.close()
