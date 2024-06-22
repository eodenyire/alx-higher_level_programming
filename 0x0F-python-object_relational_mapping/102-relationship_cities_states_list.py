#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Check if exactly 3 arguments are provided
    if len(sys.argv) != 4:
        print("Usage: ./102-relationship_cities_states_list.py <username> <password> <database_name>")
        sys.exit(1)

    # Capture command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL database using SQLAlchemy
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects with their associated State objects
    cities = session.query(City).order_by(City.id).all()

    # Print results in the format <city id>: <city name> -> <state name>
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()
