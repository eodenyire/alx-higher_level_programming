#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists
all cities of that state.
This script is SQL injection safe.
Example usage: ./5-filter_cities.py root root
hbtn_0e_4_usa 'California'
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.name FROM cities JOIN states ON \
cities.state_id = states.id WHERE states.name = %s",
        (sys.argv[4],
         ))
    query_rows = cur.fetchall()
    my_list = []
    for row in query_rows:
        my_list.append(",".join(str(x) for x in row))
    print(*my_list, sep=", ")
    cur.close()
    conn.close()
