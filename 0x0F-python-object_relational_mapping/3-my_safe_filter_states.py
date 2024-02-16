#!/usr/bin/python3
""" displays all values in the states with a match """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    curr = db.cursor()
    curr.execute(
            "SELECT * FROM states \
                WHERE name LIKE BINARY %s ORDER BY id \
                ASC", (sys.argv[4],)
            )
    states = curr.fetchall()

    for state in states:
        print(state)

    curr.close()
    db.close()
