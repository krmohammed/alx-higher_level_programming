#!/usr/bin/python3
"""
creates the students table
"""
from students import Base, Student
from sqlalchemy import (create_engine)

user = "root"
password = "kumbisal"
db = "mqi"

#creates student table
if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, password, db)
    )
    Base.metadata.create_all(engine)