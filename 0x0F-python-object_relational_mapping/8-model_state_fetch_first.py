#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
The script takes 3 arguments: MySQL username,
MySQL password, and database name.
Example usage: ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

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
    state = session.query(State).first()
    if not state:
        print("Nothing")
    print("{}: {}".format(state.id, state.name))
    session.close()
