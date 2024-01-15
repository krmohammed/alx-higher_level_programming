#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state,
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
            "SELECT cities.name \
                    FROM states JOIN cities ON cities.state_id = states.id \
                    WHERE states.name LIKE %s \
                    ORDER BY cities.id ASC", (sys.argv[4],))
    rows = c.fetchall()

    for row in rows:
        for i in row:
            print(i, end='')
        if row != rows[-1]:
            print(", ", end='')

    c.close()
    conn.close()
