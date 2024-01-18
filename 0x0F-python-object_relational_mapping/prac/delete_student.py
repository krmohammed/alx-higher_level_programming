#!/usr/bin/python3
"""
deletes a student from the table
"""
from students import Base, Student
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = "root"
    passwd = "kumbisal"
    db = "mqi"
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, passwd, db)
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    deleted = session.query(Student).filter(Student.hall == "").all()
    for i in deleted:
        session.delete(i)
    session.commit()
