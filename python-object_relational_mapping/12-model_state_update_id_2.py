#!/usr/bin/python3
"""
12-model_state_update_id_2.py

Updates the name of the State object with id = 2 to 'New Mexico'
in the database hbtn_0e_6_usa.

Usage:
    ./12-model_state_update_id_2.py <mysql_username> <mysql_password>
    <database_name>

- Connects to a MySQL server on localhost at port 3306
- Uses SQLAlchemy ORM
- Imports State and Base from model_state
- Changes the name of the State with id=2 to 'New Mexico'
- Script should not execute when imported
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
    states = session.query(State).filter_by(id=2).first()
    if states:
        states.name = "New Mexico"
        session.commit()
    session.close()
