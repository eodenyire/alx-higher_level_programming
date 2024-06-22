#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Check if exactly 4 arguments are provided
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py <username> <password> <database_name> <state_name>")
        sys.exit(1)

    # Capture command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to fetch states matching the state_name
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"
    cursor.execute(query, (state_name,))

    # Fetch all rows using fetchall() method
    rows = cursor.fetchall()

    # Print each state in the format (id, name)
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
