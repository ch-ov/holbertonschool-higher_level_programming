#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

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
    state_object = State(name="Louisiana")
    session.add(state_object)
    session.commit()
    print(f"{state_object.id}")
    session.close()
