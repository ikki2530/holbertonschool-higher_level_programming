#!/usr/bin/python3
"""lists all State objects that contain the letter a from
the database hbtn_0e_6_usa"""


from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """lists all State objects that contain the letter a from the
        database hbtn_0e_6_usa"""
    lh = "localhost"
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    nam = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format(
            u, p, lh, d))
    Session = sessionmaker(bind=engine)
    # takes the name with state.name = nam
    session = Session().query(State).order_by(State.id).filter(
            State.name==nam)
    for row in session:
        print(row.id)
        break
    else:
        print("Not found")
