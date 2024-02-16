#!/usr/bin/python3
""" lists all cities """
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
    curr.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            ORDER BY cities.id ASC")
    cities = curr.fetchall()

    for city in cities:
        print(city)

    curr.close()
    db.close()
