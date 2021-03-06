#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa"""


from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    """deletes all State objects with a name containing the letter a
    from the database hbtn_0e_6_usa"""
    lh = "localhost"
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'.format(
            u, p, lh, d))
    Session = sessionmaker(bind=engine)
    # Delete
    session = Session()
    all_states = session.query(State).order_by(State.id)
    for state in all_states:
        if 'a' in state.name:
            session.delete(state)
    session.commit()
