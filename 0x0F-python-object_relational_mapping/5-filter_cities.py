#!/usr/bin/python3
""" lists all cities of a state """
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
            "SELECT cities.name \
            FROM cities JOIN states ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %s \
            ORDER BY cities.id ASC", (sys.argv[4],)
    )

    cities = curr.fetchall()
    cities_2 = ", ".join(city[0] for city in cities)

    print(cities_2)
