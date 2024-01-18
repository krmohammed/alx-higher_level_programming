#!/usr/bin/python3
"""
updates the details of students
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from students import Base, Student

if __name__ == "__main__":
    db = "mqi"
    user = "root"
    passwd = "kumbisal"

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, passwd, db)
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Student).filter(Student.hall.like("Unity%")).update(
        {"hall": "Conti"}
    )
    session.query(Student).filter(Student.hall.like("University%")).update(
        {"hall": "Katanga"}
    )
    session.commit()
