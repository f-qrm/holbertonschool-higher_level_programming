#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.

Usage:
    ./14-model_city_fetch_by_state.py <mysql_username> <mysql_password>
    <database_name>

Functionality:
    - Connects to a MySQL server running on localhost at port 3306.
    - Uses SQLAlchemy ORM to interact with the database.
    - Imports Base and State from model_state, and City from model_city.
    - Performs an inner join between City and State on state_id.
    - Orders the results by City.id in ascending order.
    - Prints the results in the format: <state name>: (<city id>) <city name>

Example:
    $ ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
"""
import sys
from model_state import Base, State
from model_city import City
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
    cities = session.query(City, State).join(
        State, City.state_id == State.id).order_by(City.id).all()
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
