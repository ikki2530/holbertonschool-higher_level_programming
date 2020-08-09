#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""


from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """prints all City objects from the database hbtn_0e_14_usa"""
    lh = "localhost"
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format(
            u, p, lh, d))
    Session = sessionmaker(bind=engine)
    session = Session()
    # all rows(join states and cities)
    all_rows = session.query(State, City).order_by(City.id).filter(
            State.id == City.state_id).all()
    for state, city in all_rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
