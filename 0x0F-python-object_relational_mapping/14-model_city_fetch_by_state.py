#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa.
Takes 3 arguments: mysql username, mysql password, and database name.
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(
        City,
        State).filter(
        State.id == City.state_id).order_by(
            City.id)
    for (city, state) in query:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
