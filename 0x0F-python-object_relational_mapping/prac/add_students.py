#!/usr/bin/python3
"""
inserts a student into the student table
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from students import Base, Student


if __name__ == "__main__":
    user = "root"
    passwd = "kumbisal"
    db = "mqi"
    students = [
        Student(
            first_name="Irene",
            other_names="Fordjour",
            programme="BSc. Food Science and Technology",
            gender="Female",
            hall="Queens Hall",
        ),
        Student(
            first_name="Samuel",
            other_names="Konadu",
            programme="BSc. Forestry",
            gender="Male",
            hall="",
        ),
        Student(
            first_name="Mubashir",
            other_names="Salih",
            programme="BSc. Human Biology",
            gender="Male",
            hall="Africa Hall",
        ),
        Student(
            first_name="Khalilah",
            other_names="AbdurRahman",
            programme="BSc. Economics",
            gender="Female",
            hall="Unity Hall",
        ),
    ]
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, passwd, db)
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add_all(students)
    session.commit()
