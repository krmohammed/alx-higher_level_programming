#!/usr/bin/python3
"""
reads data from students table
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from students import Base, Student


if __name__ == "__main__":
    user = "root"
    passwd = "kumbisal"
    db = "mqi"
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, passwd, db)
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    males = session.query(Student).filter(Student.gender == "Male")
    females = session.query(Student).filter(Student.gender == "Female")

    print("                                           ")
    print("===========================================")
    print("                                           ")

    for male in males:
        print(
            "{} is a {} student, he lives in {}.".format(
                male.first_name, male.programme, male.hall
            )
        )

    print("                                                        ")
    print("========================================================")
    print("                                                        ")

    for female in females:
        print(
            "{} is a {} student, she lives in {}.".format(
                female.first_name, female.programme, female.hall
            )
        )
