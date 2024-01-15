#!/usr/bin/python3
"""
prints the first State object from the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]
        ))
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).first()
    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print()
