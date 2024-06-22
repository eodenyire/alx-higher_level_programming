#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connect to MySQL database
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to fetch all states ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id")

    # Fetch all rows using fetchall() method
    rows = cursor.fetchall()

    # Print each state in the format (id, name)
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
