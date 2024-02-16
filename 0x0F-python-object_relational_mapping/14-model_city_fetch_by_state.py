#!/usr/bin/python3
"""
prints all City objects from the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for s, c in session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id):
        print(f"{s.name}: ({c.id}) {c.name}")
