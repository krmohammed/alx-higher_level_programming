#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    c = conn.cursor()
    c.execute(
            "SELECT cities.id, cities.name, states.name \
                    FROM cities join states on cities.state_id = states.id \
                    ORDER BY cities.id ASC")
    rows = c.fetchall()

    for row in rows:
        print(row)

    c.close()
    conn.close()
