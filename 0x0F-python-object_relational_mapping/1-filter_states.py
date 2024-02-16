#!/usr/bin/python3
""" lists all states starting with N """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
    )

    curr = db.cursor()
    curr.execute(
            "SELECT *"
            "FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
            )
    states = curr.fetchall()

    for state in states:
        print(state)

    curr.close()
    db.close()
