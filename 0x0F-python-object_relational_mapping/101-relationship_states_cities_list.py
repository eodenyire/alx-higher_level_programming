#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding
City objects,contained in the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Check if exactly 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./101-relationship_states_cities_list.py "
              "<username> <password> <database_name>")
        sys.exit(1)
    # Capture command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL database using SQLAlchemy
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and their associated City objects using the
    # cities relationship
    states = session.query(State).order_by(State.id).all()

    # Print the results in the required format
    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    # Close the session
i    session.close()
