#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query_bd = session.query(State).order_by(State.id).first()
    if query_bd:
        print(f"{query_bd.id}: {query_bd.name}")
    else:
        print("Nothing")
    session.close()
