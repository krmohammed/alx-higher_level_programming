#!/usr/bin/python3
"""script that takes in an argument andd displays all values in the states
"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cursor = conn.cursor()
    cursor.execute(
            "SELECT * FROM states \
                    WHERE name LIKE BINARY %s ORDER BY id \
                    ASC", (sys.argv[4],)
            )
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conn.close()
