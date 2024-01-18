#!/usr/bin/python3
"""
create the program table
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime


Base = declarative_base()


class Trial(Base):
    __tablename__ = "trial"

    name = Column(String(128), primary_key=True)
    day = Column(DateTime, nullable=False)

    # class Programme(Base):
    #     """
    #     object relational mapper to the programme table
    #     """

    #     __tablename__ = 'programme'

    #     id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    #     name = Column(String, nullable=False, )


# creates student table
if __name__ == "__main__":
    from sqlalchemy import create_engine

    user = "root"
    password = "kumbisal"
    db = "mqi"
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(user, password, db)
    )
    Base.metadata.create_all(engine)
