#!/usr/bin/python3
"""
prints the State object with the name passed as argument
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name.like("{}".format(
        argv[4]
        ))).first()

    if result:
        print("{}".format(result.id))
    else:
        print("Not found")
